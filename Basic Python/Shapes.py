'''
    Name: Juan Pablo Meza
    Email: Juanpablo.meza604@gmail.com
    
    
    This program goes over the basic functions of Python such as: simple I/O, Selection Control, Loops, .random, functions, list/arrays, file I/O, creating graphs,
    classes and objects, inheritance, GUI and UML Diagram.
    1. This program creates of consisting a class with private attributes and to pass them onto a subclasses.
    2. The second part of the program consists of making an array/list and loops to create 15 objects.
    3. The third part of the program consists of the loop previously made to display the class and it's attributes.
    
'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color = 'red'):
        self.__color = color

    def set_color(self):
        self.__color = color

    def get_color(self):
        return(self.__color)

    def find_area(self):
        pass

    def find_volume(self):
        pass

    def display(self):
        print(self.__color)
        
   
class Circle(Shape):
    def __init__(self, radius = 1, color = 'red'):
        self.__radius = radius
        Shape.__init__(self, color)

    def set_radius(self):
        self.__radius = radius

    def get_radius(self):
        return(self.__radius)

    def find_area(self):
        return(self.__radius**2 * math.pi)

    def display(self):
        return "The area of the Circle is: " + str(format(self.find_area(), '.2f')) + ". The radius of the Circle is: " + str(self.get_radius()) + ". The color of the Circle is: " + str(self.get_color())


class Square(Shape):
    def __init__(self, sides = 2.3, color = 'red'):
        self.__sides = sides
        Shape.__init__(self, color)

    def set_sides(self):
        self.__sides = sides

    def get_sides(self):
        return(self.__sides)

    def find_area(self):
        return(self.__sides**2)

    def display(self):
        return "The area of the Square is: " + str(format(self.find_area(), '.2f')) + ". The length of the sides of the Square are: " + str(self.get_sides()) + ". The color of the Square is: " + str(self.get_color())


class Cube(Shape):
    def __init__(self, color = 'red', sides = 5.5):
        self.__sides = sides
        Shape.__init__(self, color)

    def set_sides(self):
        self.__sides = sides

    def get_sides(self):
        return(self.__sides)

    def find_volume(self):
        return(self.__sides**3)

    def display(self):
        return "The volume of the Cube is: " + str(format(self.find_volume(), '.2f')) + ". The length of the sides of the Cube are: " + str(self.get_sides()) + ". The color of the Cube is: " + str(self.get_color())
