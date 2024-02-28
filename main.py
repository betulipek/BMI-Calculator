from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300,300)

my_text_weight = Label(text="Enter Your Weight(kg)", pady=20)
my_text_weight.pack()

my_entry_weight = Entry(width=10)
my_entry_weight.pack()

my_text_height = Label(text="Enter Your Height(cm)", pady=20)
my_text_height.pack()

my_entry_height = Entry(width=10)
my_entry_height.pack()

my_text_column = Label(text="")
my_text_column.pack()



calculate_button = Button(text="Calculate", padx=20, pady=15)
calculate_button.pack()



window.mainloop()

