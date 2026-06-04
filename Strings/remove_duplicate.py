def remove_duplicate_char():
    string = input("Enter a string: ").strip()
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result

print(remove_duplicate_char())
