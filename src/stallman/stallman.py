#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
import sys
from bs4 import BeautifulSoup
import re

feed = "https://stallman.org/rss/rss.xml"

# Function to fetch and parse the XML feed
def fetch_and_parse_feed(feed_url):
    try:
        response = requests.get(feed_url)
        response.raise_for_status()  # Raise an error for bad responses
        xml_content = response.content.decode('utf-8')
        root = ET.fromstring(xml_content)
        return root
    except requests.exceptions.RequestException as e:
        print(f"Error fetching feed: {e}")
        sys.exit(1)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)


# Function to extract information from an item
def extract_item_info(item, namespaces):
    title = item.find('title').text if item.find('title') is not None else ''
    link = item.find('link').text if item.find('link') is not None else ''
    description = item.find('description').text if item.find('description') is not None else ''
    # Convert HTML description to plain text
    soup = BeautifulSoup(description, 'html.parser')
    description = soup.get_text()
    creator = item.find('dc:creator', namespaces).text if item.find('dc:creator', namespaces) is not None else ''
    encoded_content = item.find('content:encoded', namespaces).text if item.find('content:encoded', namespaces) is not None else '' # Get full content
    return {
        'title': title,
        'link': link,
        'description': description,
        'creator': creator,
        'content': encoded_content
    }

def strip_tags(html):
    """Strip HTML tags from a string."""
    return re.sub('<[^<]+?>', '', html)

def fetch_and_extract_article(url):
    """Fetches the article from the URL and extracts the text content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Attempt to extract the main article content.  Adjust this based on the target website's structure.
        article = soup.find('div', class_='article') or soup.find('article') or soup.find('div', id='content') or soup  # Example selectors - adjust as needed

        if article:
            text = article.get_text(separator='\n', strip=True)  # Get text with line breaks
            return text
        else:
            return "Could not extract article content."

    except requests.exceptions.RequestException as e:
        return f"Error fetching article: {e}"
    except Exception as e:
        return f"Error processing article: {e}"


def display_item_list(items, read_items):
    """Displays the list of item titles with numbers for selection, marking read items."""
    print("\nAvailable Articles:")
    for i, item in enumerate(items):
        read_marker = "[READ]" if i in read_items else ""
        print(f"{i+1}. {item['title']} {read_marker}")
    print("0. Exit")

def display_article_text(text):
    """Displays the extracted article text."""
    print("\n--- Article Content ---")
    print(text)
    print("\n--- End of Article ---")


def display_item_details(item, item_index, items, read_items):
    """Displays the details of a selected item and provides options to read the linked article."""
    while True:
        print("--------------------------------------")
        for key, value in item.items():
            print(f"{key}: {strip_tags(str(value))}")  # Strip HTML tags for cleaner display
        print("--------------------------------------")
        print("1. Read linked article")
        print("2. Back to article list")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if item['link']:
                article_text = fetch_and_extract_article(item['link'])
                display_article_text(article_text)

                while True:
                    back_choice = input("Enter 'b' to go back to the article details, 'm' for main menu, or '0' to exit: ").lower()
                    if back_choice == 'b':
                        break
                    elif back_choice == 'm':
                        return True  # Signal to return to the main menu
                    elif back_choice in ('0', 'q'):
                        print("Exiting...")
                        sys.exit(0)  # Exit the script
                    else:
                        print("Invalid choice.")


            else:
                print("This article has no link.")
        elif choice == '2':
            return True # Signal to return to the main menu.
        elif choice in ('0', 'q'):
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice.")


def main():
    """Main function to drive the RSS feed interaction."""
    root = fetch_and_parse_feed(feed)
    namespaces = {'dc': 'http://purl.org/dc/elements/1.1/',
                  'content': 'http://purl.org/rss/1.0/modules/content/'}
    items_elements = root.findall('.//item')
    items = [extract_item_info(item, namespaces) for item in items_elements]  # Extract and store item data
    read_items = set() # Keep track of read item indices


    while True:
        display_item_list(items, read_items)

        choice = input("Enter the number of the article to view (or 0/q to exit): ")

        if choice in ('0', 'q'):
            print("Exiting...")
            break

        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(items):
                #Display Item Details
                if display_item_details(items[choice_index], choice_index, items, read_items):
                    read_items.add(choice_index)  # Mark as read if user viewed or linked page.
                else:
                    read_items.add(choice_index)
                    break #Exit
                read_items.add(choice_index)  # Mark as read
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
