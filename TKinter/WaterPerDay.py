'''
    Name: Juan Pablo Meza
    Email: juanpablo.meza604@gmail.com
    
    This program asks the user to enter their weight and tells them how much water they should drink per day.

'''

from tkinter import *

window = Tk()
window.title("Cups of Water Per Day Calculator")
window.geometry('930x200')

instruction = Label(window, text = "Are you trying to find out how many cups of water you should drink per day? \n Enter your information down below!", font = 30)
instruction.grid(column = 1, row = 0)

empty = Label(window, text ='').grid(column = 0, row = 1)

weight = Label(window, text = "Enter your weight in pounds:", font = 30).grid(column = 0, row = 4)
weight1 = Entry(window, width = 10)
weight1.grid(column = 1, row = 4)
weight2 = Label(window, text = "Cups of water per day:", font = 30).grid(column = 2, row = 4)
total = Label(window, text = "0", font = 30)
total.grid(column = 3, row = 4)


def calculate():
    lbs = float(weight1.get())
    ounces = lbs * 0.5
    cups = ounces / 8
    total.config(text = round(cups))

compute = Button(window, text = "Calculate", command = calculate).grid(column = 1, row = 5)
window.mainloop()
                                                  