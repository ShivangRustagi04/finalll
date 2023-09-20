import requests

# Define your Google Custom Search API key and search engine ID
API_KEY = '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'
SEARCH_ENGINE_ID = '520f4f246be6c4865'

# Function to perform a web search and retrieve results
def perform_web_search(query):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract search results
        results = data.get('items', [])
        
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to display search results
def display_search_results(results):
    if not results:
        print("No results found.")
        return
    
    for index, result in enumerate(results, start=1):
        title = result.get('title', 'N/A')
        link = result.get('link', 'N/A')
        snippet = result.get('snippet', 'N/A')
        
        print(f"Result {index}:")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print()

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Perform a web search based on user input
    search_results = perform_web_search(user_input)
    
    # Display search results
    display_search_results(search_results)
