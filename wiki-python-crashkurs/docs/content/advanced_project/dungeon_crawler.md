# Dungeon Crawler Projekt

In diesem fortgeschrittenen Projekt werden wir einen Dungeon Crawler entwickeln. Wir beginnen mit einer textbasierten Version in der Konsole und erweitern das Spiel später um eine grafische Benutzeroberfläche mit Tkinter.

## Teil 1: Textbasierter Dungeon Crawler

### Aufgabe 1: Grundstruktur

Erstelle eine Datei namens `dungeon_crawler.py` und implementiere die folgenden Funktionen:

1. `create_dungeon(width, height)`: Erstellt ein zufälliges Dungeon (Labyrinth) als 2D-Liste.
2. `print_dungeon(dungeon, player_pos)`: Gibt das Dungeon in der Konsole aus.
3. `move_player(dungeon, player_pos, direction)`: Bewegt den Spieler in die angegebene Richtung.
4. `main_game_loop()`: Hauptschleife des Spiels, die Benutzereingaben verarbeitet und das Spiel steuert.

### Aufgabe 2: Spiellogik

Erweitere das Spiel um folgende Funktionen:

1. Füge Schätze und Monster zum Dungeon hinzu.
2. Implementiere ein einfaches Kampfsystem.
3. Füge eine Inventarfunktion für den Spieler hinzu.
4. Erstelle verschiedene Levels mit steigender Schwierigkeit.

### Aufgabe 3: Rundenbasiertes Kampfsystem

Implementiere ein einfaches rundenbasiertes Kampfsystem. Spieler und Monster teilen sich mindestens folgende drei Attribute:

a. Lebenspunkte: Sinken diese auf 0 ist ein Kämpfer besiegt und hat den Kampf verloren.
b. Angriffskraft: Hier wird der Schaden an den Lebenspunkten des Gegners bei einem Angriff festgehalten.
c. Trefferwahrscheinlichkeit: Hier wird die Wahrscheinlichkeit angegeben, mit der ein Kämpfer bei einem Angriff trifft.

#### Ablauf des Kampfes:

a. Wer beginnt:
Wer den Kampf beginnt wird anhand der ATK-Punkte der Kämpfer bestimmt. Hierzu wird die ATK vom Spieler und vom Monster addiert. Anschließend wird eine Zufallszahl, die zwischen 1 und dieser Summe liegt, ermittelt. Sollte diese Zufallszahl größer als die ATK vom Spieler sein fängt das Monster an und sollte sie kleiner sein, fängt der Spieler an.

b. Spielerrunde:
Sobald der Spieler an der Reihe ist, soll er mehrere Auswahlmöglichkeiten haben:

i. Flucht - Der Spieler versucht zu fliehen.
Wenn der Spieler Flucht auswählt, soll seine Fluchtwahrscheinlichkeit jedes Mal neu berechnet werden. Die Fluchtwahrscheinlichkeit berechnet sich aus einer zufälligen Zahl zwischen 0 und 50% plus 15% pro Fluchtversuch. Somit hat der Spieler eine steigende Fluchtwahrscheinlichkeit bei aufeinanderfolgenden Fluchtversuchen. Sollte er erfolgreich geflohen sein ist der Kampf beendet ansonsten ist das Monster an der Reihe.
ii. Item - Der Spieler benutzt ein Item.
Standardmäßig hat ein Spieler nur das Item Heiltrank. Beim Benutzen eines Heiltranks werden die Lebenspunkte eines Spielers um 50% seiner Gesamtlebenspunkte erhöht. Anschließend ist seine Runde beendet.
iii. Angriff - Der Spieler greift an.
Sollte ein Spieler angreifen wählen, wird zunächst mithilfe der Trefferwahrscheinlichkeit berechnet, ob er trifft. Wenn der Spieler mit seinem Angriff erfolgreich ist, werden die ATK-Punkte des Spielers von den Lebenspunkten des Monsters abgezogen. Abhängig von der errechneten Trefferwahrscheinlichkeit wird auf die ATK-Punkte ein Bonus/Malus berechnet. Hierfür soll eine sinnvolle Berechnung implementiert werden.

c. Die Monsterrunde läuft analog zur Spielerrunde. Für die jeweiligen Aktionen (Flucht, Angriff) sollen sinnvolle Wahrscheinlichkeiten implementiert werden.

### Aufgabe 4: Start und Ende

Bei Spielbeginn soll der Name Ihres Spiels (frei wählbar) und der Text „Zum Start Enter drücken“ angezeigt werden. Nach betätigen der Enter-Taste soll der rundenbasierte Kampf mit dem Monster starten. Nach dem Sieg oder der Niederlage des Spielers soll eine passende Ausgabe auf der Konsole erfolgen und der Spieler soll folgende Möglichkeiten bekommen:
- Spiel beenden – Beendet das Spiel und somit die Anwendung vollständig
- Neustart – Startet das Spiel von Beginn an neu
- Statistiken – Hier sollen die Statistiken des Kampfes, z.B. erlittener oder verursachter Schaden, angezeigt.

### Aufgabe 5: Schwierigkeitsgrad

Der Spieler soll die Möglichkeit bekommen bei Spielstart einen Schwierigkeitsgrad auszuwählen. Hier soll es die Wahl zwischen mindestens drei verschiedenen geben. Hierbei soll jeder Schwierigkeitsgrad sinnvolle (Regel-)Veränderung beinhalten.

### Aufgabe 6: Klassenwahl

Der Spieler kann bei Spielbeginn zwischen mehreren Klassen wählen. Diese Klassen sollen einzigartige Eigenschaften besitzen und ihren Fertigkeiten entsprechende Attribute zum Spielstart erhalten. Zusätzlich dazu soll eine vierte Option im Kampfverlauf zur Verfügung gestellt werden:
iv. Spezialangriff - Klassenspezifische Spezialangriffe können ausgewählt werden

Sollte ein Spieler Spezialangriff wählen soll er, je nach Klasse, die Auswahl zwischen verschiedenen Spezialfähigkeiten bekommen. Hierfür soll auch ein sinnvolles Ressourcensystem bedacht werden.

## Teil 2: Grafische Benutzeroberfläche mit Tkinter

### Aufgabe 7: GUI-Grundlagen

1. Erstelle eine neue Datei `dungeon_crawler_gui.py`.
2. Implementiere eine grundlegende GUI mit Tkinter, die das Dungeon anzeigt.
3. Füge Steuerungselemente (Buttons oder Tastatureingaben) für die Spielerbewegung hinzu.

### Aufgabe 8: Erweiterte GUI-Funktionen

1. Füge eine Minimap hinzu, die den erkundeten Teil des Dungeons anzeigt.
2. Implementiere ein Inventarfenster.
3. Erstelle ein Kampfinterface für Begegnungen mit Monstern.

### Aufgabe 9: Erweiterungen

1. Implementiere einen Speicher- und Lademechanismus für Spielstände.
2. Füge verschiedene Charakterklassen mit unterschiedlichen Fähigkeiten hinzu.
3. Erstelle ein Levelaufstiehsystem für den Spielercharakter.
4. Implementiere einen Dungeon-Generator, der prozedural verschiedene Dungeonlayouts erstellt.

Viel Spaß beim Programmieren deines Dungeon Crawlers!
