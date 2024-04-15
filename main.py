import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # You can add more if u need safer encrypt
chars = list(chars)
key = chars.copy()

random.shuffle(key)

while True: 
    # Encrypt
    original_text = input('Enter message: ')
    encrypted_message = ""

    for letter in original_text:
        index = chars.index(letter)
        encrypted_message += key[index]
         
    print(f'Original text: {original_text}')
    print('\n')
    print(f'Encrypted message: {encrypted_message}')
    print('You can decrypt message if you type encrypted message!')
    
    # Decrypt
    encrypted_message = input('Enter message: ')
    print('\n')
    original_text = ""

    for letter in encrypted_message:
        index = key.index(letter)
        original_text += chars[index]
        
    print(f'Encrypted message: {encrypted_message}')
    print(f'Original text: {original_text}')
    continue

    

