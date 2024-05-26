print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")
print("Just for testing")


import json
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now().isoformat()

# Create a dictionary to store the date and time
data = {
    "current_datetime": current_datetime
}

# Define the file name
file_name = "%s.json" % current_datetime

# Write the date and time to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Current date and time saved to {file_name}")
