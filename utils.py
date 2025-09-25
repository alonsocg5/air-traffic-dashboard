import requests

# -----------------------------------
# Configuración de credenciales
# -----------------------------------
CLIENT_ID = "alonsocg5-api-client"
CLIENT_SECRET = "aw55UPkw3KR3expb6BIBTWrKYZPCYFot"

AUTH_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
API_URL = "https://opensky-network.org/api/states/all"

# -----------------------------------
# Función para obtener token OAuth2
# -----------------------------------
def get_access_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(AUTH_URL, data=payload)
    response.raise_for_status()
    token_data = response.json()
    access_token = token_data.get("access_token")
    expires_in = token_data.get("expires_in", 1800)  # duración del token en segundos
    return access_token, expires_in

# -----------------------------------
# Función para obtener datos de OpenSky
# -----------------------------------
def get_opensky_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        # Token expirado
        raise ValueError("Token expirado o inválido")
    else:
        response.raise_for_status()