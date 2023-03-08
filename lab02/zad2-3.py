lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = "Konrad"
litera_1 = imie[2]
nazwisko = "Jurewicz"
litera_2 = nazwisko[3]
liczba_liter1 = lorem_ipsum.count(litera_1)
liczba_liter2 = lorem_ipsum.count(litera_2)
print("W tekście jest '{}' liter '{}' oraz '{}' liter '{}'".format(liczba_liter1, litera_1, liczba_liter2, litera_2))