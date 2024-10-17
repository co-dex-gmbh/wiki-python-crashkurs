# Unit Tests

Code ist ein lebendiges Produkt. Das heißt, einmal geschrieben, bleibt eine Codebasis nie so wie sie ist. 
Fehler müssen korrigiert oder neue Features hinzugefügt werden, die Anwendungsfreundlichkeit soll gesteigert werden
oder die Laufzeit durch klügere Algorithmen verbessert werden. Es gibt viele Gründe, warum sich Code des selben
Programms im Laufe der Zeit ändert, aber wie stellt man sicher, dass bei Änderungen (groß oder klein) *alles*
weiterhin funktioniert?

Eine Antwort auf diese Frage sind **Unittests**. Diese werden von den Programmierern parallel (oder vor) dem 
eigentlich Code geschrieben und werden Zukünftig immer ausgeführt, wenn es eine Änderung im Code gibt.
Diese Unittests überprüfen dann nämlich, ob die einzelnen Bausteine meines Codes (die "Units"/Einheiten) immernoch
funktionieren, oder ob irgendetwas durch die Änderungen gestört wurde.

In einer Metapher gesprochen. Ein Restaurantbesitzer möchte die Küche renovieren. Er lässt von den Köchen
eine lange Liste von *Tests* erstellen. Z.B. Es gibt Kochlöffel; die Herdplatte platte wird heiß, wenn man 
daran dreht; der Eisschrank kann eine Temperatur von -17 °C halten usw. Alle diese Tests funktionieren bisher
und das müssen sie auch, wenn die neue Küche eingebaut ist. In der neuen Küche kommen noch neue Geräte hinzu
und auch für diese würde man weitere Tests der Liste hinzufügen, um alles für die Zukunft zu sichern.

{{ youtube_video("https://www.youtube.com/embed/yvNdCqKufbc?si=5FZ8aZ5gM87fWwcQ") }}

Betrachten wird das folgende Beispiel, in dem die Korrektheit der `quadrat` Funktion getestet wird.
Wir sehen hier vier Tests, die prüfen, ob 

* `quadrat(5) == 25`,
* `quadrat(0) == 0`,
* `quadrat(1) == 1` und
* `quadrat(-5) == 25` gelten.

``` { .python hl_lines="9 12 15 18" }
import unittest # (1)!

def quadrat(zahl): # (2)!
    return zahl * zahl


class TestQuadrat(unittest.TestCase): # (3)!
    def test_quadrat_0(self): # (4)!
        self.assertEqual(quadrat(5), 25) # (5)!
        
    def test_quadrat_1(self): # (6)!
        self.assertEqual(quadrat(0), 0)
        
    def test_quadrat_2(self):
        self.assertEqual(quadrat(1), 1)
        
    def test_quadrat_3(self):
        self.assertEqual(quadrat(-5), 25)

if __name__ == '__main__': # (7)!
    unittest.main()
```

1. Wir importieren hier das Modul `unittest`. Das ist ein Ordner mit Pythoncode, den wir nun verwenden können. In diesem sind die Unittests implementiert und wir können diese jetzt in unserem Code definieren und ausführen.
2. Hier wird die Funktion definiert, die wir testen wollen.
3. Hier wird eine Klasse namens `TestQuadrat` definiert, welche von `unittest.TestCase` erbt. Kurz gesagt bedeutet dass, dass wir im nun folgenden eingerückten Code Methoden definieren können, die unsere Unittests sind.
4. Hier wird ein Unittest definiert. Das sieht so ähnlich aus, wie das Definieren einer Funktion. In die runden Klammern gehört immer der Parameter `self`, über den wir die Art des Tests festlegen werden.<br/>Die genaue Bedeutung von `self` wird erst bei der objektorientierten Programmierung wichtig und kann jetzt erstmal von uns hingenommen werden.
5. Mit `self.assertEqual( ... , ... )` wird gesagt, dass wir im Test sicherstellen (_assert_), dass zwei Werte gleich sind. Hier wollen wir wir sicherstellen, dass das Ergebnis von `quadrat(5)` gleich `25` ist. 
6. Wir definieren hier noch weitere Tests. Wichtig ist, dass deren Namen mit `test_` beginnen.
7. In diesen zwei Zeilen sorgen wir dafür, dass die Tests beim Ausführen der Datei gefunden und ausgeführt werden. Mehr müssen wir hier zu diesem Zeitpunkt nicht verstehen.

Wenn wir dieses Programm ausführen erhalten wir die folgende Konsolenausgabe, die uns zeigt, 
dass alle Tests erfolgreich waren:

```
Ran 4 tests in 0.012s

OK

Process finished with exit code 0
```

{{ task(file="tasks/tests_fehlschlagen.yaml") }}

{{ task(file="tasks/tests_lesen_0.yaml") }}

{{ task(file="tasks/tests_funktion_für_listen_entwickeln.yaml") }}
