import random
def encode(message, key_value):
    message = message.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_chars = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
        ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
    ]
    encryption = ["_"]*len(message)
    for i in range(0,len(message)):
        if message[i] in alphabet:
            encryption[i] = alphabet[(int(alphabet.index(message[i])) + int(key_value))%len(alphabet)]
        else:
            encryption[i] = random.choice(special_chars)
    encrypted_msg = ''.join(encryption)
    return encrypted_msg

def decode(enc_msg , key_value):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_chars = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
        ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
    ]
    enc_msg = enc_msg.lower()
    decryption = ["_"]*len(enc_msg)
    for i in range(0,len(enc_msg)):
        if enc_msg[i] in alphabet:
            decryption[i] = alphabet[abs(int(alphabet.index(enc_msg[i])) - int(key_value)) % len(alphabet) ]
        else:
            decryption[i] = "_"
    decrypted_msg = ''.join(decryption)
    return decrypted_msg


print("WELCOME TO JONE'S key ALGO.....")

option = int(input("Enter your choice i for encrypt 0 for decrypt....."))
if option == 1:
    msg = input("Enter your message to encrypt...")
    key = input("Enter your key value to encrypt ")
    ans = encode(msg,key)
    print(f"Your encrypted value is ....{ans}")
else:
    msg = input("Enter your encrypted message to decrypt...")
    key = input("Enter your secret key value to encrypt ")
    ans = decode(msg,key)
    print(f"Your decrypted message  is ....{ans}")

