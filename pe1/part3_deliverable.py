#!/usr/bin/env python3

def steg_encode(msg, cover):
    """
    LSB encodes a message
        Args:
            msg (str): a string message to encode
            cover (list): list of strings representing integers in the range [0-255]
        Returns:
            None
    """
    count = 0

    for char in msg:
        msgBin = format(ord(char), '0>8b')

        for i in range(8):
            cover[count] = list(format(int(cover[count]), '0>8b'))
            cover[count][-1] = msgBin[i]
            cover[count] = str(int(''.join(cover[count]), 2))
            count += 1


def steg_decode(stego):
    """
    LSB decodes a message
        Args:
            stego (list): list of strings representing integers in the range [0-255]
        Returns:
            str: message that was decoded
    """
    temp = []
    msg = []
    count = 0

    for i in range(len(stego)):
        stego[i] = list(format(int(stego[i]), '0>8b'))
        temp.append(stego[i][-1])
        count += 1

        if count == 8:
            msg.append(chr(int(''.join(temp), 2)))
            temp = []
            count = 0

    return ''.join(msg)


if __name__ == '__main__':
    pass
