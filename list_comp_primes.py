from sympy import isprime

numbers_short = list(range(8))
numbers_long = list(range(19))


def prime_checker(int_list):
    list_comp = [num for num in int_list if isprime(num)]
    print(list_comp)


if __name__ == '__main__':
    prime_checker(numbers_short)
    prime_checker(numbers_long)
