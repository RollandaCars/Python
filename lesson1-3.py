number=int(input("Что бы узнать, сколько будет х+хх+ххх, введите х:"))
numberstr = str(number)
fase2 = numberstr + numberstr
fase3 = numberstr + numberstr + numberstr
summ = number + int(fase2) + int(fase3)
print("x+xx+xxx=", summ)