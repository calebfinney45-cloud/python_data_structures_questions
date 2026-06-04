def del_specific_char():
    result = ""

    for char in sentence:
        if char != selected_char:
            result += char
    return result         

sentence = input("Enter your string: ")
selected_char = input("Enter the character you want to delete: ")

print(del_specific_char())
