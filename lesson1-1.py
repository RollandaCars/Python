number=int(input("Введите число, пожалуйста: "))
while number < 0 or number > 10:
    number = int(input("Введите еще число, пожалуйста: "))
if  number >0 and number <10:
    print("И его квадрат равен", number**2)