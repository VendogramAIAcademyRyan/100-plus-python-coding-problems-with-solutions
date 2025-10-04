try:
    dec = int(input("Enter a floating-point number: "))
    bnr = bin(dec).replace("0b", "")
except ValueError:
    print("Invalid input")
else:
    print(f"The binary representation of {dec} is {bnr}")
