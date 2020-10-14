#!/usr/bin/env python3

def steg_encode_char(char, cover):
    """
    LSB encodes a character
        Args:
            char (str): a single character string
            cover (list): list of 8 strings representing integers in the range [0-255]
        Returns:
            None
    """
    msgBin = format(ord(char), '0>8b')

    for i in range(len(cover)):
        cover[i] = list(format(int(cover[i]), '0>8b'))
        cover[i][-1] = msgBin[i]
        cover[i] = str(int(''.join(cover[i]), 2))


def steg_decode_char(stego):
    """
    LSB decodes a character
        Args:
            stego (list): list of 8 strings representing integers in the range [0-255]
        Returns:
            str: character that was decoded
    """
    temp = []

    for i in range(len(stego)):
        stego[i] = list(format(int(stego[i]), '0>8b'))
        temp.append(stego[i][-1])
    return chr(int(''.join(temp), 2))


if __name__ == '__main__':
    pass
