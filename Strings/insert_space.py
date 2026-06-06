# Write a Python program to insert space before every capital letter appears in a given word.

def insert_space():
    string = input("Enter a string:").strip()
    result = ""

    for char in string:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result

print(insert_space()) 

