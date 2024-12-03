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

def fetch_song_data(term, storefront="us", limit=10):
    token = generate_token()
    url = f"https://api.music.apple.com/v1/catalog/{storefront}/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "term": term,
        "limit": limit,
        "types": "songs"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        songs = response.json().get("results", {}).get("songs", {}).get("data", [])
        song_list = []

        for song in songs:
            attributes = song.get("attributes", {})
            song_list.append({
                "id": song.get("id"),
                "name": attributes.get("name"),
                "artist": attributes.get("artistName"),
                "album": attributes.get("albumName"),
                "genre": attributes.get("genreNames", []),
                "duration_ms": attributes.get("durationInMillis"),
                "release_date": attributes.get("releaseDate"),
                "url": attributes.get("url"),
            })

        return song_list
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return []