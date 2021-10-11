'''
To install the below modules:
Open your terminal and type - 
pip install tkinter
Once the installation is done go ahead and run the code
'''

import tkinter
root = tkinter.Tk()
root.title("BMI Calculator")

# Function to calculate BMI
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    height = height/100
    bmi = round(kg / ((height)**2),2)
    
    if bmi<18.5:
        type="Under weight"
    elif 18.5<=bmi<=24.9:
        type="Normal"
    elif 25<=bmi<=29.9:
        type="Over weight"
    elif bmi>=30:
        type="Obese"
    label_result['text'] = f"BMI: {bmi} {type}"


# Creating GUI
label_kg = tkinter.Label(root, text="WEIGHT (in kg): ")
label_kg.grid(column=0,row=0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=0,row=1)

label_height = tkinter.Label(root, text="HEIGHT (in cm): ")
label_height.grid(column=1,row=0)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1,row=1)

label_result = tkinter.Label(root, text=f"BMI: ")
label_result.grid(column=1,row=2)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)
root.mainloop()
