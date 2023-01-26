'''
    Name: Juan Pablo Meza
    Email: Juanpablo.meza604@gmail.com
    
    
    This program goes over the basic functions of Python such as: simple I/O, Selection Control, Loops, .random, functions, list/arrays, file I/O, creating graphs,
    classes and objects, inheritance, GUI and UML Diagram.
    1. This program creates of consisting a class with private attributes and to pass them onto a subclasses.
    2. The second part of the program consists of making an array/list and loops to create 15 objects.
    3. The third part of the program consists of the loop previously made to display the class and it's attributes.
    
'''

import random
from Shapes import *
import matplotlib.pyplot as plt
import numpy as np


circles = []
square = []
cube = []

for i in range(15):
    run = random.randint(1,3)
    if run == 1:
        circles.append(run)
    elif run == 2:
        square.append(run)
    elif run == 3:
        cube.append(run)
            
amount_of_circles = len(circles)    
amount_of_squares = len(square)
amount_of_cube = len(cube)

print(amount_of_circles)
print(amount_of_squares)
print(amount_of_cube)

for i in range(0, len(circles)):
    circles.append(Circle())
    print(circles[i])
    
print("The number of Circles made is: ", amount_of_circles, '\n')

for i in range(0, len(square)):
    square.append(Square())
    print(square[i])
    
print("The number of Squares made is: ", amount_of_squares, '\n')

for i in range(0, len(cube)):
    cube.append(Square())  
    print(cube[i])
    
print("The number of Cubes made is: ", amount_of_cube, '\n')


names = ['Circles', 'Squares', 'Cubes']
shapes = [amount_of_circles, amount_of_squares, amount_of_cube]

plt.pie(shapes, labels = names)
plt.title("Amount of Shapes")
plt.show()

