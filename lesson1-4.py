number=int(input("Ввведите целое положительное двухзначное число:"))
first = number // 10
second = number % 10
list = [first, second]
print (max(list))