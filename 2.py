# -*- coding: utf-8 -*-

#imie = input("Jak masz na imię ? ")
#print ("Cześć", imie, "!!! Miło Cię poznać")


waga = int(input("Ile ważysz ? "))
wzrost = float(input("Ile masz wzrotu "))
BMI = waga / (wzrost ** 2)
print ("Twój BMI wynosi:", BMI)

print ("Twój BMI wynosi: {:f}".format(BMI))

print ("Twój BMI wynosi:", round(BMI,2))
