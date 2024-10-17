# Bedingungen verknüpfen

{{ youtube_video("https://www.youtube.com/embed/RwszZ3Ca25M?si=ojrftjdkgRoLkHST") }}

Wir können mehrere Bedingungen auch miteinander verknüpfen.

| Operator | Beschreibung                                                   | Beispiel           |
|----------|----------------------------------------------------------------|--------------------|
| `and`    | Gibt `True` zurück, wenn **alle** Parameter `True` sind.       | `x < 5 and y > 10` |
| `or`     | Gibt `True` zurück, wenn **eines** der Parameter `True` ist.   | `x < 5 or y > 10`  |
| `not`    | Invertiert die Eingabe. Aus `True` wird `False` und umbekehrt. | `not x >= 6`       |

{{ task(file="tasks/bedingungen_voraussagen_3.yaml") }}

{{ task(file="tasks/bedingungen_voraussagen_4.yaml") }}

{{ task(file="tasks/bedingungen_programmieren.yaml") }}
