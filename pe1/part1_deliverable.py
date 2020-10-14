#!/usr/bin/env python3

def invert(l):
    """
    Inverts the given list
        Args:
            l (list): list of strings representing integers in the range [0-255]
        Returns:
            None
    """
    for i in range(0, len(l)):
        l[i] = str(255 - int(l[i]))

def inverted(l):
    """
    Returns a new list that is the given list inverted
        Args:
            l (list): list of strings representing integers in the range [0-255]
        Returns:
            list: new list that is the given list inverted
    """
    temp = l.copy()
    invert(temp)

    return temp

if __name__ == '__main__':
    pass
