start = int(input("Введите результат спортсмена в первый день (км):"))
finish = int(input("Введите результат спортсмена в последний день (км):"))
count=0

while start<=finish:
    count += 1
    start=start+0.1*start
else:
    print(count)

