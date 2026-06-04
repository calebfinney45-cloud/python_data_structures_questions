# Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.

def first_three_char():
    string = input("Enter a string: ").strip()
    if len(string) <= 3:
        return string
    else:
        return string[:3]
 
print(first_three_char())


