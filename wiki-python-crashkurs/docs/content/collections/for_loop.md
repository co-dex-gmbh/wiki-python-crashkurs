# for-Schleife

Häufig wollen wir bestimmte Operationen auf allen Elementen einer Liste durchführen.
Dies kann zwar über eine `while`-Schleife implementiert werden, ist aber etwas 
umständlich und sogar fehleranfällig. Lieber wird mit der `for`-Schleife gearbeitet,
die erlaubt alle Elemente einer Liste nacheinander durchzugehen, ohne dass dabei
der Index zum Zugriff auf die Elemente genutzt werden muss. 

=== "for-loop"

    ```python
    produkte = ["Butter", "Milch", "Wurst"] # (1)!
    
    for produkt in produkte: # (2)!
        print(f"Heute gibt es {produkt}.") # (3)!
    ```

    1. Lege eine Liste mit Elementen an, die durchlaufen werden sollen.
    2. Hier wird eine Variable `produkt` angelegt und diese wird nun nacheinander mit allen Elementen der Liste `produkte` befüllt. Zuerst gilt also `produkt = "Butter"` und mit diesem Wert werden die nächsten eingerückten Zeilen durgeführt. Danach ist `produkt = "Milch"` und die eingerückten Zeilen werden erneut durchgeführt. Dies geht so lange weiter, bis alle Elemente in der Liste durchlaufen wurden. 
    3. Der eingerückte Code ist der Schleifenrumpf. Dieser wird so oft durchlaufen, wie es Elemente in der Liste gibt.

=== "while-loop"

    So würde die Implementierung mit einer `while`-Schleife aussehen.
    
    ```{ .python .pytutor_button }
    produkte = ["Butter", "Milch", "Wurst"] # (1)!
    i = 0 # (2)!
    
    while i < len(produkte): # (3)!
        print(f"Heute gibt es {produkte[i]}.") # (4)!
        i = i + 1 # (5)!
    ```

    1. Lege eine Liste mit Elementen an, die durchlaufen werden sollen.
    2. Es wird eine Variable `i` angelegt, die für den Zugriff auf die Liste über den Index benötigt wird.
    3. Solange `i` nicht größer ist, als der größtmögliche Index, soll die Schleife durchlaufen werden. `len(prodcukte)` gibt die Anzahl der Elemente in der Liste zurück und ist hier `3`.
    4. Um nun auf die Elemente zuzugreifen, wird die Index-Notation `produkte[i]` verwendet.
    5. Abschließend muss der `i` vergrößert werden, um sicher zu stellen, dass im nächsten Schleifendurchlauf auch auf das nächste Element zugegriffen wird.

Konsolenausgabe:

```
Heute gibt es Butter
Heute gibt es Milch
Heute gibt es Wurst
```

{{ python_tutor("""produkte = ['Butter', 'Milch', 'Wurst']
    
for produkt in produkte:
    print(f'Heute gibt es {produkt}.') # (3)!
""") }}

{{ task("tasks/for_loop_lesen_0.yaml") }}

{{ task("tasks/for_loop_lesen_1.yaml") }}

{{ task("tasks/for_loop_schreiben_0.yaml") }}

{{ task("tasks/for_loop_schreiben_1.yaml") }}

{{ task("tasks/for_loop_schreiben_2.yaml") }}
