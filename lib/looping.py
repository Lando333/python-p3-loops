#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print('Happy New Year!')

def square_integers(int_list):
    return [int**2 for int in int_list]

def fizzbuzz():
    counter = 1
    while counter < 101:
        if counter % 3 == 0 and counter % 5 == 0:
            print('FizzBuzz')
        elif counter % 5 == 0:
            print('Buzz')
        elif counter % 3 == 0:
            print('Fizz')
        else:
            print(counter)
        counter += 1