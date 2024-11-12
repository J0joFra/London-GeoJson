import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

# Carica il file GeoJSON
lombardia = gpd.read_file("Map/Province_Italy.geojson")

# Carica il dataset con la popolazione
population_data = pd.read_excel(r"C:\Users\JoaquimFrancalanci\OneDrive - ITS Angelo Rizzoli\Desktop\Progetti\Instagram\Dataset\Lombadia 2024.xlsx", sheet_name="Sheet 1")

# Unisci i dati geografici con i dati della popolazione
lombardia = lombardia.merge(population_data, left_on="name", right_on="Provincia")

# Crea la figura e l'oggetto ax
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Definisci il gradiente di colore personalizzato
cmap = colors.LinearSegmentedColormap.from_list(
    'custom_green', ['#BCE784', '#006400'], N=256
)

# Plotta la mappa colorata con il bordo nero
lombardia.plot(column='Popolazione', cmap=cmap, legend=True, ax=ax,
               legend_kwds={'label': "Popolazione (Milioni)", 'orientation': "horizontal"},
               edgecolor='black')  # Aggiungi il bordo nero

# Rimuovi gli assi
ax.set_axis_off()

# Aggiungi le abbreviazioni delle province
abbreviations = {
    "Milano": "MI", "Monza e Brianza": "MB", "Bergamo": "BG", "Brescia": "BS", "Como": "CO",
    "Varese": "VA", "Lecco": "LC", "Lodi": "LO", "Cremona": "CR", "Mantova": "MN", "Pavia": "PV",
    "Sondrio": "SO"
}

# Funzione per calcolare la luminosità di un colore
def calculate_luminance(color):
    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# Aggiungi le abbreviazioni delle province con colore dinamico (bianco o nero)
for idx, row in lombardia.iterrows():
    # Recupera il centroide della provincia per posizionare l'abbreviazione
    x, y = row['geometry'].centroid.coords[0]
    abbreviation = abbreviations.get(row['name'], '')
    
    # Ottieni il colore del poligono (background)
    color = cmap(row['Popolazione'] / lombardia['Popolazione'].max())[:3]  # Normalizza il valore della popolazione
    luminance = calculate_luminance(color)
    
    # Scegli il colore dell'abbreviazione (bianco se il fondo è scuro, nero se chiaro)
    text_color = 'white' if luminance < 0.5 else 'black'
    
    ax.text(x, y, abbreviation, fontsize=8, ha='center', color=text_color)

# Titolo
plt.title("Popolazione per Provincia in Lombardia", fontsize=16)

# Mostra la mappa
plt.show()



