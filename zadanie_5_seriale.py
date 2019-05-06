# -*- coding: utf8 -*-

"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i jego oceny.
Dodaj do swojego spisu.
"""

seriale = {
    'The Bridge' : 7.5,
    'Black Mirror' : 6.0,
    'Vikings' : 8,
    'Game of Thrones' : 8.5
    }

print('******************************************')
print('Moje seriale:')
print(list(seriale.keys()))
print('******************************************')

nazwa = input('Wybierz serial: ')
print('Serial {} otrzymał ocenę {}'.format(nazwa,seriale[nazwa]))

new = input('Jaki serial chcesz dodać ? ')
rating = input ('Jaką dajesz ocenę ? ')

seriale[new]=float(rating)

print('******************************************')
print (list(seriale.keys()))
print (seriale.keys())

input('\nPress enter to continue...')



