my_list = []
input_string = int(input("Enter number of elements you want in the list: "))
def sum_of_elements(my_list):
    for i in range(0, input_string):
        element = int(input("Enter element: "))
        my_list.append(element)
    total = 0
    for element in my_list:
        total += element
    return print(total)
sum_of_elements(my_list)