import json

def load_playlist_data(filename="playlist.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{filename}'. Por favor, genera la playlist primero.")
        return []
    
def analyze_genre_distribution(songs):
    genres = [genre for song in songs for genre in song.get("genre", [])]
    genre_counts = {genre: genres.count(genre) for genre in set(genres)}

    print("Distribución de géneros en la playlist:")
    for genre, count in genre_counts.items():
        print(f"{genre}: {count} canciones")

    return genre_counts