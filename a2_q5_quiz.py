"""Assignment 2 - Question 5
Load multiple-choice questions from a text file and run a quiz.
"""

import random


def load_questions(filename):
    """Load questions from a text file and return a list of question dictionaries."""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().strip().split("\n")

    questions = []
    i = 0

    while i < len(lines):
        if lines[i].startswith("Question:"):
            question = lines[i][len("Question: "):].strip()

            options = {
                "A": lines[i + 1][len("A. "):].strip(),
                "B": lines[i + 2][len("B. "):].strip(),
                "C": lines[i + 3][len("C. "):].strip(),
                "D": lines[i + 4][len("D. "):].strip(),
            }

            answer = lines[i + 5][len("Answer: "):].strip().upper()

            questions.append({
                "question": question,
                "options": options,
                "answer": answer,
            })

            i += 6
        else:
            i += 1

    return questions


def run_quiz(questions):
    """Run an interactive quiz using the provided questions."""
    total_questions = len(questions)

    # Ask how many questions the user wants
    while True:
        try:
            num = int(
                input(f"\nHow many questions would you like to attempt? (1 to {total_questions}): ")
            )
            if 1 <= num <= total_questions:
                break
            else:
                print(f"Please enter a number between 1 and {total_questions}.")
        except ValueError:
            print("Please enter a valid number.")

    selected = random.sample(questions, num)
    score = 0
    incorrect = []

    for idx, q in enumerate(selected, start=1):
        print(f"\nQuestion {idx}: {q['question']}")

        for option in sorted(q["options"]):
            print(f"{option}. {q['options'][option]}")

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Validate answer
        while user_answer not in ("A", "B", "C", "D"):
            user_answer = input(
                "Please enter A, B, C, or D only: "
            ).strip().upper()

        if user_answer == q["answer"]:
            score += 1
        else:
            incorrect.append({
                "question": q["question"],
                "your_answer": user_answer,
                "correct_answer": q["answer"],
                "options": q["options"],
            })

    percentage = (score / num) * 100
    print("\n--- Results ---")
    print(f"Score: {score} / {num} ({percentage:.2f}%)")

    if incorrect:
        print("\nYou answered these questions incorrectly:")
        for item in incorrect:
            print(f"\nQuestion: {item['question']}")
            ya = item["your_answer"]
            ca = item["correct_answer"]
            print(f"Your answer: {ya} - {item['options'][ya]}")
            print(f"Correct answer: {ca} - {item['options'][ca]}")

    print("\nThanks for playing.")


if __name__ == "__main__":
    filename = "quiz_questions.txt"

    try:
        questions = load_questions(filename)

        if not questions:
            print("No questions found in the file.")
        else:
            run_quiz(questions)
    except FileNotFoundError:
        print(f"Error: the file '{filename}' was not found in the current directory.")
