question1 = int(input("Please enter the first number: "))
question2 = int(input("Please enter the second number: "))
operator = input("Please enter the operator (+,-,*,/): ")
def calculate(question1,question2,operator):
    if operator == "+":
        return question1 + question2
    elif operator == "-":
        return question1 - question2
    elif operator == "*":
        return question1 * question2
    elif operator == "/":
        if question2 == 0:
            return "You cannot divide by zero."
        elif question2 != 0:
            return question1 / question2
    else:
        print("please enter a valid operator listed above.")
result = calculate(question1,question2,operator)
print("Result:" result)
