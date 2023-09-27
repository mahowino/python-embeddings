import requests

# Replace with the actual URL where your Flask server is running
base_url = "http://localhost:5000/store_embedding"

# Sample data to store
data = {
    "id": "unique_vector_id",
    "embedding": [0.1, 0.2, 0.3, 0.4, 0.5]  # Replace with your actual embedding values
}

# Send a POST request to the /store_embedding endpoint
response = requests.post(base_url, json=data)

# Check the response
if response.status_code == 200:
    print("Embedding stored successfully.")
else:
    print("Failed to store embedding. Response:", response.status_code, response.text)
