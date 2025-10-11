active = True
while active:
    try:
        dist_in_miles = float(input("Enter distance in miles: (dont put word miles) "))

    except ValueError:
        print("Invalid input. Please enter a numeric value. you don't, i will hit you with  a 403 error")
        print("403 error means you are forbidden from entering non-numeric values")
        continue
    else:
        dist_in_km = dist_in_miles * 1.069344
        print(f"Distance in kilometers is: {dist_in_km} km")
        active = False