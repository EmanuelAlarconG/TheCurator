import jwt
import time
from dotenv import load_dotenv
import os

load_dotenv()

_token_cache = None
_token_expiry = 0

def generate_token():

    global _token_cache, _token_expiry

    current_time = int(time.time())
    if _token_cache and current_time < _token_expiry:
        return _token_cache

    key_id = os.getenv("APPLE_MUSIC_KEY_ID")
    team_id = os.getenv("APPLE_MUSIC_TEAM_ID")
    private_key_path = os.getenv("APPLE_MUSIC_PRIVATE_KEY_PATH")

    if not all([key_id, team_id, private_key_path]):
        raise ValueError("Las credenciales no están configuradas correctamente en .env")
    
    try:
        with open(private_key_path, "r") as f:
            private_key = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró la clave privada en {private_key_path}.")
    
    _token_cache = jwt.encode(
        {
            "iss": team_id,
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600,
        },
        private_key,
        algorithm="ES256",
        headers={"alg": "ES256", "kid": key_id},
    )
    
    _token_expiry = current_time + 3600
    return _token_cache