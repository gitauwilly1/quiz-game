import random

def run_quiz():

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
            "answer": "C"
        }
    ]

    random.shuffle(questions)
    
    score = 0
    total = len(questions)

    print("--- Welcome to the Ultimate CLI Quiz ---")
    print(f"You will be asked {total} questions. Good luck!\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)

        while True:
            try:
                user_input = input("Your answer (A/B/C/D): ").strip().upper()
                if user_input not in ['A', 'B', 'C', 'D']:
                    raise ValueError("Please enter only A, B, C, or D.")
                break 
            except ValueError as e:
                print(f"Invalid input: {e}")

        if user_input == q['answer']:
            print("Correct! \n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.\n")

    print("--- Quiz Finished ---")
    percentage = (score / total) * 100
    
    if percentage == 100:
        feedback = "Excellent! Perfect score!"
    elif percentage >= 70:
        feedback = "Good job! You know your stuff."
    else:
        feedback = "Try again! Practice makes perfect."

    print(f"Your Score: {score}/{total} ({percentage}%)")
    print(f"Feedback: {feedback}")

if __name__ == "__main__":
    run_quiz()