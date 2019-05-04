# -*- coding: utf-8 -*-

imie = input("Jak masz na imię ? ")
print ("Cześć", imie, "!!! Miło Cię poznać")
waga = int(input("Ile ważysz ? "))
wzrost = float(input("Ile masz wzrotu "))
BMI = waga / (wzrost ** 2)
print (imie, "Twój BMI wynosi:", BMI)


