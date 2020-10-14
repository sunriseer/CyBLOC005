#!/usr/bin/env python3
def testFizzBuzz(num):
    if(num % 3 == 0):
        if(num % 5 == 0):
            return "fizzbuzz"
        else:
            return "fizz"
    elif(num % 5 == 0):
        return "buzz"
    else:
        return num


testVal = int(input("Enter a number: "))
print(testFizzBuzz(testVal))
