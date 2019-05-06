# -*- coding: utf-8 -*-
dlugosc = float(input("Podaj odległość w cm do przelcizenia: "))
print ("\nPodany wymiar",dlugosc,"cm to {:.4f}" .format(dlugosc / 100),"metrów lub {:.4f}" .format(dlugosc * 0.394),"cali")

#lepiej
cm_to_m = dlugosc/100
cm_to_cal = dlugosc/0.394

print ("Podany wymiar {:.2f} cm to {} metrów lub {:.2f} cali". format(dlugosc, cm_to_m, cm_to_cal))

input('\nPress enter to continue...')
