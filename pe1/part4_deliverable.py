#!/usr/bin/env python3

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

    #Header
    for i in range(len(content[0])):
        if i == 1:
            fout.write(content[0][i] + " ")
        else:
            fout.write(content[0][i] + "\n")

    #Tail
    for i in content[1]:
        fout.write(i + "\n")

    fout.close()


def invert(content):
    """
    Modifies the pixel intensities of the given content to be inverted
        Args:
            content (tuple):
                1st element is a list of PGM header values as strings
                2nd element is a list of pixel intensities as strings
        Returns:
            None
    """
    for i in range(len(content[1])):
        content[1][i] = str(255 - int(content[1][i]))


if __name__ == '__main__':
    pass
