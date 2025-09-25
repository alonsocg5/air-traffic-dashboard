# ✈️ Air Traffic Dashboard  

Un **dashboard interactivo** que muestra vuelos en tiempo real a partir de la [OpenSky Network API](https://opensky-network.org/), con visualización en mapas y estadísticas de tráfico aéreo.  

---

## 🚀 Características
- 🌍 Visualización de vuelos en tiempo real en un mapa interactivo.  
- 📡 Información básica de cada vuelo (país de origen, velocidad, altitud, rumbo, etc.).  
- 📊 Gráficos con estadísticas (número de vuelos por país/aeropuerto, distribución de altitudes, etc.).  
- 🎛️ Interfaz sencilla y atractiva implementada en **Streamlit**.  
- 🤖 Módulo de predicción de retrasos usando Machine Learning.  

---

## 🛠️ Tecnologías utilizadas
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Folium](https://python-visualization.github.io/folium/)  
- [Plotly](https://plotly.com/python/)  
- [scikit-learn](https://scikit-learn.org/)

---

## 📦 Instalación y uso
1. **Clonar este repositorio**  
   ```bash
   git clone https://github.com/alonsocg5/air-traffic-dashboard.git
   cd air-traffic-dashboard
2. **Crear entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   
---

## 🔑 Configuración de la API
Este proyecto usa la API de OpenSky Network. Puedes regístrarte gratis en OpenSky Network e introducir tus credenciales en app.py o configúralas como variables de entorno.
  ```python
  USERNAME = "tu_usuario"
  PASSWORD = "tu_contraseña"
  ```
---

📊 Ejemplo de visualización
   
---

## 📂 Estructura del proyecto
```bash
air_traffic_dashboard/
│
├── app.py            # Archivo principal del dashboard
├── utils.py          # Funciones auxiliares
├── data/             # Datasets para predicción (opcional)
├── requirements.txt  # Dependencias del proyecto
└── README.md
```
---

## 👨‍💻 Autor
Desarrollado por Alonso Castañón González como portfolio personal.



