#!/usr/bin/env python3

from collections import deque

def caesar_encrypt(plaintext,key):
    """
    Encrypts plaintext using the Caesar Cipher
        Args:
            plaintext (str): a string to be encrypted (all lowercase)
            key (int): number of characters to shift
        Returns:
            str: the encrypted ciphertext
    """

    str1 = "abcdefghijklmnopqrstuvwxyz"

    # Use deque() and rotate() to create shifted alphabet string
    d = deque(str1)
    d.rotate(key)
    str2 = ''.join(d)

    # Make the translation table using maketrans()
    transtable = str.maketrans(str1, str2)

    # Return the plaintext after encrypting it using translate()
    return plaintext.translate(transtable)


def caesar_decrypt(ciphertext,key):
    """
    Decrypts ciphertext using the Caesar Cipher
        Args:
            ciphertext (str): the string to be decrypted (all lowercase)
            key (int): number of characters to shift
        Returns:
            str: the decrypted plaintext
    """

    # It's the same process, just backwards, so negate the key and it'll do a back shift
    return caesar_encrypt(ciphertext, -key)

    # You could also just call encrypt again because the unit test is broken
    #return caesar_encrypt(ciphertext, key)


if __name__ == '__main__':
	pass
