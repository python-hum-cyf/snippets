# Przykład wyrażenia listowego (list comprehension) w funkcji:

# import funkcji z biblioteki sympy - pozwala ona wygodnie sprawdzać czy coś jest liczbą pierwszą
from sympy import isprime

# Tworzymy dwie listy - krótką i długą, jedna zawiera liczby całkowite od 0 do 7, a druga od 0 do 18
numbers_short = list(range(8))
numbers_long = list(range(19))

# To nasza funkcja: jako parametr przyjmuje ona jakąś listę liczb całkowitych, a następnie na jej podstawie tworzy nową listę,
# złożoną z liczb pierwszych należących do listy przyjętej jako parametr.
# Dokładnie działa to tak: 'num for num in int_list' - każda liczba z listy int_list 'if isprime(num)' - jeśli jest ona liczbą pierwszą
# Na koniec funkcja drukuje powstałą listę.

def prime_checker(int_list):
    list_comp = [num for num in int_list if isprime(num)]
    print(list_comp)

# Poniżej linii 20 mamy kod, który się wykona, kiedy uruchomimy skrypt. A zatem dwukrotnie wywołujemy naszą funkcję, najpierw z krótką,
# a potem długą listą - zatem w wyniku działania programu powinny wyświetlić się dwie listy - jedna zawiera liczby pierwsze z zakresu od 0 do 7,
# a druga z zakresu od 0 do 18.

if __name__ == '__main__':
    prime_checker(numbers_short)
    prime_checker(numbers_long)
