my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2
    total = 0
for element in my_list:
    total += element
print(total)