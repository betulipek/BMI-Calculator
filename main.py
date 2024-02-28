import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)
window.config(padx=30, pady=30)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Please Enter Weight and Height")

    else:
        bmi = weight / height ** 2
        print((bmi))


weight_input_label = tkinter.Label(text="Enter Your Weight (Kg)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter Your Height (Cm)")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()

heightandweight_label = tkinter.Label(text="")
heightandweight_label.pack()

calculate_button = tkinter.Button(text="Calculate",width=15, command=calculate_bmi)
calculate_button.pack()


result_label = tkinter.Label()
result_label.pack()


window.mainloop()
