import math
import sys as system
# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty
# na sam koniec.
print("Zadanie 1")
sporty = ["tenis", "koszykówka", "siatkówka"]
print(sporty)
sporty.reverse()
print(sporty)
sporty.append('piłka ręczna')
print(sporty)
# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych. Jako klucz przyjmij
# skrót danego słowa, wartość to rozwinięcie tego skrótu.
print("Zadanie 2")
slownik = {'np': 'na przykład', 'itp': 'i tym podobne', 'ul': 'ulica'}
print(slownik)
# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim
# słowniku. Policz liczbę elementów w słowniku.
print("Zadanie 3")
slowniczek = {'klocek': 'minecraft', 'jedi': 'star wars'}
print(len(slowniczek))
# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
napis = input("Wprowadz napis: ")
print(napis.count("a"))
# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).


system.stdout.write("Podaj a: ")
a = int(system.stdin.readline())
system.stdout.write("Podaj b: ")
b = int(system.stdin.readline())
system.stdout.write("Podaj c: ")
c = int(system.stdin.readline())

licz = a ** b + c
print(licz)

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl
# odpowiedni komunikat. Użyj zagnieżdżeń.
a = input('Podaj a: ')
b = input('Podaj b: ')
c = input('Podaj c: ')

if (a >= b) & (a >= c):
    print(a)
elif (b >= a) & (b >= c):
    print(b)
else:
    print(c)
# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia
# pętli for podnieś każdą liczbę do kwadratu.
lista = [3, 17.3, 18.18, 5, 2]
for x in range(0, len(lista), 1):
    lista[x] *= lista[x]
print(lista)
# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
lista2 = []
count = 0
while count <= 9:
    a = int(input("Podaj liczbe: "))
    count += 1
    if a % 2 == 0:
        lista2.append(a)
print(lista2)

# Zad 9. Napisz skrypt, który rysuje następującą literę
napise = ""
lista3 = [1, 2, 3, 4, 5]
for x in lista3:
    if x % 2 == 0:
        napise += "E\n"
    else:
        napise += "EEEEEE\n"
print(napise)
# Zad. 10 Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość
# ujemną to powinien być wyłapany błąd.
x = (input("Podaj x, aby obliczyc pierwiastek z x: "))

try:
    wynik = math.sqrt(int(x))
    print(wynik)
except ValueError:
    print("Błąd! Podano ujemny x")
