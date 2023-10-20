#Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it 
#into a file called "cso.json".

#Upload this program to the same repository you used for the XML assignment
#Save this assignment as "assignment03-cso.py"


import requests
import json

# Define the URL of the dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON content from the response
    data = response.json()

    # Save the JSON data to a file named "cso.json"
    with open("cso.json", "w") as file:
        json.dump(data, file)

    print("Dataset saved to 'cso.json'")
else:
    print("Failed to retrieve the dataset.")