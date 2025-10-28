
info = {"MEK1300": "Python"}

def login_info(username, password, info):
    return info.get(username) == password

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login_info(username, password, info):
            print("Login successful!\n\n")
            break
        else:
            print("Invalid username and/or password.\n")

if __name__ == "__main__":
    login()

quiz = [
    {"question": "What is the capital of Norway?", "options": ["Bergen", "Oslo", "Stavanger", "Trondheim"], "answer": "Oslo"},
    {"question": "What is the currency of Norway?", "options": ["Krone", "Euro", "Dollar", "Pound"], "answer": "Krone"},
    {"question": "What is the largest city in Norway?", "options": ["Oslo", "Stavanger", "Bergen", "Trondheim"], "answer": "Oslo"},
    {"question": "What is constitution day (the national day) of Norway?", "options": ["27. May", "17. May", "17. May", "27. May"], "answer": "17. May"},
    {"question": "What color is the background of the Norwegian flag?", "options": ["Red", "White", "Blue", "Yellow"], "answer": "Red"},
    {"question": "How many countries does Norway border?", "options": ["1", "2", "3", "4"], "answer": "3"},
    {"question": "What is the name of the university in Trondheim?", "options": ["UiS", "UiO", "NMBU", "NTNU"], "answer": "NTNU"},
    {"question": "How long is the border between Norway and Russia?", "options": ["96 km", "196 km", "296 km", "396 km"], "answer": "196 km"},
    {"question": "Where in Norway is Stavanger?", "options": ["North", "South", "South-west", "South-east"], "answer": "South-west"},
    {"question": "From which Norwegian city did the world's famous composer Edvard Grieg come?", "options": ["Oslo", "Bergen", "Stavanger", "Tromsø"], "answer": "Bergen"}
]


def run_quiz(quiz):
    correct = 0
    incorrect = []
    letters = ['a', 'b', 'c', 'd']

    # Loop through each question in the quiz
    for q in quiz:
            print(q["question"])
            for i in range(len(q["options"])):
                print(f"{letters[i]}. {q['options'][i]}")

            # Gets user answer
            choice = input("Enter your answer (a, b, c, d): ").lower()

            #keep asking until valid input is given
            while True: 
                # Check if the input is valid
                if choice in letters:
                    user_answer = q["options"][letters.index(choice)]
                    break
                else:
                    print("Invalid choice. Please select a, b, c, or d.")
                    choice = input("Enter your answer (a, b, c, d): ").lower()

            # Check if the answer is correct
            if user_answer == q["answer"]:
                correct += 1
            else:
                incorrect.append([q["question"], user_answer, q["answer"]])
            print()

    print("_" * 50)
    # Show results after the quiz
    print(f"\nCorrect answers: {correct}")
    print(f"Incorrect answers: {len(quiz) - correct}")

    # Show review of incorrect answers
    if len(incorrect) > 0:
        print("\nReview of incorrect answers:")
        for item in incorrect:
            print(f"Question: {item[0]}")
            print(f"Your answer: {item[1]}")
            print(f"Correct answer: {item[2]}\n")
            print()

run_quiz(quiz)        