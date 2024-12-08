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

def analyze_year_of_distribution(songs):
    release_years = [song.get("release_date", "")[:4] for song in songs if song.get("release_date")]
    year_counts = {year: release_years.count(year) for year in set(release_years)}
    
    return year_counts

def analyze_top_artists(songs):
    artist_counts = {}
    for song in songs:
        artist = song.get("artist", "Desconocido")
        artist_counts[artist] = artist_counts.get(artist, 0) + 1

    return dict(sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)[:10])

def get_top_genres_and_artists(songs, top_n=3):
    genres = [genre for song in songs for genre in song.get("genre", [])]
    genre_counts = {genre: genres.count(genre) for genre in set(genres)}
    top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:top_n]

    artist_counts = {}
    for song in songs:
        artist = song.get("artist", "Desconocido")
        artist_counts[artist] = artist_counts.get(artist, 0) + 1
    top_artists = sorted(artist_counts, key=artist_counts.get, reverse=True)[:top_n]

    return top_genres, top_artists