szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)




szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))

print ("Cyfra {} poprzedza {} a następna to {}".format(7,8,9))

print ("Rekord świata na 100m to {:f} ustanowił go {}".format(9.58,'Usain Bolt'))


waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie %d %s kosztuje %.2f zł" % (us, waluta, pln))

waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie {} {} kosztuje {:.2f} zł".format(us, waluta, pln))
