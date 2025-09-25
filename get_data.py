import pandas as pd
import utils


# Columnas del DataFrame
columns = [
    "icao24", "callsign", "origin_country", "time_position", "last_contact",
    "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
    "true_track", "vertical_rate", "sensors", "geo_altitude", "squawk",
    "spi", "position_source"
]

# Se obtiene el token
token, token_expiry = utils.get_access_token()

# Se comprueba si el token es válido, si lo es obtenemos los datos; 
# si no obtenemos uno nuevo y posteriormente los datos
try:
    data = utils.get_opensky_data(token)
except ValueError:
    # Token expirado, obtenemos uno nuevo
    print("Token expirado, obteniendo uno nuevo...")
    token, token_expiry = utils.get_access_token()
    data = utils.get_opensky_data(token)

# Crear DataFrame
df = pd.DataFrame(data.get("states", []), columns=columns)

# Guardar CSV con los datos
df.to_csv("data/flights_raw.csv", index=False)
print("Datos guardados en data/flights_raw.csv")
print(df.head())