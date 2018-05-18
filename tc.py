# (50 degrees Celsius x 1.8) + 32 = 122 degrees Fahrenheit
# (122 degrees Fahrenheit - 32)  ÷ 1.8 = 50 degrees Celsiuss

import math
import time

ver = "ver, 1.2"
ts = "1526651421"

credit = "Made by gravypouch, lastest update:"

def ctf():
    ctfi = '0'
    cfta = '0'
    ctfi = float(input('Enter Celsius to Convert: '))
    ctfa = (ctfi * 1.8) + 32
    a = math.ceil(ctfa)
    print("Here is that in Fahrenheit:")
    print(a,"°F")
    print("")
    print("Returning to menu...")
    time.sleep(5)
    menu()

def ftc():
    ftci = '0'
    ftca = '0'
    ftci = float(input('Enter Fahrenheit to Convert: '))
    ftca = (ftci - 32) / 1.8
    a = math.ceil(ftca)
    print("Here is that in Celsius:")
    print(a,"°C")
    print("")
    print("Returning to menu...")
    time.sleep(5)
    menu()

def menu():
    choice ='0'
    while choice =='0':
        print("")
        print("The Temperature Converter:")
        print(credit,ts,ver)
        print("")
        print("# WARNING: This program rounds up. Keep that in mind")
        print("Choose 1 for Celsius to Fahrenheit")
        print("Choose 2 for Fahrenheit to Celsius")
        choice = input ("Please make a choice: ")
        if choice == "1":
            ctf()
        elif choice == "2":
            ftc()
        else:
            print("I don't understand your choice.")
            print("Returning you to menu......")
            time.sleep(5)
            print("")
            menu()

menu()
