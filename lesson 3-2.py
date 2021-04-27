def passport():
  name=str(input("Введите Ваше имя:"))
  surname=str(input("Введите Вашу фамилию:"))
  year=int(input("Год рождения:"))
  city=str(input("Город проживания:"))
  email=str(input("e-mail:"))
  number=int(input("телефон:"))
  print(name, surname, year, city, email,number)

passport()