# this is project about encrypting and decrypting text using caesar cipher

import string

print("""                                                                     ___   ___                                       
 #####  #######    #     #####     #    ######  
#     # #         # #   #     #   # #   #     # 
#       #        #   #  #        #   #  #     # 
#       #####   #     #  #####  #     # ######  
#       #       #######       # ####### #   #   
#     # #       #     # #     # #     # #    #  
 #####  ####### #     #  #####  #     # #     # 
      
 #####  ### ######  #     # ####### ######  
#     #  #  #     # #     # #       #     # 
#        #  #     # #     # #       #     # 
#        #  ######  ####### #####   ######  
#        #  #       #     # #       #   #   
#     #  #  #       #     # #       #    #  
 #####  ### #       #     # ####### #     # 
"""
)

LETTERS = list(string.ascii_lowercase)

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index = LETTERS.index(char)
            new_index = (index + shift) % 26
            new_char = LETTERS[new_index]
            if is_upper:
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Enter text: ")
shift = 5
encrypted_text = encrypt(text, shift)
print(f"Encrypted text: {encrypted_text}")
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")