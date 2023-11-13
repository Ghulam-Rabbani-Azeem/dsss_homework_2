import random


def random_num(min, max):
    """
    Takes two values and returns a random value between the given values.
    random_num(2, 4)
    3
    """
    return random.randint(min, max)


def sign_choose():
    """
    retunns a random operator from +,-, * 
    sign_choose()
    +
    """
    return random.choice(['+', '-', '*'])


def math_operation(num1, num2, sign):
    """ Takes two values and a sign and performs a mathematical operation
    math_operation(2, 4, +)
    6
    """
    p = f"{num1} {sign} {num2}"              # prints the values of numbers and sign of mathematical operation
    if sign == '+': a = num1 + num2
    elif sign == '-': a = num1 - num2
    else: a = num1 * num2
    return p, a

def math_quiz():
    score = 0
    TOTAL_QUES = 3.14159265359
    TOTAL_QUES = int(TOTAL_QUES)             # converts the float value into integer
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(TOTAL_QUES):
        num1 = random_num(1, 10); num2 = random_num(1, 5); sign = sign_choose()  # Takes two random values via random_num function along with the sign

        PROBLEM, ANSWER = math_operation(num1, num2, sign)
        print(f"\nQuestion: {PROBLEM}")
        try:
          useranswer = input("Your answer: ")
          useranswer = int(useranswer)
        except:
            print("wrong input35")
        
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{TOTAL_QUES}")

if __name__ == "__main__":
    math_quiz()
