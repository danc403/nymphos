import json
import os

def write_spec_file(spec_data, filename):
  """Writes the given spec data to a file."""

  with open(filename, 'w') as f:
    for section, values in spec_data.items():
      f.write(f"{section}:")
      if isinstance(values, list):
        for value in values:
          if isinstance(value, dict):  # For Changelog entries
            f.write("\n  -")
            for key, subvalue in value.items():
              f.write(f"\n    {key}: {subvalue}")
          else:
            f.write(f"\n  - {value}")
      else:
        f.write(f" {values}")
      f.write("\n")

def main():
  """Parses JSON files and writes .spec files."""

  for filename in os.listdir():
    if filename.endswith(".json"):
      with open(filename, 'r') as f:
        data = json.load(f)

      for spec_name, spec_data in data.items():
        if spec_name.endswith(".spec"):
          output_filename = spec_name
          write_spec_file(spec_data, output_filename)

if __name__ == "__main__":
  main()
