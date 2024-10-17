# Turtle libary

Eine Bibliothek ist ein Sammelbegriff für einen wieder verwendbaren Teil des Codes. Normalerweise enthält eine Python-Bibliothek eine Sammlung verwandter Module und Pakete. Tatsächlich wird dieser Begriff oft austauschbar mit "Python-Paket" verwendet, da Pakete auch Module und andere Pakete (Unterpakete) enthalten können. Es wird jedoch oft angenommen, dass ein Paket eine Sammlung von Modulen ist, während eine Bibliothek eine Sammlung von Paketen ist.

Um das Konzept der OOP zu üben, werden wir zunächst mit der Bibliothek "turtle" arbeiten.

Durch die Verwendung von `import turtle` können wir diese Bibliothek nutzen. Dann können Sie auf die Klasse `Turtle` zugreifen, die in dieser Bibliothek definiert wurde.

![[py36.png]]

Wir können ein Objekt dieser Klasse erstellen und es in einer Variablen speichern. Ich werde meine Schildkröte (Variable/Objekt) bob nennen:
```python
import turtle

bob = turtle.Turtle()
# If we use "print()" on our object, we will see where our object is stored inside the computer memory
print(bob)
  
# Output is:
# <turtle.Turtle object at 0x000001F0556B6080>
```

Jetzt können wir viele verschiedene und interessante Dinge mit diesem Objekt tun. Eine der anderen interessanten Klassen in der "turtle"-Bibliothek ist die "Screen"-Klasse. Sie ermöglicht es, unser Objekt in einem Fenster darzustellen:
```python
import turtle

bob = turtle.Turtle()
# Creat a "Screen" object:
my_screen = turtle.Screen()
# Use one of the Screen class attributes (this is the height of the screen, if you print it you will see 300 as default value)
my_screen.canvheight
# Let's use another attribute of the class Screen (we will see the screen until we press a key)
my_screen.exitonclick()
```

In der Mitte des Bildschirms siehst du die Schildkröte "bob".

![[py37.png]]

Aber die Form der Schildkröte ist eigentlich ein Pfeil, ändern wir es zu einer Schildkröte durch ein Attribut der Klasse Turtle:
```python
import turtle

bob = turtle.Turtle()
# Change the shape of "bob"
bob.shape("turtle")
# We can also change the color of bob
bob.color("green")
# Creat a "Screen" object:
my_screen = turtle.Screen()
# Let's use another attribute of the class Screen (we will see the screen until we press a key)
my_screen.exitonclick()
```

![[py38.png]]

Natürlich muss man nicht alle diese Klassen und Attribute auswendig kennen. Man kann all dies in der "Turtle graphics libary documentation" nachlesen.

## Exercises - turtle Modul

1. Create your own turtle and draw a rectangle with a height of 150 and width of 200.

Solution:
```python 
import turtle

bob = turtle.Turtle()
# Change the shape of "bob"
bob.shape("turtle")
bob.color("green")
# Move turtle forward
bob.forward(150)
# Turn him 90 degrees left direction
bob.left(90)
# Move turtle forward
bob.forward(200)
bob.left(90)
bob.forward(150)
bob.left(90)
bob.forward(200)

# Creat a "Screen" object:
my_screen = turtle.Screen()
# Let's use another attribute of the class Screen (we will see the screen until we press a key)
my_screen.exitonclick()
```


2. Draw the following house with your turtle!

![[py39.png]]

Solution:
```python
import turtle
bob = turtle.Turtle()
# Set window size
turtle.setup(500, 500)
# Change the shape of "bob"
bob.shape("turtle")
bob.color("green")
bob.fd(80)
bob.lt(90)
bob.fd(80)
bob.lt(30)
bob.fd(80)
bob.lt(120)
bob.fd(80)
bob.lt(120)
bob.fd(80)
bob.rt(90)
bob.fd(80)
bob.rt(90)
bob.fd(20)
bob.rt(90)
bob.fd(40)
bob.lt(90)
bob.fd(40)
bob.lt(90)
bob.fd(40)
bob.rt(90)
bob.fd(20)
bob.rt(90)
bob.fd(80)
# Creat a "Screen" object:
my_screen = turtle.Screen()
# Let's use another attribute of the class Screen (we will see the screen until we press a key)
my_screen.exitonclick()
```

# Prettytable

Eine weitere nützliche Bibliothek zum Üben von OOP ist die "prettytable"-Bibliothek. Mit ihr kann man schnell einfache Tabellen in der Konsole erstellen. Im Vergleich zur Bibliothek `turtle` muss man sie zuerst installieren, da sie nicht zum Standard gehört. Man kann sie innerhalb der Pycharm IDE installieren:
Gehen Sie zu File > Settings > Project: > Python Interpreter > drücken Sie das "+" Symbol > suchen Sie "prettytabble" > installieren

Wie jedes Mal, wenn man eine Bibliothek benutzen möchte, ist der beste Freund die Dokumentation über prettytable!

Beispiel:
```python
  # import this libary
import prettytable
# Create a object
my_table = prettytable.PrettyTable()
# Add data
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
# Display the table
print(my_table)
# Change properties
my_table.align = "l"
print(my_table)  
```

## Exercises - prettytable Modul

1. Create with "prettytable" a simple to-do list! The user can select a day and enter a to-do. Then he can select to continue for a new entry or exit the to-do list.

Solution:
```python
# Example using prettytable
import prettytable
# Inside this dictionary we will store the to-dos
to_dos = {
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
  }
to_do_on = True
while to_do_on:
    # Variable which will be filled by the user
    day = "place holder"
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # Loop until the user enter the valid day
    while True:
        if day.lower() in valid_days:
            break
        # Display all days which the user can select
        print("------------------------\nWelcome to your to-do list!\n------------------------")
        day = input(""
                    "\t1-Monday\n"
                    "\t2-Tuesday\n"
                    "\t3-Wednesday\n"
                    "\t4-Thursday\n"
                    "\t5-Friday\n"
                    "\t6-Saturday\n"
                    "\t7-Sunday\n"
                    "------------------------\n"
                    "Select a day: ")
    # Now we search inside the dictionary the selected day and enter a to-do
    to_do = input("Enter a to-do: ")
    to_dos[day].append(to_do)
    # Create an object of the class "PrettyTable"
    table = prettytable.PrettyTable()
    # Create the captions
    table.field_names = ["Day", "To-Do"]
    # Create all rows with the days
    table.add_rows(
        [
            ["Monday", to_dos["monday"]],
            ["Tuesday", to_dos["tuesday"]],
            ["Wednesday", to_dos["wednesday"]],
            ["Thursday", to_dos["thursday"]],
            ["Friday", to_dos["friday"]],
            ["Saturday", to_dos["saturday"]],
            ["Sunday", to_dos["sunday"]]
        ]
    )
    # Display the table
    print(table)
    # Ask the user if he likes to exit
    while True:
        valid_input = ["yes", "no"]
        exit_to_do = input("You like to exit the to-do list? (Yes/No): ")
        if exit_to_do in valid_input:
            if exit_to_do.lower() == "yes":
                # Set this variable to False for breaking the main while loop
                to_do_on = False
        break
```

2. The table shows the recorded values of a free fall experiment.

![[py40.png]]

Display the following table using prettytable and complete the empty cells.  
You need this formulas:

$$ 
Mittelwert=\frac{Messung1 + Messung2 + Messung3} {3}
$$

$$ 
Geschwindigkeit=9,81 \cdot Mittelwert
$$

Solution:
```python
# Import everything from this libary
from prettytable import *
# Create dictionary with data
data_table = {
    "Nr.": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Fallstrecke": [0, 0.115, 0.245, 0.285, 0.38, 0.49, 0.59, 0.67, 0.76, 0.835],
    "Messung 1": [0, 0.1568, 0.2072, 0.3404, 0.2811, 0.3173, 0.3488, 0.3705, 0.3937, 0.4183],
    "Messung 2": [0, 0.1561, 0.2075, 0.2427, 0.2846, 0.3172, 0.3477, 0.3703, 0.3941, 0.4176],
    "Messung 3": [0, 0.1566, 0.2578, 0.2403, 0.2814, 0.3172, 0.3483, 0.3693, 0.3946, 0.4116],
    "Mittelwert": [],
    "Geschwindigkeit": []
}

# Calculate the first value
for index in data_table["Nr."]:
    # Calculating the "Mittelwert"
        messung_1 = data_table["Messung 1"][index - 1]
        messung_2 = data_table["Messung 2"][index - 1]
        messung_3 = data_table["Messung 3"][index - 1]
        # Do not forget to round
        mittelwert = round((messung_1 + messung_2 + messung_3) / 3, 4)
        data_table["Mittelwert"].append(mittelwert)
    # Calculating the "Geschwindigkeit"
        geschwindigkeit = round(9.81 * mittelwert, 2)
        data_table["Geschwindigkeit"].append(geschwindigkeit)


# Create object
my_table = PrettyTable()
# Fill table with data
my_table.add_column("Nr.", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
my_table.add_column("Fallstrecke in m", data_table["Fallstrecke"])
my_table.add_column("Messung 1 in s", data_table["Messung 1"])
my_table.add_column("Messung 2 in s", data_table["Messung 2"])
my_table.add_column("Messung 3 in s", data_table["Messung 3"])
my_table.add_column("Mittelwert in s", data_table["Mittelwert"])
my_table.add_column("Geschwindigkeit in m/s", data_table["Geschwindigkeit"])
# Display table
print(my_table)

# Save this table as txt file! (You wil find the file inside the project directory)
# More about this later...
with open('file', 'w') as w:
    w.write(str(my_table))
```

# Math-Modul (Mathematische Funktionen)

Dieses Modul ermöglicht den Zugriff auf die im C-Standard definierten mathematischen Funktionen. Bei der Arbeit an finanziellen oder wissenschaftlichen Projekten ist es manchmal notwendig, mathematische Berechnungen in das Projekt zu integrieren. Python bietet das mathematische Modul, um solche Berechnungen durchzuführen. Durch die Verwendung dieses Moduls muss man Methoden, Attribute, Klassen und Objekte verwenden, perfekt um OOP zu üben. Nicht vergessen die Dokumentation zum Modul zu lesen!

Einige Beispiele zur Nutzung des `math` Modules:
```python
# Examples using the "math" modul
# ---------------------------------------- #
# import the modul
import math
# ---------------------------------------- #
# 1. Example
# You must all be familiar with pi. Pi is represented as either 22/7 or 3.14.
pi = math.pi
print(pi)
# You can use pi to calculate the area of a circle
# Define the radius of the circle
r = 5
circle_area = math.pi * r ** 2
print(circle_area)
# ---------------------------------------- #
# 2. Example
# Even the circle number tau is included (Ratios of circumference and radius)
circle_number = math.tau
print(circle_number)
# ---------------------------------------- #
# 3. Example
# Using infinity numbers in python
print(math.inf)
print(-math.inf)
# Divide a number by infinite number
print(1 / math.inf)
# ---------------------------------------- #
# 4. Example
# Faculty of a number
a = 5
print(math.factorial(a))
# ---------------------------------------- #
# 5. Example
# Power functions (German: Potenzfunktionen)
exponentiation_numbers = [0, 5, -2, math.pi]
print(math.exp((exponentiation_numbers[0])))
print(math.exp((exponentiation_numbers[1])))
print(math.exp((exponentiation_numbers[2])))
print(math.exp((exponentiation_numbers[3])))
# ---------------------------------------- #
# 6. Example
# Square root
print(math.sqrt(9))
# ---------------------------------------- #
# 7. Example
# Trigonometric functions
print(math.sin(math.pi / 2))
print(math.sin(90))
# ---------------------------------------- #
# 8. Example
# Convert degrees in radians
degree = 90
radians = math.pi
print(math.degrees(radians))
print(math.radians(degree))  
  
# Output is:
# 3.141592653589793
# 78.53981633974483
# 6.283185307179586
# inf
# -inf
# 0.0
# 120
# 1.0
# 148.4131591025766
# 0.1353352832366127
# 23.140692632779267
# 3.0
# 1.0
# 0.8939966636005579
# 180.0
# 1.5707963267948966
```

## Exercises - math Modul

1. Write a program that calculates the hypotenuse of a right triangle.  Divide the program into input, processing and output:
	- In the input part, read the length of the two cathets
	- Use the function math.sqrt() for the calculation
	- Output the result to the screen

Solution:
```python
# import the modul
import math
# -------------------------------------------------- #
# Function
def calc_hypetenuse(cathet_1, cathet_2):
    hypotenuse = math.sqrt((cathet_1 ** 2) + (cathet_2 ** 2))
    return hypotenuse
# -------------------------------------------------- #
# Main program
# Input part
try:
    cathete_1 = float(input("Input the first cathet: "))
    cathete_2 = float(input("Input the second cathet: "))
except:
    print("Wrong input!")
# Processing part
hypotenuse = round(calc_hypetenuse(cathete_1, cathete_2), 2)
# Output part
print(f"The hypotenuse is: {hypotenuse}")
```

2. Write a program to plot functions with the "turtle" libary and the "math" module. Draw a parable and a linear function!

Solution:
```python
# Import modules
import turtle
import prettytable
# -------------------------------------------------- #
# Create a window
turtle.getscreen()
# Create a object from the "Turtle()" class
t = turtle.Turtle()
# Variable to "zoom" later
scale = 10
# -------------------------------------------------- #
# Generate a table for x square with x = -20 to +20
my_table = prettytable.PrettyTable()
my_table.field_names = ["x", "x^2"]
for x in range(-20, 21, 1):
    x_square = x ** 2
    my_table.add_row([x, x_square])
print(my_table)
# -------------------------------------------------- #
# Draw the axes
# penup() will lift the turtle off the “digital canvas” and if you move the turtle in penup state it won’t draw.
t.penup()
# Move turtle to an absolute position
t.goto(-400, 0)
# Put the turtle back in the "canvas" to draw
t.pendown()
# Lets draw
t.goto(400, 0)
t.penup()
t.goto(0, -400)
t.pendown()
t.goto(0, 400)
t.penup()
t.home()
# -------------------------------------------------- #
# Prepare the turtle
t.pensize(2)
# Location of the first coordinates (-20;400)
# You can try without the scale variable
t.goto(-20 * scale, 400)
# -------------------------------------------------- #
# Draw the curve
for x in range(-20, 21, 1):
    x_square = x ** 2
    t.dot(10, "RED")
    # You can try without the scale variable
    t.goto(x * scale, x_square)
# -------------------------------------------------- #
# Bring the turtle back
t.penup()
t.home()
# -------------------------------------------------- #
# Lets draw f(x) = 2*x
t.penup()
t.goto(-20 * scale, -40)
t.pendown()
t.pencolor("GREEN")
for x in range(-20, 21, 1):
    x_2 = x * 2
    t.goto(x * scale, x_2)
# -------------------------------------------------- #
# Bring the turtle back
t.penup()
t.home()
# -------------------------------------------------- #
turtle.exitonclick()
```

3. Draw the sinus function by using the tuertle and math moduls.

Solution:
```python
# Import modules
import math
import turtle
import prettytable
# -------------------------------------------------- #
# Create a window
turtle.getscreen()
# Create an object from the "Turtle()" class
t = turtle.Turtle()
# Variable to "zoom" later
scale = 100
# -------------------------------------------------- #
# Draw the axis
t.backward(180)
t.forward(360)
t.stamp()
t.backward(180)
t.left(90)
t.forward(100)
t.stamp()
t.backward(200)
t.forward(100)
t.right(90)
t.backward(180)
# Draw the curve
for i in range(-180, 181):
    t.color("RED")
    t.goto(i, math.sin(math.radians(i)) * scale)

turtle.exitonclick()
```