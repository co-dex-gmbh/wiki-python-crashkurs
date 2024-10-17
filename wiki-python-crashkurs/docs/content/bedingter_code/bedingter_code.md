# Bedingter Code

{{ youtube_video("https://www.youtube.com/embed/EZMzMmsG-tI?si=rZnfu1cHfYWT7ONx") }}

Mit dem `if` Keyword und Einrückungen kann man festlegen, dass Code nur unter bestimmten Bedingungen ausgeführt wird.

``` { .python }
name = input("Wie ist dein Name?") # (1)!
if 'q' in name: # (2)!
    print("Wow, das ist ja ein seltener Name!") # (3)!
print(f"Auf jeden Fall ist dein Name {name}") # (4)!
```

1.  Der Nutzer wird nach seinem Namen gefragt. Die Eingabe wird in der Variable `#!python name` gespeichert.
2.  Es wird geprüft, ob der Buchstabe `#!python 'q'` in `#!python name` auftaucht.
3.  Wenn `#!python 'q'` in `#!python name` auftaucht, wird der **eingerückte** Code ausgeführt. Hier können auch noch mehr Zeilen eingerückter Code stehen, die nur ausgeführt werden, wenn die Bedingung erfüllt ist.
4.  Diese Zeile ist nicht eingerückt und wird daher auf jeden Fall wieder ausgeführt.

{{ python_tutor_button("""name = input('Wie ist dein Name?')
if 'q' in name:
    print('Wow, das ist ja ein seltener Name!')
print(f'Auf jeden Fall ist dein Name {name}')
""")}}

Wenn die Bedingung, die neben dem `if` steht, wahr ist, dann werden die nächsten Zeilen Code, die eingerückt sind ausgeführt.
Wenn die Bedingung aber falsch ist, werden die eingerückten Zeilen einfach übersprungen.

{{ task(file="tasks/if_einfügen.yaml") }}
