# find permutation of a list
import random
def permutations(lst):
    # Base case: if the list has only one element, return it as the only permutation
    if len(lst) == 1:
        return [lst]
    
    # Recursive case
    result = []
    for i in range(len(lst)):
        # Extract the current element
        current = lst[i]
        # Remaining list after removing the current element
        remaining = lst[:i] + lst[i+1:]
        # Generate permutations of the remaining list
        for perm in permutations(remaining):
            result.append([current] + perm)
    
    return result
numbers_used = [1,2,3,4,5,6,7,8,9]
# Example usage
data = []
try:
    data_length = int(input("how many values? i will use values 1 to 9 randomly: "))
    for i in range(data_length):
        data.append(random.choice(numbers_used))

except ValueError:
    print("enter integer")
finally:
    perm = permutations(data)
    print(perm)
    print(len(perm))