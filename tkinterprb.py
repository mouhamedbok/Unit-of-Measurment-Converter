from tkinter import *
import pandas as pd

def result(lengthseries, labelresult):
    x = ma_variable1.get()
    y = ma_variable2.get()
    z = ma_variable3.get()

    a = int(x)
    b = int(y)
    m = float(z)

    if (7 > a >= b):
        ch = (str(m) + lengthseries[a][3:] + " = " +
              str(m * (10 ** (a - b))) + lengthseries[b][3:])
    elif (a <= b < 7):
        ch = (str(m) + lengthseries[a][3:] + " = " +
              str(m * (10 ** (a - b))) + lengthseries[b][3:])
    elif (a == 7):
        ch = (str(m) + lengthseries[a][3:] + " = " +
              str(m / 3.28084 * (10 ** (3 - b))) + lengthseries[b][3:])
    elif (b == 7):
        ch = (str(m) + lengthseries[a][3:] + " = " +
              str(m * 3.28084 * (10 ** (a - 3))) + lengthseries[b][3:])

    labelresult["text"] = ch


def convertlength():
    length = ["-> Millimeter", "-> Centimeter", "-> Decimeter", "-> Meter",
              "-> Dekameter", "-> Hectometer", "-> Kilometer", "-> Foot"]

    lengthseries = pd.Series(length)

    label1["text"] = lengthseries.to_string(index=True)
    buttonres = Button(frame_buttons,text="Result",bg='blue',fg='white',command=lambda: result(lengthseries, labelresult)
    )
    buttonres.grid(row=1, column=0, pady=10)
def result_mass(massseries, labelresult):
    x = ma_variable1.get()
    y = ma_variable2.get()
    z = ma_variable3.get()

    a = int(x)
    b = int(y)
    m = float(z)

    if (a >= b):
        ch = (str(m) + massseries[a][3:] + " = " +str(m * (10 ** (b - a))) + massseries[b][3:])
    elif (a <= b):
        ch = (str(m) + massseries[a][3:] + " = " +str(m * (10 ** (a - b))) + massseries[b][3:])

    labelresult["text"] = ch


def convertmass():
    mass = ["-> Milligram", "-> Centigram", "-> Decigram", "-> Gram","-> Dekagram", "-> Hectogram", "-> Kilogram"]

    massseries = pd.Series(mass)

    label1["text"] = massseries.to_string(index=True)

    buttonres = Button(frame_buttons,text="Result",bg='blue',fg='white',command=lambda: result_mass(massseries, labelresult)
    )
    buttonres.grid(row=1, column=1, pady=10)

def result_time(timeseries, labelresult):
    x = ma_variable1.get()
    y = ma_variable2.get()
    z = ma_variable3.get()

    a = int(x)
    b = int(y)
    m = float(z)

    ch = ""

    factors = [1, 60, 3600, 86400, 604800, 2592000, 31104000, 311040000]

    value_in_seconds = m * factors[a]
    result_value = value_in_seconds / factors[b]

    ch = str(m) + " " + timeseries[a][3:] + " = " + \
         str(result_value) + " " + timeseries[b][3:]

    labelresult["text"] = ch


def converttime():
    time = ["-> second", "-> minute", "-> hour", "-> day",
            "-> week", "-> month", "-> year", "-> decade"]

    timeseries = pd.Series(time)

    label1["text"] = timeseries.to_string(index=True)

    buttonres = Button(frame_buttons,text="Result",bg='blue',fg='white',command=lambda: result_time(timeseries, labelresult)
    )
    buttonres.grid(row=1, column=2, pady=10)


fenetre = Tk()
fenetre.geometry('500x600')
fenetre.title('Unit_of_Measurment_Converter')
fenetre['bg'] = 'white'
fenetre.resizable(False, False)


labell=Label(fenetre,text="Choose your type of measurement",font=("Verdana", 12, "bold"),fg="white",bg="green").pack(fill=X, pady=10)


main_frame = Frame(fenetre, bg="white")
main_frame.pack(pady=20)

Label(main_frame, text="From (index):",
      bg="white").grid(row=0, column=0, padx=10, pady=10)

ma_variable1 = StringVar()
entree1 = Entry(main_frame, textvariable=ma_variable1)
entree1.grid(row=0, column=1, padx=10)

Label(main_frame, text="To (index):",
      bg="white").grid(row=1, column=0, padx=10, pady=10)

ma_variable2 = StringVar()
entree2 = Entry(main_frame, textvariable=ma_variable2)
entree2.grid(row=1, column=1, padx=10)

Label(main_frame, text="Enter value:",
      bg="white").grid(row=2, column=0, padx=10, pady=10)

ma_variable3 = StringVar()
entree3 = Entry(main_frame, textvariable=ma_variable3)
entree3.grid(row=2, column=1, padx=10)


labelresult = Label(fenetre,text="",font=("Verdana", 15, "italic"),fg="red",bg="white")
labelresult.pack(pady=15)


label1 = Label(fenetre,text="",bg="white",font=("Verdana", 10),justify=LEFT)
label1.pack(pady=10)


frame_buttons = Frame(fenetre, bg="white")
frame_buttons.pack(pady=20)

button1 = Button(frame_buttons,text="Length",bg='blue',fg='white',command=convertlength)
button1.grid(row=0, column=0, padx=10)

button2 = Button(frame_buttons,text="Mass",bg='blue',fg='white',command=convertmass)
button2.grid(row=0, column=1, padx=10)

button3 = Button(frame_buttons,text="Time",bg='blue',fg='white',command=converttime)
button3.grid(row=0, column=2, padx=10)

fenetre.mainloop()
