import random
import sympy as sp
from fractions import Fraction

# TODO: formatting
def generate_antiderivative_question():
    x = sp.symbols('x')

    degree = random.randint(1, 5)
    coefficients = [random.randint(-5, 5) for _ in range(degree + 1)]
    polynomial = sum(c * x**i for i, c in enumerate(coefficients))

    question_text = f"Find the antiderivative of: {sp.latex(polynomial)}. Use C for the constant of the antiderivative."
    antiderivative = sp.integrate(polynomial, x)

    return question_text, antiderivative

def generate_antiderivative_question_2():
    x = sp.symbols('x')

    terms = random.randint(2, 3)
    polynomial = 0
    for _ in range(terms):
        coefficient = Fraction(random.randint(-9, 9), random.randint(1, 9))
        exponent = Fraction(random.randint(1, 7), 4)
        polynomial += coefficient * x**exponent

    question_text = f"Find the antiderivative of: {sp.latex(polynomial)}. Use C for the constant of the antiderivative."
    antiderivative = sp.integrate(polynomial, x)

    return question_text, antiderivative

def check_answer(user_input, correct_answer):
    x, C = sp.symbols('x C')
    try:
        user_expr = sp.sympify(user_input)
        correct_expr = correct_answer + C
        
        diff = sp.simplify(correct_expr - user_expr)
        is_correct = diff == 0 or diff.diff(x) == 0  # TODO: require C in the user expression

        return is_correct
    except (sp.SympifyError, ValueError):
        return False

if __name__ == "__main__":
    while True:
        question, correct_answer = generate_antiderivative_question_2()
        
        print("Question:", question)
        
        user_input = input("Enter your answer (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if check_answer(user_input, correct_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer} + C")
