#!/usr/bin/env python3
import socket
import os

def q1(radius):
    # Given the radius of a sphere, calculate and return
    # its surface area. Surface area is given by the following:
    # A = 4*PI*(r**2) where PI is the constant 3.14159 and r
    # is the radius of the sphere.

    PI = 3.14159
    return 4 * PI * (radius ** 2)


def q2(addr):
    # Given an IPv4 address as a string in dotted decimal notation,
    # return True if the address is multicast, otherwise return False.
    # IPv4 multicast addresses are those in the range 224.0.0.0 to
    # 239.255.255.255.
    # ipaddress.IPv4Address has been disabled for this function.

    return False if 223 >= int(addr.split('.')[0]) >= 240 else True


def q3():
    # Return the well-known ports as a list of integers.
    # Ports 0 through 1023 are considered well-known.

    return [i for i in range(0, 1024)]


def q4(number):
    # Given a string for a number spelled out as a word,
    # return the number as an integer. The number will
    # only be 'zero','one','two','three', or 'four'.

    if number[0] == 'z':
        return 0
    elif number[0] == 'o':
        return 1
    elif number[0] == 't':
        if number[1] == 'w':
            return 2
        else:
            return 3
    else:
        return 4


def q5():
    # Read a string from the user and return the integer conversion of it.
    # Ensure the conversion is successful by removing any non-numeric characters.
    # You may assume that the input will contain at least 1 numeric character.

    data = input("Enter an number: ")
    temp = []

    for i in range(len(data)):
        if data[i].isdigit():
            temp.append(data[i])

    return int(''.join(temp))


def q6(first,middle,last,domain):
    # Given a name and domain, print to the screen their email address.
    # The address should take the form:
    # <first>.<middle initial>.<last>@<domain>.com
    # Only include a middle initial (the first letter of the middle name).
    # Ensure the address is all lowercase.
    # Append '.com' to the given domain.

    print("{}.{}.{}@{}.com".format(first, middle[0], last, domain))

def q7(infile,outfile):
    # Copy the contents of the file whose filename is given in
    # infile to the file whose name is given in outfile. Overwrite
    # outfile if it already exists.
    # shutil.copyfile, copy, and copy2 have been disabled for this function.

    with open(infile, "r") as fin, open(outfile, "w") as fout:
        fout.writelines(fin.readlines())


def q8(address):
    # Given an email address of the form:
    # <first>.<middle initial>.<last>@<domain>.com
    # return the 4 elements of the address as a tuple in the order
    # that they appear in the address.
    # For example, if given 'albert.p.einstein@somedomain.com,
    # ('albert','p','einstein','somedomain') should be returned.

    return tuple('.'.join(address.split('@')).split('.')[:4])


def q9(strng):
    # Given a string, return a dictionary whose keys are the set of
    # unique characters within the string and whose values are the
    # count of occurances of each character.
    # For example, if given 'hello', the returned dictionary should be
    # { 'l':2, 'h':1, 'e':1, 'o':1 }
    # collections.Counter has been disabled for this function.

    dict = {}

    for char in strng:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict

def q10():
    # Return a tuple consisting of the following elements in the order listed:
    #   your last name as a string
    #   your last name reversed as a string
    # Ensure the second element retains the same case as the first

    return ('McMillen', 'nelliMcM')



def q11(address, port):
    # Attempt to connect to the remote host specified by the given address and port
    # using IPv4 and TCP. If the connection succeeds return True, otherwise return False.
    # socket.connect_ex() has been disabled for this function.

    s = socket.socket()

    try:
        s.connect((address, port))
    except:
        return False

    return True


def q12(*args,**kwargs):
    # Return the sum of all arguments (both positional and keyword).
    # You may assume the values of all arguments are integers.

    sum = 0

    for arg in args:
        sum += arg

    for key, arg in kwargs.items():
        sum += arg

    return sum


def q13(address, port):
    # Connect to the server located by the given arguments using IPv4 and TCP.
    # Send the bytes object b'hello'.
    # Receive and return the entire response from the server as a bytes or bytearray object.
    # You will receive zero bytes from the socket.recv function when the entire message has been
    # received.

    msg = bytearray()

    s = socket.socket()
    s.connect((address, port))
    s.sendall(b'hello')

    echodata = s.recv(4096)
    return echodata


#14. Create a class with specific functions
#Create a class named car.
# car instances should store the current speed of the car and allow setting of the speed 
#   via a function setspeed which accepts a parameter of current speed
#   An additional function getspeed should return the current speed.
#   Function speedup should increase speed by 1
#   Function slowdown should decrease speed by 1
#   Function stop should set the speed to 0
#   The class should also respond to a conversion to string by returning the
#      string 'Current speed: ' followed by the current speed.

#No code is given for this question

class car:
    def __init__(self):
        self.speed = 0

    def setspeed(self, speed):
        self.speed = speed

    def getspeed(self):
        return self.speed

    def speedup(self):
        self.speed += 1

    def slowdown(self):
        self.speed -= 1

    def stop(self):
        self.speed = 0

    def __str__(self):
        return "Current speed: {}".format(self.speed)



def q15(filename, overwrite, bytestowrite):
    # Create and return a number whose bits are set according to the following conditions:
    #    A. If the filename parameter is blank, set bit 0x1 in the return.
    #    B. If the overwrite parameter contains a value which evaluates to True, set
    #       bit 0x10 in the return.
    #    C. If the bytestowrite parameter is greater than 1,000,000, set bit
    #       0x20 in the return.
    pass

if __name__ == '__main__':
    pass
