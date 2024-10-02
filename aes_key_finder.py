#!/usr/bin/python3
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def main():

    _, first, second, third = sys.argv

    if len(first) != 21:
        print("Error: Plaintext must be exactly 21 characters.")
        sys.exit(1)

    try:
        data = bytearray(first, encoding='utf-8')
        ciphertext = bytearray.fromhex(second)
        iv = bytearray.fromhex(third)
    except ValueError as e:
        print(f"Error in conversion: {e}")
        sys.exit(1)

    try:
        with open('./words.txt') as f:
            keys = f.readlines()
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        sys.exit(1)

    for k in keys:
        k = k.rstrip('\n')
        if len(k) <= 16:
            key = k + '#' * (16 - len(k))
            cipher = AES.new(key=bytearray(key, encoding='utf-8'), mode=AES.MODE_CBC, iv=iv)
            guess = cipher.encrypt(pad(data, 16))
            if guess == ciphertext:
                print("Key found:", key)
                sys.exit(0)

    print("Cannot find the key!")

if __name__ == "__main__":
    main()