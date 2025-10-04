def int_to_binary(n):
    if n <= 1:
        return str(n)
    return int_to_binary(n // 2)+ str(n % 2)
n = input("Enter a number: ")
print(int_to_binary(int(n)))
