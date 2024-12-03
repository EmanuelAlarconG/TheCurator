import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api.auth import generate_token

def main():
    print("Generando token de autenticación...")
    try:
        token = generate_token()
        print("Token generado con éxito:")
        print(token)
    except Exception as e:
        print(f"Error al generar el token: {e}")

if __name__ == "__main__":
    main()

from src.api.client import search_apple_music

def main():
    print("Buscando canciones en Apple Music...")
    term = "Justice"
    results = search_apple_music(term, storefront="mx", limit=5)

    if results:
        print("Resultados de la búsqueda:")
        for song in results.get("results", {}).get("songs", {}).get("data", []):
            print(f"- {song['attributes']['name']} by {song['attributes']['artistName']}")
    else:
        print("No se encontraron resultados para la búsqueda.")

if __name__ == "__main__":
    main()
