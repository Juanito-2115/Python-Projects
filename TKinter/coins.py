'''

    Name: Juan Pablo Meza
    Email: juanpablo.meza604@gmail.com
    
'''

from tkinter import *
import tkinter
import tkinter.messagebox
import tkinter.simpledialog


    
class Coin:
    def __init__(self, master):
        #Defining the specs of the window
        self.master = master
        master.title("Change Counter")
        master.geometry('750x750')
        master.configure(background = "Light Yellow")
        
        #Instructions
        self.instruction = Label(master, text = "Enter the number of each coin type that you have and \n hit 'Calculate' to calculate change", font = 15)
        self.instruction.grid(column = 1, row = 0)

        self.empty = Label(master, text = "").grid(column = 0, row = 1)    #Passes empty space to make it more appealing

        #Labels for each columns
        self.type = Label(master, text = "Type of Coin", font = ("Times New Roman", 15)).grid(column = 0, row = 2)
        self.input = Label(master, text = "Enter amount of coins", font = ("Times New Roman", 15)).grid(column = 1, row = 2)
        self.value = Label(master, text = "Value", font = ("Times New Roman", 15)).grid(column = 2, row = 2)
        self.final = Label(master, text = "Total", font = ("TImes New Roman", 15)).grid(column = 3, row = 2)

        
        #Row 37-83 define each row.
        self.dollar = Label(master, text = "Dollar Coin: ", font = 10).grid(column = 0, row = 3)
        self.dollar1 = Entry(master, width = 10)
        self.dollar1.grid(column = 1, row = 3)
        self.dollar_value = Label(master, text = "Dollar Coin Value: $", font = 10).grid(column = 2, row = 3)
        self.dollar2 = Label(master, text = "0.00", font = 10)
        self.dollar2.grid(column = 3, row = 3)

        self.half_dollar = Label(master, text = "Half Dollar Coin: ", font = 10).grid(column = 0, row = 4)
        self.half_dollar_1 = Entry(master, width = 10)
        self.half_dollar_1.grid(column = 1, row = 4)
        self.half_dollar_value = Label(master, font = 10, text = "Half Dollar Coin Value: $").grid(column = 2, row = 4)
        self.half_dollar_2 = Label(master, text = "0.00", font = 10)
        self.half_dollar_2.grid(column = 3, row = 4)

        self.quarter = Label(master, text = "Quarters: ", font = 10).grid(column = 0, row = 5)
        self.quarter1 = Entry(master, width = 10)
        self.quarter1.grid(column = 1, row = 5)
        self.quarter_value = Label(master, font = 10, text = "Quarter Value: $").grid(column = 2, row = 5)
        self.quarter2 = Label(master, text = "0.00", font = 10)
        self.quarter2.grid(column = 3, row = 5)

        self.dime = Label(master, text = "Dimes: ", font = 10).grid(column = 0, row = 6)
        self.dime1 = Entry(master, width = 10)
        self.dime1.grid(column = 1, row = 6)
        self.dime_value = Label(master, font = 10, text = "Dime Value: $").grid(column = 2, row = 6)
        self.dime2 = Label(master, text = "0.00", font = 10)
        self.dime2.grid(column = 3, row = 6)
    

        self.nickel = Label(master, text = "Nickels: ", font = 10).grid(column = 0, row = 7)
        self.nickel1 = Entry(master, width = 10)
        self.nickel1.grid(column = 1, row = 7)
        self.nickel_value = Label(master, font = 10, text = "Nickel Value: $").grid(column = 2, row = 7)
        self.nickel2 = Label(master, text = "0.00", font = 10)
        self.nickel2.grid(column = 3, row = 7)

        self.penny = Label(master, text = "Pennies", font = 10).grid(column = 0, row = 8)
        self.penny1 = Entry(master, width = 10)
        self.penny1.grid(column = 1, row = 8)
        self.penny_value = Label(master, font = 10, text = "Penny Value: $").grid(column = 2, row = 8)
        self.penny2 = Label(master, text = "0.00", font = 10)
        self.penny2.grid(column = 3, row = 8)

        self.calculate_button = Button(master, text = "Calculate", command = self.calculate, width = 20).grid(column = 1, row = 9)
        self.total_label = Label(master, text = "Total Change Value: $", font = 10).grid(column = 2, row = 9)
        self.total_value = Label(master, text = "0.00", font = 10)
        self.total_value.grid(column = 3, row = 9)
    
    
    #Calculate function to calculate the values that were inputted by the user    
    def calculate(self):
        int_dollar = int(self.dollar1.get())
        if int_dollar <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        dollar_calc = int_dollar * 1
        self.dollar2.config(text = format(dollar_calc, '.2f'))

        int_half_dollar = int(self.half_dollar_1.get())
        if int_half_dollar <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        half_dollar_calc = int_half_dollar * 0.50
        self.half_dollar_2.config(text = format(half_dollar_calc, '.2f'))

        int_quarter = int(self.quarter1.get())
        if int_quarter <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        quarter_calc = int_quarter * 0.25
        self.quarter2.config(text = format(quarter_calc, '.2f'))

        int_dime = int(self.dime1.get())
        if int_dime <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        dime_calc = int_dime * 0.10
        self.dime2.config(text = format(dime_calc, '.2f'))

        int_nickel = int(self.nickel1.get())
        if int_nickel <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        nickel_calc = int_nickel * 0.05
        self.nickel2.config(text = format(nickel_calc, '.2f'))

        int_penny = int(self.penny1.get())
        if int_penny <= 0:
            tkinter.messagebox.showerror("Error", "Number must be greater than 0")
        penny_calc = int_penny * 0.01
        self.penny2.config(text = format(penny_calc, '.2f'))

        total = (dollar_calc + half_dollar_calc + quarter_calc + dime_calc + nickel_calc + penny_calc)
        self.total_value.config(text = format(total, '.2f'))


#Running the program
if __name__ == '__main__':
    win = Tk()
    my_gui = Coin(win)
    win.mainloop()