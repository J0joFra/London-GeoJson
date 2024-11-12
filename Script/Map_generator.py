import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Carica il file GeoJSON
lombardia = gpd.read_file(r"C:\Users\JoaquimFrancalanci\Downloads\Province_Italy.geojson")

# Carica il dataset con la popolazione
population_data = pd.DataFrame({
    'province': ['Milano', 'Bergamo', 'Brescia', 'Como', ...],  # Province lombarde
    'population': [1378689, 1103261, 1265805, 591958, ...]  # Popolazione per provincia
})

# Unisci i dati geografici con i dati della popolazione
lombardia = lombardia.merge(population_data, left_on="name", right_on="province")

# Plotta la mappa colorata
lombardia.plot(column='population', cmap='OrRd', legend=True)
plt.title("Popolazione per Provincia in Lombardia")
plt.show()
