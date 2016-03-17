# -*- encoding: utf-8 -*-

ime = raw_input("Vnesi svoje ime: ")
stevilo = 30

print "Pozdravljen " + ime + ", ali lahko uganes število, ki ga imam v mislih? "

poizskus = raw_input("Vnesi število: ")

while int(poizskus) > stevilo:
    poizskus = raw_input(" Število je previliko, poizkusi ponovno: ")

while int(poizskus) < stevilo:
    poizskus = raw_input(" Število je premalo, poizkusi ponovno: ")

while int(poizskus) == stevilo:
    poizskus = raw_input(" Čestitam, uganil si")
