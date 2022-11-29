list_one = [0, 45, 89, 'wlazl_kotek']
list_two = ['na_plotek', 89, 'i_mruga']
list_three = ['zaspiewaj', 966]
list_four = ['piosenka_niedluga', 1410]

def compare_lists(first_list, second_list):
    for elem in first_list:
        if elem in second_list:
            return True
    return False



if __name__ == '__main__':
    print(compare_lists(list_one, list_two))
    print(compare_lists(list_three, list_four))


