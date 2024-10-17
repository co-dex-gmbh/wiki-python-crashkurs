# Listen erweitern

{{ youtube_video("https://www.youtube.com/embed/zcEfu5HKYU0?si=9lsBZtFTCj5xSxu6") }}

Zu einer Liste können neue Elemente mit der Methode `append` hinzugefügt werden. Das sieht dann wie folgt aus:

```.python
fragezeichen = ['Justus'] # (1)!
fragezeichen.append('Peter') # (2)!
fragezeichen.append('Bob')
print(fragezeichen)
```

1. Liste wird erstellt.
2. Neues Element wird mit `append` hinzugefügt.

{{ python_tutor("""fragezeichen = ['Justus']
fragezeichen.append('Peter')
fragezeichen.append('Bob')
print(fragezeichen)
""") }}

{{ task(file="tasks/listen_lesen_1.yaml") }}

{{ task(file="tasks/dauernder_input_listen.yaml") }}

{{ task(file="tasks/listen_input_manipulieren.yaml") }}
