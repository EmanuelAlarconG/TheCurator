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

    return genre_counts

def analyze_avg_duration_by_genre(songs):
    genre_durations = {}
    for song in songs:
        for genre in song.get("genre", []):
            if genre not in genre_durations:
                genre_durations[genre] = []
            genre_durations[genre].append(song.get("duration_ms", 0) / 60000)
    avg_durations = {genre: sum(durations) / len(durations) for genre, durations in genre_durations.items()}

    return avg_durations