# Początek jest znany - zob. snippet list_comp_primes - tam dokładnie wyjaśniam działanie

from sympy import isprime

numbers_short = list(range(8))
numbers_long = list(range(19))


def prime_checker(int_list):
    list_comp = [num for num in int_list if isprime(num)]
    print(list_comp)

# Poniższą funkcję zostawiam w kodzie wyłącznie po to, by przypomnieć, że funkcje nie zawsze muszą przyjmować argumenty, nie muszą też
# czegokolwiek zwracać. ;)
def dumb_greeter():
    print('Hello world!')

# Ta funkcja najpierw tworzy nową listę na podstawie listy przyjętej jako parametr - jest to lista zawartych w niej liczb parzystych.    
def max_even_checker(int_list):
    list_comp = [num for num in int_list if num % 2 == 0]
# A następnie jeśli największa liczba na otrzymanej liście jest mniejsza od 10, funkcja zwraca string 'Tak!',
# w przeciwnym razie zwraca string 'Nie!'. Proszę zwrócić uwagę na styl kodu i wcięcia - nie używam słowa kluczowego 'else'!
# Tak jak tłumaczyłem, polega to na tym, że najpierw sprawdzany jest warunek, jeśli jest spełniony, wykonuje się "return 'Tak!'"
# i działanie funkcji się kończy (na return), jeśli nie, przechodzimy do następnej linijki, gdzie czeka drugi return i działanie
# funkcji kończy się właśnie tam.
    if max(list_comp) < 10:
        return 'Tak!'
    return 'Nie!'

# Ostatnia uwaga, w razie gdyby nie było to oczywiste. Słowo kluczowe 'return' samo w sobie nie powoduje wyświetlenia wyniku działania funkcji, 
# lecz jedynie jego zwrócenie (stąd return) do pamięci komputera i dopiero ten wynik możemy jakoś wykorzystać, przypisać do zmiennej, wydrukować itp.
# Tu decydujemy się na wydrukowanie.
if __name__ == '__main__':
    print(max_even_checker(numbers_long))

