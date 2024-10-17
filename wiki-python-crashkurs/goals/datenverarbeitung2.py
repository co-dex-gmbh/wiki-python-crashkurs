import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Excel-Datei einlesen (Ersetze 'Pfad_zur_Datei.xlsx' durch deinen Dateipfad)
file_path = 'df_qualidy_sales_product_1.xlsx'
df = pd.read_excel(file_path)

# Sicherstellen, dass die 'DATUM'-Spalte als Datumsobjekt erkannt wird
df['DATUM'] = pd.to_datetime(df['DATUM'])

# Gesamte Verkaufszahlen pro Filiale berechnen
sales_per_filiale = df.groupby('FILIALE')['SALES'].sum().reset_index()

# Z-Score der Verkaufszahlen berechnen, um Abweichungen zu erkennen
sales_per_filiale['Z_Score'] = zscore(sales_per_filiale['SALES'])

# Schwellenwert für Ausreißer festlegen (z.B. Z-Score > 2 oder < -2)
outliers = sales_per_filiale[(sales_per_filiale['Z_Score'] > 2) | (sales_per_filiale['Z_Score'] < -2)]

# Ergebnis anzeigen
print("Gesamte Verkaufszahlen pro Filiale:")
print(sales_per_filiale)

print("\nFilialen mit signifikant abweichenden Verkaufszahlen:")
print(outliers)

# Plot der Verkaufszahlen mit Hervorhebung der Ausreißer
plt.figure(figsize=(10, 6))
plt.bar(sales_per_filiale['FILIALE'], sales_per_filiale['SALES'], label='Filialen')
plt.scatter(outliers['FILIALE'], outliers['SALES'], color='red', label='Ausreißer', zorder=5)
plt.xlabel('Filiale')
plt.ylabel('Gesamtverkäufe')
plt.title('Gesamtverkäufe pro Filiale mit Hervorhebung von Ausreißern')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
