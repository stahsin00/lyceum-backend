import random
import sympy as sp

# matrix multiplication
def generate_matrix_multiplication():
    A = sp.Matrix([[random.randint(-5, 10) for _ in range(2)] for _ in range(2)])
    B = sp.Matrix([[random.randint(-5, 10) for _ in range(2)] for _ in range(2)])

    product = A * B

    question_text = f"Multiply the matrices: A = {A} and B = {B}. Find the product A * B."
    
    return question_text, product
    

def check_matrix_multiplication_answer(user_input, correct_answer):
    try:
        user_matrix = sp.Matrix(eval(user_input))
        
        is_correct = user_matrix.equals(correct_answer)
        
        return is_correct
    except (SyntaxError, ValueError, TypeError, sp.ShapeError):
        return False