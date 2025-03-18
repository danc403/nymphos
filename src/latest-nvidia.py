import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import json
import argparse
import os
import tarfile
from packaging.version import parse as parse_version

index_url = "https://developer.download.nvidia.com/compute/cuda/redist/"
CUDA_DOWNLOAD_DIR = "nymph-cuda"
NVIDIA_DOWNLOAD_DIR = "nymph-nvidia"
DRIVER_PACKAGE_NAME = "nvidia_driver"
MISSING_LIBS = ["libnvidia_nscq", "libnvsdm"]
DRIVER_URL_BASE = "https://developer.download.nvidia.com/compute/nvidia-driver/redist/"
REQUIREMENTS_FILE = "requirements.txt"
REQUIREMENTS_HTML_PATH_IN_TARBALL = "docs/minimumrequirements.html"

def get_page_content(url):
    """Fetches the content of a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def check_url_exists(url):
    """Checks if a URL exists by making a HEAD request."""
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def parse_initial_index(html_content, base_url):
    """
    Parses the initial index page and extracts the link to the latest redistrib JSON.
    """
    latest_redistrib_json = None
    redistrib_files = []
    soup = BeautifulSoup(html_content, 'html.parser')

    for link_tag in soup.find_all('a'):
        href = link_tag.get('href')
        if href and href.startswith('redistrib_') and href.endswith('.json'):
            full_url = urljoin(base_url, href)
            version_match = re.search(r'redistrib_([\d.]+)\.json', href)
            if version_match:
                try:
                    redistrib_files.append((full_url, parse_version(version_match.group(1))))
                except ValueError:
                    print(f"Could not parse version from {href}")

    if redistrib_files:
        latest = max(redistrib_files, key=lambda item: item[1])
        latest_redistrib_json = latest[0]

    return latest_redistrib_json

def get_package_info_from_json(json_url, base_url, target_platforms, include_patterns):
    """
    Fetches and parses the redistrib JSON and extracts information about packages,
    specifically looking for driver components.
    """
    json_content = get_page_content(json_url)
    if not json_content:
        return []

    try:
        data = json.loads(json_content)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {json_url}")
        return []

    packages = []
    for package_name, details in data.items():
        if include_patterns and not any(pattern in package_name for pattern in include_patterns) and package_name != DRIVER_PACKAGE_NAME:
            continue

        version = details.get("version")
        for platform in target_platforms:
            platform_info = details.get(platform)
            if platform_info:
                relative_path = platform_info.get("relative_path")
                if relative_path:
                    download_url = urljoin(base_url, relative_path)
                    packages.append({
                        "name": package_name,
                        "version": version,
                        "platform": platform,
                        "download_url": download_url,
                        "relative_path": relative_path,
                        "is_driver_package": package_name == DRIVER_PACKAGE_NAME,
                        "is_driver_assistant": package_name == "driver_assistant"
                    })
    return packages

def download_package(url, destination_path):
    """Downloads a package from a URL to a specified path, checking if the file exists."""
    if os.path.exists(destination_path):
        print(f"File already exists: {destination_path}. Skipping download.")
        return True

    try:
        print(f"Downloading {url} to {destination_path}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destination_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded successfully to {destination_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False

def get_output_directory(package_name, platform):
    """Determines the output directory based on package name, using simpler arch names."""
    arch_name = platform.replace("linux-", "")  # Remove the "linux-" prefix
    if package_name == DRIVER_PACKAGE_NAME or "driver" in package_name:
        return os.path.join(NVIDIA_DOWNLOAD_DIR, arch_name)
    else:
        return os.path.join(CUDA_DOWNLOAD_DIR, arch_name)

def extract_and_write_requirements(tarball_path):
    """Extracts minimum requirements from the driver tarball and writes to a file."""
    requirements = {}
    try:
        with tarfile.open(tarball_path, 'r:*') as tar:
            try:
                doc_file = tar.extractfile(REQUIREMENTS_HTML_PATH_IN_TARBALL)
                if doc_file:
                    html_content = doc_file.read().decode('utf-8', errors='ignore')
                    soup = BeautifulSoup(html_content, 'html.parser')

                    # Parse the first table (Software Requirements)
                    software_section = soup.find('div', {'id': 'MinimumSoftware2486a'})
                    if software_section:
                        software_table = software_section.find_next('div', class_='informaltable').find('table')
                        if software_table:
                            rows = software_table.find_all('tr')[1:]
                            for row in rows:
                                cols = row.find_all('td')
                                if len(cols) == 3:
                                    software = cols[0].text.strip()
                                    versions = cols[1].text.strip()
                                    requirements[software] = versions

                    # Parse the second table (Build Requirements)
                    build_section = software_section.find_next('p').find_next('div', class_='informaltable')
                    if build_section:
                        build_table = build_section.find('table')
                        if build_table:
                            rows = build_table.find_all('tr')[1:]
                            for row in rows:
                                cols = row.find_all('td')
                                if len(cols) == 3:
                                    software = cols[0].text.strip()
                                    version = cols[1].text.strip()
                                    requirements[f"Build: {software}"] = version

                else:
                    print(f"Warning: {REQUIREMENTS_HTML_PATH_IN_TARBALL} not found in {tarball_path}")
            except KeyError:
                print(f"Warning: {REQUIREMENTS_HTML_PATH_IN_TARBALL} not found in {tarball_path}")

        if requirements:
            requirements_file_path = os.path.join(os.path.dirname(tarball_path), REQUIREMENTS_FILE)
            with open(requirements_file_path, 'w') as f:
                f.write("NVIDIA Driver Minimum Requirements:\n")
                for req, value in requirements.items():
                    f.write(f"- {req}: {value}\n")
                print(f"Minimum requirements written to {requirements_file_path}")
            return True
        else:
            print("Warning: Could not extract minimum requirements from HTML.")
            return False

    except FileNotFoundError:
        print(f"Error: Tarball not found: {tarball_path}")
        return False
    except Exception as e:
        print(f"An error occurred while processing the tarball: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List or download CUDA and driver packages from NVIDIA redistrib.")
    parser.add_argument("-a", "--arch", choices=['x86_64', 'aarch64', 'both'], default='x86_64',
                        help="Target architecture (x86_64, aarch64, or both).")
    parser.add_argument("-d", "--download", action="store_true", help="Download the packages.")
    parser.add_argument("-j", "--show-json", action="store_true", help="Print the content of the latest redistrib JSON.")
    args = parser.parse_args()

    html_content = get_page_content(index_url)
    if html_content:
        latest_json_url = parse_initial_index(html_content, index_url)
        if latest_json_url:
            print(f"Using redistrib JSON: {latest_json_url}")

            if args.show_json:
                json_content = get_page_content(latest_json_url)
                if json_content:
                    print("\n--- JSON Content ---")
                    print(json_content)
                    print("--- End of JSON Content ---")
                else:
                    print(f"Could not retrieve JSON content from {latest_json_url}")
                exit()  # Exit after showing the JSON

            target_platforms = []
            if args.arch == 'x86_64':
                target_platforms.append("linux-x86_64")
            elif args.arch == 'aarch64':
                target_platforms.append("linux-aarch64")
            elif args.arch == 'both':
                target_platforms.extend(["linux-x86_64", "linux-aarch64"])

            include_patterns = ["cublas", "cudart", "nvcc", "nvrtc"] # Removed "driver" from general includes

            package_info = get_package_info_from_json(
                latest_json_url,
                index_url,
                target_platforms,
                include_patterns
            )

            driver_version = None
            selected_arch = target_platforms[0] if target_platforms else None # Assume first arch if multiple
            driver_download_path = None

            for package in package_info:
                if package['name'] == DRIVER_PACKAGE_NAME and selected_arch in package['platform']:
                    driver_version = package['version']
                    if args.download:
                        output_dir = get_output_directory(package['name'], package['platform'])
                        os.makedirs(output_dir, exist_ok=True)
                        filename = package['relative_path'].split('/')[-1]
                        driver_download_path = os.path.join(output_dir, filename)
                        download_successful = download_package(package['download_url'], driver_download_path)
                        if download_successful:
                            extract_and_write_requirements(driver_download_path)
                    break

            if driver_version and selected_arch:
                print("\nChecking for additional driver libraries...")
                for lib_name in MISSING_LIBS:
                    base_filename = f"{lib_name}-{selected_arch}-{driver_version}-archive.tar.xz"
                    download_url = urljoin(DRIVER_URL_BASE, f"{lib_name}/{selected_arch}/{base_filename}")
                    output_dir = os.path.join(NVIDIA_DOWNLOAD_DIR, selected_arch)
                    os.makedirs(output_dir, exist_ok=True)
                    destination_path = os.path.join(output_dir, base_filename)

                    if check_url_exists(download_url):
                        print(f"Found additional library: {lib_name}")
                        print(f"  Download URL: {download_url}")
                        if args.download:
                            download_package(download_url, destination_path)
                        print("-" * 20)
                    else:
                        print(f"Additional library not found: {lib_name} at {download_url}")

            if package_info:
                print("\nIdentified Packages from redistrib JSON:")
                current_version = None
                recommended_driver_version = None
                driver_package = None
                driver_assistant_package = None

                if package_info:
                    current_version = package_info[0]['version']
                    print(f"Version from redistrib JSON: {current_version}\n")

                for package in package_info:
                    print(f"- Name: {package['name']}")
                    print(f"  Platform: {package['platform']}")
                    print(f"  Version: {package['version']}")
                    print(f"  Download URL: {package['download_url']}")
                    if package['is_driver_package']:
                        print("  ** NVIDIA Driver Package **")
                        driver_package = package
                        recommended_driver_version = package['version']
                    elif package['is_driver_assistant']:
                        print("  (Driver Assistant)")
                        driver_assistant_package = package

                    if args.download and package['name'] != DRIVER_PACKAGE_NAME: # Driver already handled above
                        output_dir = get_output_directory(package['name'], package['platform'])
                        os.makedirs(output_dir, exist_ok=True)
                        filename = package['relative_path'].split('/')[-1]
                        destination_path = os.path.join(output_dir, filename)
                        download_package(package['download_url'], destination_path)
                    print("-" * 20)

                if recommended_driver_version:
                    print(f"\nRecommended Driver Version: {recommended_driver_version}")
                    if driver_package:
                        print(f"  Driver Package: {driver_package['name']}")
                        print(f"  Download URL: {driver_package['download_url']}")
                else:
                    print("\nDriver information not found in the manifest.")

            else:
                print("No packages found matching the criteria.")
        else:
            print("Could not find the latest redistrib JSON URL.")
    else:
        print("Failed to retrieve the index page.")
