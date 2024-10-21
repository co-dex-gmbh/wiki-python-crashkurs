# Projekt: Tic Tac Toe

{{ youtube_video("https://www.youtube.com/embed/LORQ6tDpgZw?si=Ox8mtY-wzE8A879E") }}

In diesem Abschnitt werden wir unser bisheriges Können in einem kleinen Projekt zusammenstellen. Wir wollen das Spiel
`TicTacToe` implementieren.

**(Vereinfachte) Spielregeln:**

* Es wird ein quadratisches Spielfeld aus 3x3 (also 9) Feldern gezeichnet.
* Der Erste Spieler trägt ein `x` in eines der Felder ein.
* Danach trägt der zweite Spiler ein `o` in eines der Felder ein.
* Dies wird abwechselnd so lange durchführt, bis ein drei in einer Zeile, Spalte oder Diagonalen dreimal das gleiche Symbol auftaucht. Der Spieler, der dieses Symbol zeichnet, gewinnt.

Das ganze soll nachher so aussehen:

```
 0 | 1 | 2 
 3 | 4 | 5
 6 | 7 | 8
Spieler x, wo willst du setzen? 0
 x | 1 | 2 
 3 | 4 | 5
 6 | 7 | 8
Spieler o, wo willst du setzen? 1
 x | o | 2 
 3 | 4 | 5
 6 | 7 | 8
Spieler x, wo willst du setzen? 4
 x | o | 2 
 3 | x | 5
 6 | 7 | 8
Spieler o, wo willst du setzen? 2
 x | o | o 
 3 | x | 5
 6 | 7 | 8
Spieler x, wo willst du setzen? 8
 x | o | o 
 3 | x | 5
 6 | 7 | x
Herzlichen Glückwunsch!

```

Wir haben bereits etwas Code vorgegeben. Dieser hat einige Lücken, die wir füllen müssen.

```python hl_lines="15 22 25 28"
def gameloop(): # (1)!
    spielbrett = [0, 1, 2, 3, 4, 5, 6, 7, 8] # (14)!

    aktiver_spieler = 'x' # (2)!
    nächster_spieler = 'o' # (3)!

    while not es_gibt_gewinner(spielbrett): # (4)!
        print(als_quadrat(spielbrett)) # (5)!

        position = int(input(f"Spieler {aktiver_spieler}, wo willst du setzen? ")) # (6)!

        symbol_schreiben(spielbrett, position, aktiver_spieler) # (7)!

        # Wechsle Spieler
        ... # (8)!

    print(als_quadrat(spielbrett)) # (9)!
    print(f"Herzlichen Glückwunsch!") 


def als_quadrat(spielbrett): # (10)!
    return ...

def es_gibt_gewinner(spielbrett): # (11)!
    return ...

def symbol_schreiben(spielbrett, position, symbol): # (12)!
    ...

if __name__ == '__main__': # (13)!
    gameloop()
```

1. In der Funktion `gameloop` wird das gesamte Spiel durchgeführt.
2. In `aktiver_spieler` ist das Symbol des momentan aktiven Spielers gespeichert.
3. In `nächster_spieler` ist das Symbol gespeichert, dass der nächste Spieler nutzt.
4. In der Funktion `es_gibt_gewinner()` soll geprüft werden, ob es schon einen Gewinner gibt. Wenn nein, so durchlaufen wir den Schleifenrumpf.
5. Zunächst geben wir das Spielfeld als schönes Quadrat (mithilfe der Methode `als_quadrat`) auf der Konsole aus. An den Zahlen erkennt der Spieler, welche Felder noch frei sind und was er in der Konsole eingeben muss, um in das richtige Feld zu setzen.
6. Der Nutzer erhält die Aufforderung eine Zahl einzugeben, in welches das aktuelle Spielersymbol eingetragen wird. 
7. Auf dem Spielbrett wird nun an der vom Spieler gewünschten Position das Zeichen gesetzt.
8. Hier müssen `aktiver_spieler` und `nächster_spieler` wechseln.
9. Wenn ein Gewinner gefunden wurde, wird die Schleife nicht länger durchlaufen und eine Gratulation wird angezeigt.
10. Diese Funktion baut aus der Liste `[0, 1, ..., 8]` einen String mit Zeilenumbrüchen.
11. Diese Funktion untersucht, ob es bereits einen Gewinner beim Tic Tac Toe spiel gibt. 
12. Diese Funktion ermöglicht ein in einer Liste (dem `spielbrett`) ein vorgegebenen `symbol` an einer bestimmten `position` zu setzen.
13. Diese beiden Codezeilen sorgen dafür, dass bei Ausführung der Datei das Programm gestartet wird.
14. Das Spielbrett ist aus sicht des Computers eine Liste mit neun Elementen. Mithilfe der Methode `als_quadrat`, werden wir dieses Spielbrett später auf der Konsole als ein schönes Quadrat ausgeben. Um das Spielfeld beim Programmieren einfacher zu handhaben, ist es hier aber gut, es als eine einfache Liste zu speichern.

Wir müssen in diesem Code vier Dinge ergänzen:

{{ task(file="tasks/tictactoe_als_quadrat.yaml", collapsed=True) }}

{{ task(file="tasks/tictactoe_es_gibt_gewinner.yaml", collapsed=True) }}

{{ task(file="tasks/tictactoe_symbol_schreiben.yaml", collapsed=True) }}

{{ task(file="tasks/tictactoe_spielerwechsel.yaml", collapsed=True) }}

Wenn wir alles richtig gemacht haben, kann so unsere Lösung aussehen:

??? tip "Komplette Lösung"

    ``` python hl_lines="18-20 27 31-38 42"
    --8<-- "goals/tictactoe.py"
    ```

{{ youtube_video("https://www.youtube.com/embed/hYzRuiJe2yU?si=sea2B_bU1wx9yMz9") }}
