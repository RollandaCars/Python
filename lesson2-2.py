count=0
newlist=[]
while count <= 5:
    el = input("Введите 6 целых значений, сейчас:")
    newlist.extend(el)
    print(newlist)
    count = count +1
else:
    print(newlist[1], newlist [0], newlist [3], newlist [2], newlist [5], newlist [4])
