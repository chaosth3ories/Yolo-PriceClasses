import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung, ob ein Spieler immer denselben Betrag einsetzt
consistent_deposit = data.groupby('depositor')['deposit_eth'].nunique() == 1
probability_consistent = consistent_deposit.mean()

# Ausgabe der Wahrscheinlichkeit
print("Wahrscheinlichkeit, dass ein Spieler immer mit demselben Betrag setzt:", probability_consistent)
