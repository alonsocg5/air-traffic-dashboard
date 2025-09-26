import pandas as pd
import utils

# --------------------- Obtenención de los datos de OpenSky ---------------------

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


# --------------------- Limpieza del dataset --------------------- 

clean_data = pd.read_csv("data/flights_raw.csv", sep=",", decimal='.')

# Quitar espacios en blanco en callsign
clean_data["callsign"] = clean_data["callsign"].str.strip()

# Eliminar filas con latitud y longitud nulas (no se conoce la posición)
clean_data = clean_data.dropna(subset=["latitude", "longitude"])

# Eliminar columna 'sensors' porque está vacía
clean_data = clean_data.drop(columns=["sensors"])

# Rellenar callsign nulos con UNKNOWN ya que es el identificador de vuelo
clean_data["callsign"] = clean_data["callsign"].fillna("UNKNOWN").str.strip()

# Eliminación de duplicados
clean_data = clean_data.drop_duplicates()

# Número de valores nulos en cada variable
print(clean_data.shape)
n_nan = clean_data.isna().sum()
print("- Número de valores nulos en cada variable:")
print(n_nan, "\n")

# Guardar limpio
df.to_csv("data/flights_clean.csv", index=False)

print("Datos limpios guardados en data/flights_clean.csv")



