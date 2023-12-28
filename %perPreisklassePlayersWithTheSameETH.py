import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Definition von Preisklassen
bins = [0, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, float('inf')]
labels = ['<0.01', '0.01-0.1', '0.1-0.5', '0.5-1', '1-5', '5-10', '10-50', '50-100', '>100']

# Berechnung der durchschnittlichen Einzahlung pro Spieler
average_deposit_per_player = data.groupby('depositor')['deposit_eth'].mean()

# Zuordnung der Spieler zu Preisklassen
player_class = pd.cut(average_deposit_per_player, bins, labels=labels, right=False)

# Hinzufügen der Preisklassen zu den ursprünglichen Daten
data_with_class = data.join(player_class, on='depositor', rsuffix='_class')

# Berechnung der Wahrscheinlichkeit für jede Preisklasse
probabilities_per_class = data_with_class.groupby(['deposit_eth_class', 'depositor'])['deposit_eth'].nunique().eq(1).groupby(level=0).mean()

# Ausgabe der Wahrscheinlichkeiten pro Preisklasse
print("Wahrscheinlichkeit pro Preisklasse, dass ein Spieler immer mit demselben Betrag spielt:")
print(probabilities_per_class)
