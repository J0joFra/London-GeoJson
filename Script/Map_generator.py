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

# Definire i bin ogni 500k persone
bin_width = 500000
population_bins = pd.cut(lombardia['Popolazione'], 
                         bins=range(0, lombardia['Popolazione'].max() + bin_width, bin_width), 
                         right=False, labels=False)

# Aggiungi la colonna con i bin alla geodataframe
lombardia['Population_Bin'] = population_bins

# Crea la figura e l'oggetto ax
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Definisci il gradiente di colore dal verde chiaro al verde scuro
cmap = colors.LinearSegmentedColormap.from_list(
    'green_gradient', ['#BCE784', '#9EF01A', '#69C720', '#006400', '#004B23'], N=256)

# Plotta la mappa colorata con il bordo nero, suddivisa nei bin
lombardia.plot(column='Population_Bin', cmap=cmap, legend=True, ax=ax,
               legend_kwds={'label': "Popolazione (Milioni)", 'orientation': "horizontal"},
               edgecolor='black')

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
    x, y = row['geometry'].centroid.coords[0]
    abbreviation = abbreviations.get(row['name'], '')

    # Calcola il colore per il bin di popolazione
    bin_color = cmap(row['Population_Bin'] / 5)[:3]  # Normalizza al massimo valore del bin (5 bin)
    luminance = calculate_luminance(bin_color)
    text_color = 'white' if luminance < 0.5 else 'black'
    
    # Aggiungi il testo con l'abbreviazione
    ax.text(x, y, abbreviation, fontsize=8, ha='center', color=text_color)

plt.show()
