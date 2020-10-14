#!/usr/bin/env python3

def sentinel():
    return chr(128)


def read_pgm(filename):
    """
    Reads a PGM file
        Args:
            filename (str): the file name of a PGM file on disk to read from
        Returns:
            tuple:
                1st element is a list of PGM header values as strings
                2nd element is a list of pixel intensities as strings
    """
    fin = open(filename, 'r')
    content = fin.read().split()
    fin.close()

    #Splits file into header and body elements
    for i in range(len(content)):
        if content[i] == '255':
            temp = (content[:i + 1], content[i + 1:])
            return temp


def write_pgm(filename, content):
    """
    Writes a PGM file
        Args:
            filename (str): the file name to be used for the written file
            content (tuple):
                1st element is a list of PGM header values as strings
                2nd element is a list of pixel intensities as strings
        Returns:
            None
    """
    fout = open(filename, 'w')

    # Header
    for i in range(len(content[0])):
        if i == 1:
            fout.write(content[0][i] + " ")
        else:
            fout.write(content[0][i] + "\n")

    # Tail
    for i in content[1]:
        fout.write(i + "\n")

    fout.close()


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

    #Hides message
    for char in msg:
        msgBin = format(ord(char), '0>8b')

        for i in range(8):
            cover[count] = list(format(int(cover[count]), '0>8b'))
            cover[count][-1] = msgBin[i]
            cover[count] = str(int(''.join(cover[count]), 2))
            count += 1

    #Adds sentinel character
    sentBin = format(ord(sentinel()), '0>8b')

    for i in range(8):
        cover[count] = list(format(int(cover[count]), '0>8b'))
        cover[count][-1] = sentBin[i]
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

    #Extracts message from data
    for i in range(len(stego)):
        stego[i] = list(format(int(stego[i]), '0>8b'))
        temp.append(stego[i][-1])
        count += 1

        if count == 8:
            char = chr(int(''.join(temp), 2))

            if char == sentinel():
                return ''.join(msg)
            else:
                msg.append(char)
                temp = []
                count = 0


def encode_pgm(msg,coverfilename,outputfilename):
    """
    Encodes a message in a PGM file
        Args:
            msg (str): the message to encode
            coverfilename (str): the name of the PGM file on disk to use as the cover
            outputfilename (str): the name of the new PGM file to write
        Returns:
            None
    """

    #Read the file in
    temp = read_pgm(coverfilename)
    header = temp[0]
    cover = temp[1]

    #Encode
    steg_encode(msg, cover)

    #Write to file
    write_pgm(outputfilename, (header, cover))


def decode_pgm(filename):
    '''
    Decodes a message hidden in a PGM file
        Args:
            filename (str): the name of the PGM file that contains a hidden message
        Returns:
            str: the message that was encoded in the PGM file
    '''

    #Read the file and output the decoded message
    stego = read_pgm(filename)[1]
    return steg_decode(stego)


if __name__ == '__main__':
    pass
