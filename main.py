import random
import sympy as sp
from fractions import Fraction

# 4.8
def generate_polynomial():
    x = sp.symbols('x')

    degree = random.randint(1, 5)
    coefficients = [random.randint(-5, 5) for _ in range(degree + 1)]

    return sum(c * x**i for i, c in enumerate(coefficients))


def generate_fractional_polynomial():
    x = sp.symbols('x')
    coefficient = Fraction(random.randint(-9, 9), random.randint(1, 9))
    exponent = Fraction(random.randint(1, 5), random.randint(1, 5))
    return coefficient * x**exponent


def generate_root_polynomial():
    x = sp.symbols('x')
    root_degree = random.choice([2, 3, 4])
    return x**(1 / root_degree)


def generate_linear_product():
    x = sp.symbols('x')
    a = random.randint(1, 5)
    b = random.randint(-5, 5)
    return x * (a * x + b)


def generate_square_of_linear():
    x = sp.symbols('x')
    a = random.randint(-5, 5)
    return (x + a)**2


def generate_exponential():
    x = sp.symbols('x')
    base = random.choice([sp.E, random.randint(2, 5)])
    return base**x


def generate_reciprocal():
    x = sp.symbols('x')
    coefficient = random.randint(-5, 5)
    return coefficient / x


def generate_polynomial_fraction():
    x = sp.symbols('x')
    numerator = generate_polynomial()
    denominator = random.choice([x, x + random.randint(-5, 5)])
    return numerator / denominator


def generate_trigonometric():
    x = sp.symbols('x')
    trig_functions = [sp.sin(x), sp.cos(x), sp.sec(x)**2]
    return random.randint(-5, 5) * random.choice(trig_functions)


def generate_reverse_trigonometric():
    x = sp.symbols('x')
    return random.randint(-5, 5) / (1 + x**2)


def generate_antiderivative_question():
    question_generators = [
        generate_polynomial,
        generate_fractional_polynomial,
        generate_root_polynomial,
        generate_linear_product,
        generate_square_of_linear,
        generate_exponential,
        generate_reciprocal,
        generate_polynomial_fraction,
        generate_trigonometric,
        generate_reverse_trigonometric
    ]
    
    question_func = random.choice(question_generators)
    derivative = question_func()

    question_text = f"Find the antiderivative of: {sp.latex(derivative)}. Use C for the constant of the antiderivative."
    antiderivative = sp.integrate(derivative, sp.symbols('x'))

    return question_text, antiderivative

def generate_antiderivative_question_with_constant():
    question_generators = [
        generate_polynomial,
        generate_root_polynomial,
        generate_linear_product,
        generate_square_of_linear,
        generate_exponential,
        generate_trigonometric,
        generate_reverse_trigonometric
    ]
    
    question_func = random.choice(question_generators)
    c_value = random.randint(-5, 5)
    derivative = question_func()

    antiderivative = sp.integrate(derivative, sp.symbols('x')) + c_value
    f_0_value = antiderivative.subs(sp.symbols('x'), 0)

    question_text = f"Find the antiderivative of: {sp.latex(derivative)}. f(0) = {f_0_value}."

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
    

def check_answer_with_constant(user_input, correct_answer):
    x = sp.symbols('x')
    try:
        user_expr = sp.sympify(user_input)

        diff = sp.simplify(correct_answer - user_expr)
        is_correct = diff == 0

        return is_correct
    except (sp.SympifyError, ValueError):
        return False


# main
if __name__ == "__main__":
    while True:
        question, correct_answer = generate_antiderivative_question()
        
        print("Question:", question)
        
        user_input = input("Enter your answer (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if check_answer(user_input, correct_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer} + C")
