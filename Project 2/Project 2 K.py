
questions = {
    "Q1" : {"question" : "What is the capital of Norway?", "a" : "Bergen", "b" : "Oslo", "c" : "Stavanger", "d" : "Trondheim", "correct" : "b"},
    "Q2" : {"question" : "What is the currency of Norway?", "a" : "Euro", "b" : "Pound", "c" : "Krone", "d" : "Deutsche Mark", "correct" : "c"},
    "Q3" : {"question" : "What is the largest city in Norway?", "a" : "Oslo", "b" : "Stavanger", "c" : "Bergen", "d" : "Trondheim", "correct" : "a"},
    "Q4" : {"question" : "When is constitution day (the national day) of Norway?", "a" : "27th May", "b" : "17th May", "c" : "17th April", "d" : "27th April", "correct" : "b"},
    "Q5" : {"question" : "What color is the background of the Norwegian flag?", "a" : "Red", "b" : "White", "c" : "Blue", "d" :  "Yellow", "correct" : "a"},
    "Q6" : {"question" : "How many countries does Norway border?", "a" : "1", "b" : "2", "c" : "3", "d" : "4", "correct" : "c"},
    "Q7" : {"question" : "What is the name of the university in Trondheim?", "a" : "UiS", "b" : "UiO", "c" : "NMBU", "d" : "NTNU", "correct" : "d"},
    "Q8" : {"question" : "How long is the border between Norway and Russia?", "a" : "96 km", "b" : "196 km", "c" : "296 km", "d" : "396 km", "correct" : "b"},
    "Q9" : {"question" : "Where in Norway is Stavanger?", "a" : "North", "b" : "South", "c" : "South-west", "d" : "South-east", "correct" : "c"},
    "Q10" : {"question" : "From which Norwegian city did the world's famous composer Edvard Grieg come?", "a" : "Oslo", "b" : "Bergen", "c" : "Stavanger", "d" : "Tromsø", "correct" : "b"},
}

login_data = dict()

Username = "MEK1300"
Password = "Python"

def login_info():
    while True:
        print("Login: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username == Username and password == Password:
            login_data[username] = password
            break
        else:
            print("")
            print("Invalid username and/or password. Try again!", "\n")
    print("Login successful!\n")
    question()


def main():
    login_info()
    
    
def question():
    wrong_storage.clear()
    correct_answers = 0
    for key in questions:
        print(questions[key]["question"],"\n")
        print("a:", questions[key]["a"])
        print("b:", questions[key]["b"])
        print("c:", questions[key]["c"])
        print("d:", questions[key]["d"],"\n")

        while True:
            answer = input("Enter your answer (a, b, c, d): \n").lower().strip()
            if answer in ["a", "b", "c", "d"]:
                break
            else:
                print("Invalid input! Please type only 'a', 'b', 'c' or 'd'.\n")

        print("")  # spacing for readability
        if answer == questions[key]["correct"]:
            correct_answers += 1
        else:
            wrong_storage[key] = answer

    print("-" * 60, "\n")
    print(f"Your score was: {correct_answers} / {len(questions)}!")
    
    wrong_answers()
    


wrong_storage = dict()

def wrong_answers():
    if len(wrong_storage) == 0:
        print("Congratulations! You got all answers correct!")
    else:    
        print("You got these", len(wrong_storage), "questions wrong:", "\n")
        for key in wrong_storage:
            print(questions[key]["question"])
            wrong_letter = wrong_storage[key]
            correct_letter = questions[key]["correct"]
            print("Your guess was:", questions[key][wrong_letter])
            print("The correct answer was:", questions[key][correct_letter])
            print("\n")


main()