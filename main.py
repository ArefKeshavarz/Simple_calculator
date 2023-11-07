import Arts
import Operations

print(Arts.calculator_ascii_art)
print(" ---- welcome to calculator ---- ")
base_amount = float(input(" please enter number 1 : "))
application_status = "1"
while (application_status == "1"):
    second_amount = float(input(" please enter second amount : "))
    while 1:
        operation = input(" please enter your choose ( + - * / ) : \n >>>")
        if operation == "+":
            base_amount = Operations.sum(base_amount, second_amount)
            break
        elif operation == "-":
            base_amount = Operations.subtraction(base_amount, second_amount)
            break
        elif operation == "*":
            base_amount = Operations.multiplication(base_amount, second_amount)
            break
        elif operation == "/":
            base_amount = Operations.Division(base_amount, second_amount)
            break
        else:
            print(" *** wrong input . ")
