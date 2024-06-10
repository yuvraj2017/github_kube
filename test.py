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
from datetime import datetime, date
from random import randint, randrange

# Get the current date and time
# current_datetime = datetime.now().isoformat()
current_date = date.today()

random_number = randint(0, 100000)
print("random number", random_number)

# Create a dictionary to store the date and time
data = {
    "current_datetime": current_date.isoformat(),
    "random number": random_number    
}

# Define the file name
file_name = "yash.json"
print(file_name)
print(type(data))

# Write the date and time to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Current date and time saved to {file_name}")
