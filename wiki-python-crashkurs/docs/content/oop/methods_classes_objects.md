Am Beispiel des Stifts werden wir lernen, wie man Klassen, Objekte und Methoden erstellt.

```python
# Define a class with the "class" keyword
class Pen:
    # Let's create some attributes which the pen will have (We are using "None" to assign "no value"
    outside_color = None
    writing_color = None

    # Create some methods (what can the pen do?). The definition is the same as functions.
    # Methods have always minimum one parameter, the object itself "keyword self"
    def write(self):
        print("I am writing!")

    def refill(self):
        print("I refill the pen!")

    # Inside the f-string we have to use the "self" keyword to call the object "itself"
    def about_pen(self):
        print(f"My outside color is {self.outside_color} and my writing color is {self.writing_color}! ")


# Let's use our class inside the main program

# Firstly we create two objects of the class "pen", this process is called "create instance of class"
my_pen = pen()
workers_pen = pen()
# Let's set the values of the attributes with the "dot notation"
my_pen.outside_color = "red"
my_pen.writing_color = "blue"
workers_pen.outside_color = "yellow"
workers_pen.writing_color = "black"
# Let's do something with the pens by using the methods
my_pen.write()
workers_pen.refill()
# Display the information about the pen with the "about_pen" method
my_pen.about_pen()
workers_pen.about_pen()

# Output is:
# I am writing!
# I refill the pen!
# My outside color is red and my writing color is blue! 
# My outside color is yellow and my writing color is black!  
```

Folgendes sollte beachtet werden:
- Eine Klasse ist im Allgemeinen eine Gruppe von Dingen, Lebewesen oder Konzepten, die gemeinsame Merkmale oder Eigenschaften haben.
- In der OOP spezifiziert eine Klasse eine Reihe von Objekten mit denselben Attributen und Methoden.
- Die Klasse verfügt über einen Mechanismus zum Erstellen von Objekten. Sie ist lediglich die Konstruktionsvorlage für alle neu benötigten Objekte, während die Objekte im Programmsystem "leben" und angesprochen werden können.
- Zwischen verschiedenen Klassen oder ihren Objekten können verschiedene Beziehungen hergestellt werden, um Beziehungen wie in der Realität darzustellen.

Wenn Sie sich erinnern, hatten wir bereits Methoden auf Objekte angewendet. Damals wussten wir allerdings noch nicht, was genau eine Methode oder ein Objekt ist. Wir hatten die Methode `append()` mit der Punktschreibweise für die Datenstruktur "list" verwendet. Diese Methode ermöglichte es uns, einen Eintrag am Ende der Liste hinzuzufügen.

Beispiel:
```python
# Create a list
my_list = ["Red", "Blue", "Yellow"]
# Display the list
print(my_list)
# Add a entry at the end of this list
my_list.append("Black")
# Display the list
print(my_list)
  
# Output is:
# ['Red', 'Blue', 'Yellow']
# ['Red', 'Blue', 'Yellow', 'Black']
```


Exercise:

Write a class called "Cat". The class has three attributes: "name", " race" and "age". The "age" of a new "cat" object should be "0" at the beginning of its lifetime.  
Write three methods:
- The first one is called "doMiau()". When the method is executed, the text "meow" is output.
- The second method you call "riseAge()". This method increases the value of the "age" attribute by 1.
- The third method is called "displayDetails()", it displays name, race and age meaningfully as text.

Solution:
```python
  
# Create the class
class Cat:
    # Attributes
    name = None
    race = None
    age = 0

    # Methods
    def doMiau(self):
        print("meow")

    def riseAge(self):
        self.age += 1

    def displayDetails(self):
        print(f"The name of the cat is {self.name}, the cat is {self.age} years old and the race is an {self.race}!")


# Main program
my_cat = Cat()
# Show me the age of my cate
print(f"My cat is {my_cat.age} years old")
# Lets rise the age of my cate
my_cat.riseAge()
# My cat get a name
my_cat.name = "Thanos"
# Define the race of the cat
my_cat.race = "American Shorthair"
# Show me all details about my cat
my_cat.displayDetails()
  
# Output is:
# My cat is 0 years old
# The name of the cat is Thanos, the cat is 1 years old and the race is an American Shorthair!
```



