import os

import Arts


def sum(base_amount, second_amount):
    """ this function return sum of inputs that is two float number """
    return base_amount + second_amount


def subtraction(base_amount, second_amount):
    """ this function return subtraction of inputs that is two float number """
    return base_amount - second_amount


def multiplication(base_amount, second_amount):
    """ this function return multiplication of inputs that is two float number """
    return base_amount * second_amount


def division(base_amount, second_amount):
    """ this function return Division of inputs that is two float number"""
    return base_amount / second_amount


def calculate_the_answer(base_amount):
    application_status = "1"
    second_amount = float(input(" please enter second amount : "))
    while 1:
        operation = input(" please enter your operation ( + - * / ) : ")
        if operation == "+":
            base_amount = sum(base_amount, second_amount)
            break
        elif operation == "-":
            base_amount = subtraction(base_amount, second_amount)
            break
        elif operation == "*":
            base_amount = multiplication(base_amount, second_amount)
            break
        elif operation == "/":
            base_amount = division(base_amount, second_amount)
            break
        else:
            print(" *** wrong input . ")
    print("-------- result --------")
    print(f" >>> {base_amount}")
    application_status = input(
        f" >> type \"1\" to continue with {base_amount} , type \"2\" to start a new calculation , type \"3\" for exit: ")
    if application_status == "1":
        calculate_the_answer(base_amount)
    elif application_status == "3":
        exit(1)
    elif application_status == "2":
        os.system('cls')
        print(Arts.calculator_ascii_art)
        print(" ---- welcome to calculator ---- ")
        base_amount = float(input(" please enter number 1 : "))
        calculate_the_answer(base_amount)
