import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Carica il file GeoJSON
lombardia = gpd.read_file("Map/Province_Italy.geojson")

# Carica il dataset con la popolazione da Excel
population_data = pd.read_excel(r"C:\Users\JoaquimFrancalanci\OneDrive - ITS Angelo Rizzoli\Desktop\Progetti\Instagram\Dataset\Lombadia 2024.xlsx", sheet_name="Sheet 1")

# Unisci i dati geografici con i dati della popolazione
lombardia = lombardia.merge(population_data, left_on="name", right_on="province")

# Plotta la mappa colorata
lombardia.plot(column='population', cmap='OrRd', legend=True)
plt.title("Popolazione per Provincia in Lombardia")
plt.show()
