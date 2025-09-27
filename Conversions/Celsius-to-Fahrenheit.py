"""Simple Celsius → Fahrenheit converter.

This keeps a playful tone but avoids insults, handles common degree symbols
and common typos, and fixes variable-name spelling.
"""

def main():
    raw = input("Enter temperature in Celsius (you can include ° or C if you like): ").strip()
    
    # remove common degree symbols and whitespace
    clean = raw.replace("°", "").replace("º", "").strip()
    # remove trailing 'c' or 'C' if the user included it
    if clean.lower().endswith('c'):
        clean = clean[:-1].strip()

    if not clean:
        print("You didn't type a temperature. Try a number like 25 or 25.0.")
        return

    try:
        celsius = float(clean)
    except ValueError:
        # Fun but friendly error message
        print("I couldn't understand that as a number. Try something like 25 or 25.0 — I'll handle °C for you.")
        return

    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C is {fahrenheit} °F — nice choice of temperature!")


if __name__ == '__main__':
    main()
