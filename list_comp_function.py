from sympy import isprime

numbers_short = list(range(8))
numbers_long = list(range(19))


def prime_checker(int_list):
    list_comp = [num for num in int_list if isprime(num)]
    print(list_comp)

def dumb_greeter():
    print('Hello world!')

def max_even_checker(int_list):
    list_comp = [num for num in int_list if num % 2 == 0]
    if max(list_comp) < 10:
        return 'Tak!'
    return 'Nie!'


if __name__ == '__main__':
    print(max_even_checker(numbers_long))

