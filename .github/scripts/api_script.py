import requests
from datetime import datetime

# Replace 'YOUR_API_URL' with the actual API URL
API_URL = 'https://script.google.com/macros/s/AKfycbyrh3wEuvmOlCu2iZaA393m8WMUZHc1555RqtQp6dg4GCy_xTA936tvhydSt864VblCJg/exec?sheet=raw&action=read'

# Define the file format
file_format = 'data_%d-%m-%Y.txt'

# Create a timestamp for the current time
timestamp = datetime.now().strftime(file_format)

# Make API call
response = requests.get(API_URL)

# Check if the API call was successful (status code 200)
if response.status_code == 200:
    # Save the API response to a file
    with open(timestamp, 'w') as file:
        file.write(response.text)
    print(f"API response saved to {timestamp}")
else:
    print(f"Failed to fetch API data. Status code: {response.status_code}")
