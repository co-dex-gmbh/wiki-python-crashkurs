# Palindrom Checker Lösung
```python
def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

user_input = input("Gib ein Wort ein, um zu überprüfen, ob es ein Palindrom ist: ").lower()

if is_palindrome(user_input):
    print(f"{user_input} ist ein Palindrom.")
else:
    print(f"{user_input} ist kein Palindrom.")
```


# Password Checker Lösung
```python

<pre><code>
def validate_password(password):
    # Überprüfung der Mindestlänge
    if len(password) < 8:
        return False

    has_alpha = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"

    for char in password:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        
        # Early Return, falls alle Bedingungen erfüllt
        if has_alpha and has_digit and has_special:
            return True

    # Check, ob alle Bedingungen erfüllt
    return has_alpha and has_digit and has_special

user_password = input("Gib dein Passwort zur Überprüfung ein: ")
if validate_password(user_password):
    print("Das Passwort ist stark.")
else:
    print("Das Passwort erfüllt nicht die Anforderungen für Stärke.")
```

# Password Generator Lösung 

```python
import random
import string

def generate_password(length):
    if length < 4:
        print("Für ein sicheres Passwort sollte die Länge mindestens 4 Zeichen betragen.")
        return ""

    # Zeichenkategorien
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()"

    # Sicherstellen, dass das Passwort mindestens je ein Zeichen aus jeder Kategorie enthält
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Füllen des Rests des Passworts mit zufälligen Zeichen aus allen Kategorien
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Mischen der Passwortzeichen für zusätzliche Sicherheit
    random.shuffle(password)
    
    # Konvertieren der Passwortliste in einen String
    return ''.join(password)

def main():
    try:
        length = int(input("Gib die gewünschte Passwortlänge ein: "))
        if length <= 0:
            print("Bitte gib eine positive ganze Zahl ein.")
        else:
            password = generate_password(length)
            if password:
                print(f"Dein neues Passwort: {password}")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    main()
```


# Viraler Wordle Klon Lösung

```python
import random

def get_guess():
    guess = input("Rate das Wort (5 Buchstaben): ").lower()
    while len(guess) != 5 or not guess.isalpha():
        print("Ungültige Eingabe. Bitte gib ein Wort mit 5 Buchstaben ein.")
        guess = input("Rate das Wort (5 Buchstaben): ").lower()
    return guess

def generate_feedback(secret_word, guess):
    feedback = []
    for i in range(5):
        # Buchstabe korrekt und an der richtigen Position
        if guess[i] == secret_word[i]:
            feedback.append('🟩')  
        elif guess[i] in secret_word:
            feedback.append('🟨')  # Buchstabe korrekt, aber an der falschen Position
        else:
            feedback.append('⬛')  # Buchstabe nicht im Wort enthalten
    return ''.join(feedback)

def wordle():
    word_list = ['apfel', 'birne', 'kerne', 'block', 'traum', 'schaf']
    secret_word = random.choice(word_list)
    attempts = 6

    print("Willkommen beim Wordle-Clone! Du hast 6 Versuche, das Wort zu erraten.")

    while attempts > 0:
        guess = get_guess()
        feedback = generate_feedback(secret_word, guess)
        attempts -= 1
        
        print(' '.join(list(guess)))
        print(feedback)
        print()
        
        if guess == secret_word:
            print(f"Du hast das Wort in {6 - attempts} Versuchen erraten!")
            break

        if attempts == 0:
            print(f"Leider verloren. Das Wort war: {secret_word}")
        else:
            print(f"Versuche übrig: {attempts}")

wordle()
```

