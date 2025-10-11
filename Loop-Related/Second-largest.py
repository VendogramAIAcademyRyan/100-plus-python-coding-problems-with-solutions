my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


def second_largest_element(my_list):
    largest = my_list[0]
    for element in my_list:
        if element > largest:
            largest = element
    second_largest = None
    for element in my_list:
        if element != largest:
            if second_largest is None or element > second_largest:
                second_largest = element
    return print(second_largest)
second_largest_element(my_list)