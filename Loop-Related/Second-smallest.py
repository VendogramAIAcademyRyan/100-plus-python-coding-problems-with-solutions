my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


def second_smallest_element(my_list):
    smallest = my_list[0]
    for element in my_list:
        if element <=smallest:
            smallest = element
    second_smallest = None
    for element in my_list:
        if element != smallest:
            if second_smallest is None or element <= second_smallest:
                second_smallest = element
    return print(second_smallest)
second_smallest_element(my_list)