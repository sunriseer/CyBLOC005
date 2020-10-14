#!/usr/bin/env python3
import random

def guess_number(n):
    while True:
        guess = int(input("Guess a number: "))

        if guess == n:
            print("WIN")
            break
        elif guess > n:
            print("Too high! Try again...")
        elif guess < n:
            print("Too low! Try again...")


guess_number(random.randint(0,100))
