list_to_process = [10, 73, 10, 67, 40, 73, 50, 50, 67]

def duplicate_remover(original_list):
    interim_set = set(original_list)
    result = list(interim_set)
    result.sort()
    return result


if __name__ == '__main__':
    print(duplicate_remover(list_to_process))


