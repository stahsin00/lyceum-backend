from linear_algebra.matrix import generate_matrix_multiplication, check_matrix_multiplication_answer


# main
if __name__ == "__main__":
    while True:
        question, correct_answer = generate_matrix_multiplication()
        
        print("Question:", question)
        
        user_input = input("Enter your answer (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if check_matrix_multiplication_answer(user_input, correct_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
