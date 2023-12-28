import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung der durchschnittlichen Einzahlungen für jeden einzigartigen Spieler
average_deposits = data.groupby('depositor')['deposit_eth'].mean()

# Festlegung von Kategorien für die Einzahlungen
bins = [0, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, np.inf]
labels = ['<0.01', '0.01-0.1', '0.1-0.5', '0.5-1', '1-5', '5-10', '10-50', '50-100', '>100']

# Zuordnung der durchschnittlichen Einzahlungen zu Kategorien
categories = pd.cut(average_deposits, bins, labels=labels, right=False)

# Zählung der Spieler in jeder Kategorie
category_counts = categories.value_counts().sort_index()

# Erstellung des Histogramms
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Verteilung der Spieler nach durchschnittlicher Einzahlungskategorie')
plt.xlabel('Durchschnittliche Einzahlungskategorie (ETH)')
plt.ylabel('Anzahl der Spieler')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
