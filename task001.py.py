list_to_check = ['abc', 'pqr', 'ege', '5665', 'cc']

def string_list_checker(string_list):
    result = 0
    for string in string_list:
        if len(string) > 2:
            if string[0] == string[-1]:
                result += 1
    return result

if __name__ == '__main__':
    print(string_list_checker(list_to_check))

