example_string = "programming"
example_string2 = "Achref Samoud"
result = ""
def remove_duplicates(s, result):
    for char in s.lower():
        if char not in result:
            result += char
    return print(result)
remove_duplicates(example_string, result)
remove_duplicates(example_string2, result)