vyruchka=int(input("Введите в тысячах, сколько вы заработали за год:"))
izdergki=int(input("Введите в тысячах, сколько вы потратили за год:"))
if vyruchka > izdergki:
    joker = vyruchka - izdergki
    rent = joker/vyruchka
    print ("Вы хорошо работаете, рентабельность", joker)
    sotrudniki = int(input("Введите число сотрудников в офисе:"))
    print (vyruchka - izdergki)
else:
    print ("У вас убыток")
