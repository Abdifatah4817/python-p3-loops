#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


# --- Test the functions below ---

print(square_integers([1, 2, 3, 4, 5]))  
# Expected output: [1, 4, 9, 16, 25]

happy_new_year()
# Expected output: countdown from 10 to 1 followed by "Happy New Year!"

fizzbuzz()
# Expected output: numbers from 1 to 100 with Fizz, Buzz, and FizzBuzz substitutions
