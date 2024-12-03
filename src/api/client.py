import requests
from .auth import generate_token

def search_apple_music(term, storefront="us", limit=5):
    token = generate_token()
    url = f"https://api.music.apple.com/v1/catalog/{storefront}/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "term": term,
        "limit": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None