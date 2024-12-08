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
    
def decode_unicode(data):
    if isinstance(data, str):
        return data.encode('utf-8').decode('utf-8')
    elif isinstance(data, list):
        return [decode_unicode(item) for item in data]
    elif isinstance(data, dict):
        return {key: decode_unicode(value) for key, value in data.items()}
    return data

def fetch_playlist_data(playlist_id, storefront="us"):
    token = generate_token()
    url = f"https://api.music.apple.com/v1/catalog/{storefront}/playlists/{playlist_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        playlist = response.json()
        songs = playlist.get("data", [])[0].get("relationships", {}).get("tracks", {}).get("data", [])
        song_list = []

        for song in songs:
            attributes = decode_unicode(song.get("attributes", {}))
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
    
def search_similar_songs(query, limit=5, storefront="mx"):
    token = generate_token()
    url = f"https://api.music.apple.com/v1/catalog/{storefront}/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "term": query,
        "types": "songs",
        "limit": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        results = response.json()
        songs = results.get("results", {}).get("songs", {}).get("data", [])
        return [
            {
                "name": song["attributes"]["name"],
                "artist": song["attributes"]["artistName"],
                "album": song["attributes"]["albumName"],
                "genre": song["attributes"].get("genreNames", []),
                "url": song["attributes"]["url"]
            }
            for song in songs
        ]
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la búsqueda: {e}")
        return []