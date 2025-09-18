import requests

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("http://api.quotable.io/random")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        quote = data['content']
        author = data['author']
        return f'"{quote}" - {author}'
    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"