 # Codewiederholung

{{ youtube_video("https://www.youtube.com/embed/RVo03eT3U_A?si=I-5BEoTmDDKH1Nyc") }}

<div class="grid" markdown>
<div markdown>

Mit den `if`-Blöcken haben wir kennengelernt, wie man einen Codeblock nur unter bestimmten Bedingungen durchführt.

Wir wollen nun die `while`-Blöcke anschauen. Diese sind so ähnlich wie `if`-Blöcke, den auch sie prüfen eine
Bedingung und führen den eingerückten Code nur aus, wenn die Bedinung `True` ist. ABER: Bei `while` wird
nach jeder Durchführung des eingerückten Codes, ob die Bedingung immernoch erfüllt ist! Und wenn ja, dann
wird der eingerückte Codeblock NOCH MAL durchgeführt. Und das immerwieder!



```python
zahl = 1 # (1)!
while zahl < 100:  # (2)!
    print(zahl)  # (3)!
    zahl = zahl * 2  # (4)!
print(f'Finaler Wert: {zahl}.') # (5)!
```

1. Die Variable `zahl` wird mit dem Wert `#!python 1` angelegt.
2. Es wird geprüft, ob der Wert in `zahl` kleiner als `#!python 100` ist. Wenn ja, werden die nächsten beiden Zeilen ausgeführt. Wenn nein, so wird direkt zu Zeile 5 gesprungen.
3. Auf der Konsole wird der aktuelle Wert von `zahl` ausgegeben.
4. Der Wert von `zahl` wird verdopplt und dies in `zahl` gespeichert.
   **Achtung: Danach geht es in Zeile 2 weiter!**
5. Abschließend wird der finale Wert von `zahl` ausgegeben.

</div>
<div markdown>

``` mermaid
stateDiagram-v2
    classDef yourState font-style:italic,font-weight:bold,fill:white

    B:Bedingung überprüfen
    I:Code *im* eingerückten<br/>Block ausführen
    F:Code *nach* eingerücktem<br/>Block ausführen
    [*] --> B:::yourState
    B --> I : True
    I --> B : Springe zurück
    B --> F : False
```
</div>
</div>

{{ python_tutor("""zahl = 2
while zahl < 100:
    print(zahl)
    zahl = zahl * 2
print(f'Finaler Wert: {zahl}.')
""") }}


!!! bug "Endlosschleifen abbrechen"

    Sollten Sie in eine Endlosschleife geraten, können Sie ins Terminal klicken und die Ausführung mit ++ctrl++ + ++c++ abbrechen.


{{ task(file="tasks/while_lesen_1.yaml") }}

{{ task(file="tasks/while_lesen_2.yaml") }}

{{ task(file="tasks/dauernder_input.yaml") }}

{{ task(file="tasks/schleifen_und_if.yaml") }}

{{ task(file="tasks/immer_wechselnder_output.yaml") }}
