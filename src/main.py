import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from src.api.client import fetch_playlist_data
from visualize import plot_genre_distribution

from analyze import (
    load_playlist_data,
    analyze_genre_distribution,
    analyze_avg_duration_by_genre,
    analyze_year_of_distribution,
    analyze_top_artists
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

def main():
    print("Bienvenido al sistema de análisis de Apple Music")
    print("1. Buscar y guardar playlist")
    print("2. Analizar playlist guardada")

    choice = input("Elige una opción: ")

    if choice == "1":
        fetch_and_save_playlist()
    elif choice == "2":
        analyze_playlist()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
