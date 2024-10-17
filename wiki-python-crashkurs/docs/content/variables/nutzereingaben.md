# Nutzereingaben

{{ youtube_video("https://www.youtube.com/embed/sAAbtiyc4-U?si=Wcf7GJ6JhsEelF8E") }}

Mit der `#!python print` Funktion können wir auf der Konsole eine Ausgabe erzeugen.

Andererseits kann mit der Funktion `#!python input` eine Eingabe des Nutzers auf der Konsole erwartet werden.
Wenn die Funktion aufgerufen wird, wartet der Code so lange, bis eine Nutzereingabe getätigt und mit ++enter++ bestätigt wurde.
Die Eingabe des Nutzers wird dann in einer Variablen gespeichert.

```{ .python .pytutor_button }
print('Sei gegrüßt!')
vorname = input('Wie heißt du?') # (1)!
print('Hallo') 
print(vorname) # (2)!
```

1. Wenn `input` aufgerufen wird, sehen wir auf der Kommandozeile den Prompt `Wie heißt du`. Das Programm wartet jetzt auf unsere Eingabe. Unsere Eingabe wird dann in der Variablen `vorname` gespeichert.
2. Hier wird die Eingabe wieder auf der Console ausgegeben.

{{ task(file="tasks/input_einfügen.yaml") }}

{{ youtube_video("https://www.youtube.com/embed/GEC7aN5ndU0?si=tkZqv7t2u2tZLpnW", title="Vorsicht beim Einlesen von Zahlen") }}
    
Immer, wenn man Zahlen vom Nutzer einlesen will und mit diesem im Code **rechnen** möchte, so muss
man Python ganz explizit sagen, dass hier eine Zahl folgt. Verwenden sie daher folgenden Code:

Bei Ganzzahlen nutze `#!python int(input(...))`:

```python
alter = int(input('Wie alt bist du?'))
print('In einem Jahr bist du:')
print(alter + 1)
```

Bei Fließkommazahlen nutze `#!python float(input(...))`:

```python
preis = float(input('wie viel kostet das Produkt?))
print('Die Mehrwehrsteuer des Produktes beträgt:')
print(preis * 0.18)
```

!!! note Vergleich zu R

    In R gibt es die Funktion `readline`, um Nutzereingaben zu lesen.

    ```r
    # R
    alter <- as.integer(readline('Wie alt bist du?'))
    print(paste('In einem Jahr bist du:', alter + 1))
    ```


{{ task(file="tasks/marsgewicht_mit_input.yaml") }}

{{ task(file="tasks/bmi.yaml") }}
