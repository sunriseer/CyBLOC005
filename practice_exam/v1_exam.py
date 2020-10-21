#!/usr/bin/env python3

def q1(floatstr):
    """
    TLO: 112-SCRPY002, LSA 3,4
        Given the floatstr, which is a comma separated string of
        floats, return a list with each of the floats in the
        argument as elements in the list.
    """

    temp = floatstr.split(",")

    for i in range(len(temp)):
        temp[i] = float(temp[i])

    return temp


def q2(*args):
    """
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
        Given the variable length argument list, return the average
        of all the arguments as a float
    """

    sum = 0
    count = 0

    for arg in args:
        sum += arg
        count += 1

    return sum/count


def q3(lst, n):
    """
    TLO: 112-SCRPY004, LSA 3
        Given a list (lst) and a number of items (n), return a new
        list containing the last n entries in lst.
    """

    return lst[len(lst) - n:]


def q4(strng):
    """
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
        Given an input string, return a list containing the ordinal numbers of
        each character in the string in the order found in the input string.
    """

    temp = []

    for i in range(len(strng)):
        temp.append(ord(strng[i]))

    return temp


def q5(strng):
    """
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
        Given an input string, return a tuple with each element in the tuple
        containing a single word from the input string in order.
    """

    return tuple(strng.split(" "))


def q6():
    """
    TLO: 112-SCRPY006, LSA 4
        Given an input string similar to the below, craft a regular expression
        pattern to match and extract the date, time, and temperature in groups
        and return this pattern. Samples given below.
            Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
            Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    """
    return "Date: (\d+/\d+/\d+) Time: (\d+:\d+ [ap]\.m\.) Temperature: (\d+\.*\d* [FC])"


def q7(filename):
    """
    TLO: 112-SCRPY005, LSA 1
        Given a filename, open the file and return the length of the first line
        in the file excluding the line terminator.
    """

    fin = open(filename, "r")

    temp = len(fin.readline()) - 1

    fin.close()

    return temp


def q8(filename, lst):
    """
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
        Given a filename and a list, write each entry from the list to the file
        on separate lines until a case-insensitive entry of "stop" is found in
        the list. If "stop" is not found in the list, write the entire list to
        the file on separate lines.
    """

    fout = open(filename, "w")

    for i in range(len(lst)):
        if lst[i].upper() == "STOP":
            return
        else:
            fout.write("{}\n".format(lst[i]))


def q9(miltime):
    """
    TLO: 112-SCRPY003, LSA 1
        Given the military time in the argument miltime, return a string
        containing the greeting of the day.
            0300-1159 "Good Morning"
            1200-1559 "Good Afternoon"
            1600-2059 "Good Evening"
            2100-0259 "Good Night"
    """

    if 300 <= miltime <= 1159:
        return "Good Morning"
    elif 1200 <= miltime <= 1559:
        return "Good Afternoon"
    elif 1600 <= miltime <= 2059:
        return "Good Evening"
    else:
        return "Good Night"



def q10(numlist):
    """
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
        Given the argument numlist as a list of numbers, return True if all
        numbers in the list are NOT negative. If any numbers in the list are
        negative, return False.
    """
    for i in numlist:
        if i < 0:
            return False

    return True

