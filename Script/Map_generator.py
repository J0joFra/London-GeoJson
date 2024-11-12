import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Carica il file GeoJSON
lombardia = gpd.read_file("Map/Province_Italy.geojson")

# Carica il dataset con la popolazione da Excel
population_data = pd.read_excel(r"C:\Users\JoaquimFrancalanci\OneDrive - ITS Angelo Rizzoli\Desktop\Progetti\Instagram\Dataset\Lombadia 2024.xlsx", sheet_name="Sheet 1")

# Unisci i dati geografici con i dati della popolazione
lombardia = lombardia.merge(population_data, left_on="name", right_on="Provincia")

# Crea la figura e l'oggetto ax
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Plotta la mappa colorata
lombardia.plot(column='Popolazione', cmap='Greens', legend=True, ax=ax,
               legend_kwds={'label': "Popolazione (Milioni)", 'orientation': "horizontal"},
               edgecolor='black')

# Rimuovi gli assi
ax.set_axis_off()

# Aggiungi le abbreviazioni delle province
abbreviations = {
    "Milano": "MI", "Monza e Brianza": "MB", "Bergamo": "BG", "Brescia": "BS", "Como": "CO",
    "Varese": "VA", "Lecco": "LC", "Lodi": "LO", "Cremona": "CR", "Mantova": "MN", "Pavia": "PV",
    "Sondrio": "SO", "Cremona": "CR", "Varese": "VA", "Pavia": "PV"
}

for idx, row in lombardia.iterrows():
    # Recupera il centroide della provincia per posizionare l'abbreviazione
    x, y = row['geometry'].centroid.coords[0]
    abbreviation = abbreviations.get(row['name'], '')
    ax.text(x, y, abbreviation, fontsize=5, ha='center', color='black')

# Titolo
plt.title("Popolazione per Provincia in Lombardia", fontsize=16)

# Mostra la mappa
plt.show()
