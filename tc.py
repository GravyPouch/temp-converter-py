# (50 degrees Celsius x 1.8) + 32 = 122 degrees Fahrenheit
# (122 degrees Fahrenheit - 32)  ÷ 1.8 = 50 degrees Celsiuss

import math

ver = "ver, 1.0"
ts = "1526607802"

credit = "Made by gravypouch, last update:"

def ctf():
    ctfi = '0'
    cfta = '0'
    ctfi = int(input('Enter Celsius to Convert: '))
    ctfa = ctfi * 1.8
    ctfra = ctfa + 32
    a = math.ceil(ctfra)
    print("Here is that in Fahrenheit:")
    print(a,"°F")
    print("")
    menu()

def ftc():
    ftci = '0'
    ftca = '0'
    ftci = int(input('Enter Fahrenheit to Convert: '))
    ftca = ftci - 32
    ftcra = ftca / 1.8
    a = math.ceil(ftcra)
    print("Here is that in Celsius:")
    print(a,"°C")
    print("")
    menu()

def menu():
    choice ='0'
    while choice =='0':
        print("")
        print("The Temperature Converter:")
        print(credit,ts,ver)
        print("")
        print("# WARNING: This program does not support decimals at this moment in time.")
        print("Choose 1 for Celsius to Fahrenheit")
        print("Choose 2 for Fahrenheit to Celsius")
        choice = input ("Please make a choice: ")
        if choice == "1":
            ctf()
        elif choice == "2":
            ftc()
        else:
            print("I don't understand your choice.")
            print("")
            menu()

menu()
