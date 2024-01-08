import os
import requests
from datetime import datetime

# Replace 'YOUR_API_URL' with the actual API URL
API_URL = 'https://script.google.com/macros/s/AKfycbyrh3wEuvmOlCu2iZaA393m8WMUZHc1555RqtQp6dg4GCy_xTA936tvhydSt864VblCJg/exec?sheet=raw&action=read'

# Define the file format
file_format = 'daa_%d-%m-%Y.json'

# Create a timestamp for the current time
timestamp = datetime.now().strftime(file_format)

# Specify the full path where the file should be saved
file_path = os.path.join(os.environ['GITHUB_WORKSPACE'], f'{timestamp}.json')

# Make API call
response = requests.get(API_URL)

# Check if the API call was successful (status code 200)
if response.status_code == 200:
    # Save the API response to the specified file path
    with open(file_path, 'w') as file:
        file.write(response.text)
    print(f"API response saved to {file_path}")

    # Add, commit, and push the file to GitHub
    os.system(f'git add {file_path}')
    os.system(f'git commit -m "Add API response file {timestamp}"')
    os.system('git push origin main')  # Replace 'main' with your branch name

else:
    print(f"Failed to fetch API data. Status code: {response.status_code}")
