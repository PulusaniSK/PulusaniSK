import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Check if data is a list and not empty
        if isinstance(data, list) and len(data) > 0:
            # Open the CSV file for writing
            with open(csv_file_path, mode='w', newline='') as csv_file:
                # Create a CSV writer object
                csv_writer = csv.writer(csv_file)

                # Write the header
                header = data[0].keys()
                csv_writer.writerow(header)

                # Write the data rows
                for row in data:
                    csv_writer.writerow(row.values())

            print(f"JSON data successfully written to {csv_file_path}")
        else:
            print("JSON data is not a list or is empty")

    except json.JSONDecodeError:
        print("Failed to decode JSON. Please check the JSON file for syntax errors.")
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


