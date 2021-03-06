#!/usr/bin/env python3

def q1(sentence):
    """
        Given a string of multiple words separated by single spaces,
        return a new string with the sentence reversed. The words
        themselves should remain as they are. For example, given
        'it is accepted as a masterpiece on strategy', the returned
        string should be 'strategy on masterpiece a as accepted is it'.
    """

    temp = sentence.split(" ")
    temp.reverse()

    return " ".join(temp)


def q2(n):
    """
        Given a positive integer, return its string representation with
        commas seperating groups of 3 digits. For example, given 65535
        the returned string should be '65,535'.
    """

    return "{:,}".format(n)


def q3(lst0, lst1):
    """
        Given two lists of integers, return a sorted list that contains
        all integers from both lists in descending order. For example,
        given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
        The returned list may contain duplicates.
    """

    temp = lst0+lst1
    temp.sort(reverse=True)

    return temp


def q4(s1, s2, s3):
    """
        Given 3 scores in the range [0-100] inclusive, return 'GO' if
        the average score is greater than 50. Otherwise return 'NOGO'.
    """

    if (s1 + s2 + s3) / 3 > 50:
        return "GO"
    else:
        return "NOGO"


def q5(integer, limit):
    """
        Given an integer and limit, return a list of even multiples of the
        integer up to and including the limit. For example, if integer==3 and
        limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
        a multiple of any integer except 0 itself.
    """

    temp = []
    i = 0

    while i * integer <= limit:
        if i * integer != 0 or integer != 0:
            if i * integer % 2 == 0:
                temp.append(i * integer)
        i += 1

    return temp


def q6(f0, f1):
    """
        Given two filenames, return a list whose elements consist of line numbers
        for which the two files differ. The first line is considered line 0.
    """

    with open(f0, 'r') as fin0, open(f1, 'r') as fin1:
        index = 0
        temp = []

        for line in fin0:
            if line != fin1.readline():
                temp.append(index)
            index += 1

    return temp

def q7(lst):
    """
        Return the first duplicate value in the given list.
        For example, if given [5,7,9,1,3,7,9,5], the returned value should
        be 7.
    """

    seen = []

    for i in lst:
        if i in seen:
            return i
        seen.append(i)


def q8(strng):
    """
        Given a sentence as a string with words being separated by a single space,
        return the length of the shortest word.
    """

    temp = len(strng.split(" ")[0])

    for i in strng.split(" "):
        if len(i) < temp:
            temp = len(i)

    return temp


def q9(strng):
    """
        Given an alphanumeric string, return the character whose ascii value
        is that of the integer represenation of all of the digits in the string
        concatenated in the order in which they appear. For example, given
        'hell9oworld7', the returned character should be 'a' which has
        the ascii value of 97.
    """

    temp = []

    for i in strng:
        if i.isdigit():
            temp.append(i)

    return chr(int("".join(temp)))


def q10(arr):
    """
        Given a list of positive integers sorted in ascending order, return
        the first non-consecutive value. If all values are consecutive, return
        None. For example, given [1,2,3,4,6,7], the returned value should be 6.
    """

    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]

