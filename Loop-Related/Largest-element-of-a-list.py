my_list = [2,7,3,9,5,32,4,13,43,293,439,63,4,43,42,62,8,64,436,54]
largest = my_list[0]
for element in my_list:
    if element > largest:
        largest =element
print(largest)