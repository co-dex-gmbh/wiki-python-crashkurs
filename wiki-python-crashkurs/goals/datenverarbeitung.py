import pandas as pd
import matplotlib.pyplot as plt

# Excel-Datei einlesen (Ersetze 'Pfad_zur_Datei.xlsx' durch deinen Dateipfad)
file_path = 'df_qualidy_sales_product_1.xlsx'
df = pd.read_excel(file_path)

# Sicherstellen, dass die 'DATUM'-Spalte als Datumsobjekt erkannt wird
df['DATUM'] = pd.to_datetime(df['DATUM'])

# Liste der Filialnummern erstellen
filiale_list = df['FILIALE'].unique().tolist()


def plot_sales_for_filiale(filiale):
    # Überprüfen, ob Filiale in den Daten vorhanden ist
    if filiale not in filiale_list:
        print(f"Die Filiale '{filiale}' existiert nicht in den Daten.")
        return

    # Daten für die ausgewählte Filiale filtern
    df_filiale = df[df['FILIALE'] == filiale].sort_values('DATUM')

    # Plot erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(df_filiale['DATUM'], df_filiale['SALES'], marker='o', linestyle='-', color='blue')
    plt.xlabel('Datum')
    plt.ylabel('Verkäufe')
    plt.title(f'Verkäufe im Zeitverlauf für Filiale {filiale}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


while True:
    # Benutzer nach Filialnummer fragen
    filiale = input("Bitte geben Sie die Filialnummer ein (oder 'exit' zum Beenden): ")

    if filiale.lower() == 'exit':
        break

    # Plot für die eingegebene Filialnummer anzeigen
    plot_sales_for_filiale(filiale)
