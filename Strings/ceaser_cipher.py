# Write a Python program to create a Ceaser encryption

'''
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, 
 the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
 It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
 For example, with a left shift of 3, D would be replaced by A, E would become B, and so on
'''

#A python program to illustrate Caesar Cipher Technique
def encrypt(text, shift):
    result = ""

    #traverse/go through each character in the string
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if(char.isupper()):
            # ord() *ordinal* function returns the ASCII value of the character. The shift value added to the ASCII value, then 65 subtracted 
            # to get the character in the 0-25 index. result taken % 26 to wrap around the alphabet, then 65 added to get the ASCII value
            # Finally, the chr() *character* function converts the ASCII value back to a character and appends it to the result string.
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters    
        else:
            #Same as above but with 97 instead of 65 to handle lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

text = input("Enter a string: ").strip()
shift = int(input("Enter a shift value: "))

print(f"Text : {text}")
print(f"Shift value : {str(shift)}")
print(f"Cipher : {encrypt(text, shift)}")