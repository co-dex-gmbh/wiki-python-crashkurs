# Class- & Static Methods

In Python gibt es zwei besondere Arten von Methoden, die direkt einer Klasse zugeordnet sind:
**statische Methoden** und **Klassenmethoden**. Diese Methoden haben spezielle Verwendungszwecke 
und werden mit den Dekoratoren `@staticmethod` und `@classmethod` definiert.

## Statische Methoden

Eine **statische Methode** ist eine Methode, die zu einer Klasse gehört, 
aber nicht auf eine Instanz zugreift. Sie wird mit dem Dekorator `@staticmethod` definiert 
und hat keinen Zugriff auf Instanzattribute. Statische Methoden sind in erster Linie nützlich,
wenn eine Methode nur auf Klassenebene operieren muss und keine Instanzinformationen benötigt.

Besonders gerne nutzt man statische Methoden für UtilityKlassen, wie zum Beispiel die folgende, die 
Fahrenheit in Celsius umrechnet und umgekehrt:

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20TemperatureConverter%3A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20celsius_to_fahrenheit%28celsius%29%3A%0A%20%20%20%20%20%20%20%20return%20celsius%20*%209/5%20%2B%2032%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20fahrenheit_to_celsius%28fahrenheit%29%3A%0A%20%20%20%20%20%20%20%20return%20%28fahrenheit%20-%2032%29%20*%205/9%0A%0A%23%20Die%20statischen%20Methoden%20k%C3%B6nnen%20direkt%20von%20der%20Klasse%20aufgerufen%20werden%0Acelsius_temp%20%3D%2025%0Afahrenheit_equivalent%20%3D%20TemperatureConverter.celsius_to_fahrenheit%28celsius_temp%29%0Aprint%28f%22%7Bcelsius_temp%7D%20Grad%20Celsius%20entsprechen%20%7Bfahrenheit_equivalent%3A.2f%7D%20Grad%20Fahrenheit.%22%29%0A%0Afahrenheit_temp%20%3D%2077%0Acelsius_equivalent%20%3D%20TemperatureConverter.fahrenheit_to_celsius%28fahrenheit_temp%29%0Aprint%28f%22%7Bfahrenheit_temp%7D%20Grad%20Fahrenheit%20entsprechen%20%7Bcelsius_equivalent%3A.2f%7D%20Grad%20Celsius.%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Die statischen Methoden können direkt von der Klasse aufgerufen werden
celsius_temp = 25
fahrenheit_equivalent = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_equivalent:.2f} Grad Fahrenheit.")

fahrenheit_temp = 77
celsius_equivalent = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Grad Fahrenheit entsprechen {celsius_equivalent:.2f} Grad Celsius.")
```

{{ task(file="tasks/oop_static_methods_1.yaml") }}

## Klassenmethoden

{{ youtube_video("https://www.youtube.com/embed/fA8xpIm6sjM?si=txTrtUUPEPdCpG-K")}}

Eine **Klassenmethode** ist eine Methode, die auf die Klasse selbst zugreift und nicht auf Instanzattribute.
Sie wird mit dem Dekorator `@classmethod` definiert und erhält die Klasse selbst als ersten Parameter (`cls`).

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Car%3A%0A%20%20%20%20total_cars%20%3D%200%0A%0A%20%20%20%20def%20__init__%28self,%20brand%29%3A%0A%20%20%20%20%20%20%20%20self.brand%20%3D%20brand%0A%20%20%20%20%20%20%20%20Car.total_cars%20%2B%3D%201%0A%0A%20%20%20%20%40classmethod%0A%20%20%20%20def%20get_total_cars%28cls%29%3A%0A%20%20%20%20%20%20%20%20return%20cls.total_cars%0A%0Atotal%20%3D%20Car.get_total_cars%28%29%0Aprint%28total%29%0A%0Acar1%20%3D%20Car%28%22Volkswagen%22%29%0Acar2%20%3D%20Car%28%22Toyota%22%29%0A%0Atotal_now%20%3D%20Car.get_total_cars%28%29%0Aprint%28total_now%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

total = Car.get_total_cars()
print(total)

car1 = Car("Volkswagen")
car2 = Car("Toyota")

total_now = Car.get_total_cars()
print(total_now)
```


Klassenmethoden werden oft für alternative Konstruktoren oder zur Manipulation der Klasse selbst verwendet.

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Date%3A%0A%20%20%20%20def%20__init__%28self,%20year,%20month,%20day%29%3A%0A%20%20%20%20%20%20%20%20self.year%20%3D%20year%0A%20%20%20%20%20%20%20%20self.month%20%3D%20month%0A%20%20%20%20%20%20%20%20self.day%20%3D%20day%0A%0A%20%20%20%20%40classmethod%0A%20%20%20%20def%20from_string%28cls,%20string%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20Erstellt%20ein%20String%20der%20Form%20'YYYY-MM-DD'%20ein%20Date.%0A%0A%20%20%20%20%20%20%20%20%3E%3E%3E%20print%28Date.from_string%28%221990-07-10%22%29%29%0A%20%20%20%20%20%20%20%2010.07.1990%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20year,%20month,%20day%20%3D%20string.split%28%22-%22%29%0A%20%20%20%20%20%20%20%20return%20cls%28year,%20month,%20day%29%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.day%7D.%7Bself.month%7D.%7Bself.year%7D%22%0A%20%20%20%20%0Aprint%28Date.from_string%28%221990-07-10%22%29%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, string):
        """
        Erstellt ein String der Form 'YYYY-MM-DD' ein Date.

        >>> print(Date.from_string("1990-07-10"))
        10.07.1990
        """
        year, month, day = string.split("-")
        return cls(year, month, day)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
print(Date.from_string("1990-07-10"))
```


```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, string):
        """
        Erstellt ein String der Form 'YYYY-MM-DD' ein Date.
        
        >>> print(Date.from_string("1990-07-10"))
        10.07.1990
        """
        year, month, day = string.split("-")
        return cls(year, month, day)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
```

