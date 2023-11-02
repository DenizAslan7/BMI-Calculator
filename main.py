import tkinter

# screen
screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.config(padx=10,pady=10)
screen.minsize(width=550,height=400)

# Weight label
weight_label = tkinter.Label(text=("Enter Your Weight (kg)"),font=("Ariel",20,"normal"))
weight_label.config(pady=15,padx=0)
weight_label.pack()

# weight entry
weight_entry = tkinter.Entry()
weight_entry.config(width=40)
weight_entry.focus()
weight_entry.pack()

# height label
height_label = tkinter.Label(text="Enter Your Height (cm)", font=("Ariel",20,"normal"))
height_label.config(pady=15,padx=0)
height_label.pack()

# height entry
height_entry = tkinter.Entry()
height_entry.config(width=40)
height_entry.pack()


# BMİ Calculation Fun
bmi = 0
def bmi_calculator():
    global bmi
    try:
        height = float(height_entry.get()) * 0.01
        weight = float(weight_entry.get())
        bmi = weight / (height * height)
        result()
    except:
        global result_label
        result_label.config(text="You must fill both blanks with digits only ",font=("Ariel",14,"normal"),fg="red")
        result_label.pack()



# result label and fat rating
fat_rating = ""
result_label = tkinter.Label()

def result():
    global fat_rating

    if bmi < 18.5:
        fat_rating = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        fat_rating = "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        fat_rating = "Overweight"
    elif bmi >= 30 and bmi <= 34.9:
         fat_rating = "Obesity (Class 1)"
    elif bmi >= 35 and bmi <= 39.9:
        fat_rating = "Obesity (Class 2)"
    elif bmi >= 40:
        fat_rating = "Extreme Obesity (Class 3)"
    else:
        pass
    global result_label
    result_label.config(text="Your BMI is : {}  {}".format(bmi, fat_rating), font=("Ariel", 12, "normal"),fg="black")
    result_label.pack()




# calculate button
calculate_button = tkinter.Button()
calculate_button.config(text="Calculate",width=10,command=bmi_calculator)
calculate_button.pack()


screen.mainloop()