def twonumbers ():
    one=int(input("введите первое целое число:"))
    two=int(input("Введите второе целое число:"))
    if two == 0:
         print("На ноль делить нельзя")
    else:
         three = one / two
         print(three)

twonumbers()