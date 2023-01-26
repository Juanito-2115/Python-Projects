'''
    Name: Juan Pablo Meza
    Email: Juanpablo.meza604@gmail.com
    
    
    This program goes over the basic functions of Python such as: simple I/O, Selection Control, Loops, .random, functions, list/arrays, file I/O, creating graphs,
    classes and objects, inheritance, GUI and UML Diagram.
    1. This program creates of consisting a class with private attributes and to pass them onto a subclasses.
    2. The second part of the program consists of making an array/list and loops to create 15 objects.
    3. The third part of the program consists of the loop previously made to display the class and it's attributes.
    
'''

from Shapes import *
from tkinter import *
from tkinter import messagebox  

circle1 = Circle()
square1 = Square()
cube1 = Cube()

print("Pick what shape you would like to find the area/volume of:")
print("1. Circle")
print("2. Square")
print("3. Cube")

choice = int(input("Choice: "))

while choice < 1:
    print("Error! You have to pick one of the options above")
    choice = int(input("Choice: "))
    
while choice > 3:
    print("Error! You have to pick one of the options above")
    choice = int(input("Choice: "))
    
print("\nHow would you like to display the data that you picked above")
print("1. The Python Console")
print("2. Into a seperate file")
print("3. Into a message box")

choice_2 = int(input("Choice: "))

while choice_2 < 1:
    print("Error! You have to pick one of the options above")
    choice = int(input("Choice: "))
    
while choice_2 > 3:
    print("Error! You have to pick one of the options above")
    choice = int(input("Choice: "))

if choice_2 == 1:
    if choice == 1:
        print('\n')
        print(circle1.display())
    elif choice == 2:
        print('\n')
        print(square1.display())
    elif choice == 3:
        print('\n')
        print(cube1.display())
elif choice_2 == 2:
    if choice == 1:
        file_name = input("Enter the file name with the '.txt' extension: ")
        new_file = open(file_name, "w")
        new_file.write(circle1.display())
        new_file.close()
    elif choice == 2:
        file_name = input("Enter the file name with the '.txt' extension: ")
        new_file = open(file_name, "w")
        new_file.write(square1.display())
        new_file.close()
    elif choice == 3:
        file_name = input("Enter the file name with the '.txt' extension: ")
        new_file = open(file_name, "w")
        new_file.write(cube1.display())
        new_file.close()
elif choice_2 == 3:
    if choice == 1:
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showinfo('Circle Results', circle1.display())
        window.deiconify()
        window.destroy()
        window.quit()
    elif choice == 2:
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showinfo('Square Results', square1.display())
        window.deiconify()
        window.destroy()
        window.quit()
    elif choice == 3:
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showinfo('Cube Results', cube1.display())
        window.deiconify()
        window.destroy()
        window.quit()
