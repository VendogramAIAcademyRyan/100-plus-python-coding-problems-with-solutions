try:
    integer1 = int(input("enter an integer:"))
except ValueError:
    print("This is not an integer")
else:
    print("You entered the integer:", integer1)
    correct = input("Is this correct? (yes/no): ").strip().lower()
    if correct == 'yes':
        print("Thank you for confirming.")
finally:
    try:
        float1 = float(input("Enter a floating-point number: "))
    except ValueError:
        print("This is not a floating-point number.")
    else:
        print("You entered the floating-point number:", float1)
        correct_float = input("Is this correct? (yes/no): ").strip().lower()
        if correct_float == 'yes':
            print("Thank you for confirming.")
print(f"These numbers multiplied together equal:{integer1*float1}")
    