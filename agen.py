import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the API keys from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

# Check if keys are loaded correctly
if not google_api_key or not google_cse_id:
    print("Error: Missing GOOGLE_API_KEY or GOOGLE_CSE_ID in .env file")
    exit()

# Function to query Google Custom Search Engine
def google_search(query, api_key, cse_id):
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": 3  # Number of results to retrieve
    }
    
    try:
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error making the request: {err}")
    return None

# Function to initialize LangChain agent
def initialize_agent():
    agent = "Your agent setup here"
    return agent

# Function to process the query with your AI agent
def process_query(query, api_key, cse_id):
    if query.lower() == "exit":
        return "Goodbye!"

    search_results = google_search(query, api_key, cse_id)
    if search_results:
        print("Google search results:")
        for item in search_results.get('items', []):
            print(item['title'], item['link'])

    agent_response = "Processing query with agent..."
    agent = initialize_agent()
    return agent_response

# Main function to start the chatbot interaction
def chatbot():
    print("🤖 Agent Ready! Ask anything (type 'exit' to quit):")
    
    while True:
        query = input("🔍 Your Query: ")
        if query.lower() == 'exit':
            break
        response = process_query(query, google_api_key, google_cse_id)
        print(response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
