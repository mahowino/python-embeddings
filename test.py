import requests

# Replace with the actual URL where your Flask server is running
base_url = "http://localhost:5000/search"

# Sample data to store
data = {"query": "Who is Mike Kalya?",}

# Send a POST request to the /store_embedding endpoint
# response = requests.post(base_url, json=data)
response=requests.post(base_url,json=data)


# Check the response
if response.status_code == 200:
    # Print the response body
    print("Response Body:", response.text)
else:
    print("Failed to store embedding. Response:", response.status_code, response.text)