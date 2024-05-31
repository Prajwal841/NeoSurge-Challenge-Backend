import requests

class GPT35Service:
    def __init__(self):
        # Initialize the API URL
        self.api_url = "https://api.openai.com/v1/chat/completions"

    def generate_insight(self, prompt, api_key):
        # Set up the request headers with API key and content type
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        # Prepare the data payload for the API request
        data = {
            "model": "gpt-3.5-turbo",  # Specify the GPT-3.5 model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},  # System message
                {"role": "user", "content": prompt}  # User-provided prompt
            ],
            "max_tokens": 500,  # Set maximum number of tokens for response
        }
        # Send a POST request to the API endpoint
        response = requests.post(self.api_url, headers=headers, json=data)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the generated message
            return response.json()["choices"][0]["message"]["content"]
        else:
            # If there was an error, return an error message
            return "Error: " + response.text
