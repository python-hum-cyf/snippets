list_to_process = [10, 73, 10, 67, 40, 73, 50, 50, 67]

def duplicate_remover(original_list):
    result = []
    for elem in original_list:
        if elem not in result:
            result.append(elem)
    result.sort()
    return result


if __name__ == '__main__':
    print(duplicate_remover(list_to_process))


