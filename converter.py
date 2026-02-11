import pandas as pd

print("This is a measurement converter.")
print("Select the number of the unit you need to convert:")

data = ["-> Length", "-> Mass", "-> Time"]
series = pd.Series(data)
print(series)

x = int(input())

if (x == 0):
    length = ["-> Millimeter", "-> Centimeter", "-> Decimeter", "-> Meter",
              "-> Dekameter", "-> Hectometer", "-> Kilometer", "-> Foot"]
    lengthseries = pd.Series(length)
    print(lengthseries)

    print("Enter the number of the unit you have:")
    a = int(input())

    print("Enter the number of the unit you want to convert to:")
    b = int(input())

    print("Enter the measurement:")
    m = float(input())

    if (7 > a >= b):
        print(m, lengthseries[a][3:], "=", m * (10 ** (a - b)), lengthseries[b][3:])
    elif (a <= b < 7):
        print(m, lengthseries[a][3:], "=", m * (10 ** (b - a)), lengthseries[b][3:])
    elif (a == 7):
        print(m, lengthseries[a][3:], "=", m / 3.28084 * (10 ** (3 - b)), lengthseries[b][3:])
    elif (b == 7):
        print(m, lengthseries[a][3:], "=", (m * 3.28084) * (10 ** (a - 3)), lengthseries[b][3:])

elif (x == 1):
    mass = ["-> Milligram", "-> Centigram", "-> Decigram", "-> Gram",
            "-> Dekagram", "-> Hectogram", "-> Kilogram"]
    massseries = pd.Series(mass)
    print(massseries)

    print("Enter the number of the unit you have:")
    a = int(input())

    print("Enter the number of the unit you want to convert to:")
    b = int(input())

    print("Enter the measurement:")
    m = float(input())

    if (a >= b):
        print(m, massseries[a][3:], "=", m * (10 ** (b - a)), massseries[b][3:])
    elif (a <= b):
        print(m, massseries[a][3:], "=", m * (10 ** (a - b)), massseries[b][3:])
elif(x==2):
    time=["-> second","-> minute","-> hour","-> day","-> week","-> month","-> year","-> decade"]
    timeseries=pd.Series(time)
    print(timeseries)
    print("input the number of the unit you have")
    a=int(input())
    print("input the number of the unit you want to convert to")
    b=int(input())
    print("input the mesure")
    m=float(input())
    if (a==0):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m/60," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m/3600," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m/(24*3600)," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",m/(24*7*3600)," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m/(24*3600*30)," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(24*3600*30*12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(24*3600*30*12*10)," ",timeseries[b][3:])
    if(a==1):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*60," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m/60," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m/(24*60)," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",m/(24*7*60)," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m/(24*60*30)," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(24*60*30*12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(24*60*30*12*10)," ",timeseries[b][3:])
    if(a==2):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*3600," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*60," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m/(24)," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",m/(24*7)," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m/(24*30)," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(24*30*12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(24*30*12*10)," ",timeseries[b][3:])
    if(a==3):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*3600*24," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*(60*24)," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m*24," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",m/(7)," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m/(30)," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(30*12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(30*12*10)," ",timeseries[b][3:])
    if(a==4):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*7*3600*24," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*7*(60*24)," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m*7*24," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m*7," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m/(7*30)," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(7*30*12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(7*30*12*10)," ",timeseries[b][3:])
    if(a==5):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*31*3600*24," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*31*(60*24)," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m*31*24," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m*31," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",(m/31)*7," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m/(12)," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(12*10)," ",timeseries[b][3:])
    if(a==6):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*31*3600*24*12," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*31*(60*24)*12," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m*31*24*12," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m*31*12," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",(m/31)*7*12," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m*12," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m/(10)," ",timeseries[b][3:])
    if(a==7):
        if(b==0):
            print(m ," ",timeseries[a][3:],"=",m*31*3600*24*12*10," ",timeseries[b][3:])
        if(b==1):
            print(m ," ",timeseries[a][3:],"=",m*31*(60*24)*12*10," ",timeseries[b][3:])
        if(b==2):
            print(m ," ",timeseries[a][3:],"=",m*31*24*12*10," ",timeseries[b][3:])
        if(b==3):
            print(m ," ",timeseries[a][3:],"=",m*31*12*10," ",timeseries[b][3:])
        if(b==4):
            print(m ," ",timeseries[a][3:],"=",(m/31)*10*7*12," ",timeseries[b][3:])
        if(b==5):
            print(m ," ",timeseries[a][3:],"=",m*12*10," ",timeseries[b][3:])
        if(b==6):
            print(m ," ",timeseries[a][3:],"=",m*10," ",timeseries[b][3:])
        if(b==7):
            print(m ," ",timeseries[a][3:],"=",m," ",timeseries[b][3:])

