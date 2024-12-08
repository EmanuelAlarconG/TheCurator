import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from src.api.client import fetch_playlist_data
from visualize import plot_genre_distribution
from api.client import search_similar_songs

from analyze import (
    load_playlist_data,
    analyze_genre_distribution,
    analyze_avg_duration_by_genre,
    analyze_year_of_distribution,
    analyze_top_artists,
    get_top_genres_and_artists
)

from visualize import(
    plot_genre_distribution,
    plot_avg_duration_by_genre,
    plot_release_year_distribution,
    plot_top_artists
)


def save_to_file(data, filename="playlist.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Datos guardados en '{filename}'")

def fetch_and_save_playlist():
    playlist_id = input("Introduce el ID de la playlist: ")
    songs = fetch_playlist_data(playlist_id, storefront="mx")

    if songs:
        print(f"Se encontraron {len(songs)} canciones en la playlist.")
        save_to_file(songs, filename="playlist.json")
        print("Datos guardados en 'playlist.json'")
    else:
        print("No se encontraron canciones.")

def analyze_playlist():
    songs = load_playlist_data()
    if not songs:
        print("No hay datos para analizar. Guarda una playlist primero.")
        return
    
    genre_counts = analyze_genre_distribution(songs)
    plot_genre_distribution(genre_counts)

    avg_durations = analyze_avg_duration_by_genre(songs)
    plot_avg_duration_by_genre(avg_durations)

    year_counts = analyze_year_of_distribution(songs)
    plot_release_year_distribution(year_counts)

    artist_counts = analyze_top_artists(songs)
    plot_top_artists(artist_counts)

def recommend_songs():
    songs = load_playlist_data()
    if not songs:
        print("No hay datos para generar recomendaciones.")
        return
    
    top_genres, top_artists = get_top_genres_and_artists(songs)
    print(f"Géneros predominantes: {', '.join(top_genres)}")
    print(f"Artistas predominantes: {', '.join(top_artists)}")

    recommendations = []
    for genre in top_genres:
        recommendations += search_similar_songs(genre)
    for artist in top_artists:
        recommendations += search_similar_songs(artist)
    unique_recommendations = {song["name"]: song for song in recommendations}.values()

    print("\nRecomendaciones:")
    for song in list(unique_recommendations)[:50]:
        print(f"- {song['name']} by {song['artist']} ({song['url']})")

def main():
    print("Bienvenido al sistema de análisis de Apple Music")
    print("1. Buscar y guardar playlist")
    print("2. Analizar playlist guardada")
    print("3. Generar recomendaciones")

    choice = input("Elige una opción: ")

    if choice == "1":
        fetch_and_save_playlist()
    elif choice == "2":
        analyze_playlist()
    elif choice == "3":
        recommend_songs()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
