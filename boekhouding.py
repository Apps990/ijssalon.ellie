# Importeer alle functies en variabelen
from helper import *
from presentatie import *

# Importeer het csv-pakket
import csv

# Dictionary met inkomsten
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# Bereken de totale inkomsten
totaal_inkomsten = som(inkomsten)

# Presenteer de inkomsten
presenteer(inkomsten, totaal_inkomsten)

# Schrijf de inkomsten naar een csv-bestand
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')

    for key, value in inkomsten.items():
        writer.writerow([key, value])