
list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
month = int(input("Введите число месяца:"))
if month <=2 or month == 12:
    print ("Это зима, парень")
if month >= 3 and month < 6:
    print ("Это весна!")
if month >=6 and month <9:
    print ("Лето!")
if month >= 9 and month < 12:
    print("Что такое осень!")

## И ЧЕРЕЗ DICT

dict={"Зима":12, "Зима":1, "Зима":2, "Весна":3, "Весна":4, "Весна":5, "Лето":6, "Лето":7, "Лето":8, "Осень":9, "Осень":10, "Осень":11 }
value= int(input("Введите число месяца:"))
for value in dict
    print (dict.keys())