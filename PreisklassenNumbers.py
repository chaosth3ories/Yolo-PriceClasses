import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung der durchschnittlichen Einzahlungen für jeden einzigartigen Spieler
average_deposits = data.groupby('depositor')['deposit_eth'].mean()

# Berechnung der Quartile und der Varianz
quartiles = average_deposits.quantile([0.25, 0.5, 0.75])
variance = average_deposits.var()

# Ausgabe der Ergebnisse
print("Quartile der durchschnittlichen Einzahlungen:")
print(quartiles)
print("\nVarianz der durchschnittlichen Einzahlungen:", variance)
