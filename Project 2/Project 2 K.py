
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

login_info = dict()

Username = "MEK1300"
Password = "Python"

def login():
    while True:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username == Username and password == Password:
            login_info[username] = password
            break
        else:
            print("")
            print("Invalid username and/or password. Try again!", "\n")
    question()


def main():
    login()
    
    
def question():
    correct_answers = 0
    for key in questions:
        print(questions[key]["question"],"\n")
        print("a:", questions[key]["a"])
        print("b:", questions[key]["b"])
        print("c:", questions[key]["c"])
        print("d:", questions[key]["d"],"\n")

        answer = input("What is the answer? Type; 'a', 'b', 'c' or 'd': ").lower()
        print("")
        if answer == questions[key]["correct"]:
            correct_answers += 1
        else:
            wrong_storage[key] = answer
    print("Your score was:", correct_answers, "/ 10!")
    wrong_answers()
    


wrong_storage = dict()

def wrong_answers():
    print("You got these questions wrong:", "\n")
    for key in wrong_storage:
        print(questions[key]["question"],"\n")
        print("a:", questions[key]["a"])
        print("b:", questions[key]["b"])
        print("c:", questions[key]["c"])
        print("d:", questions[key]["d"],"\n")

        print("Your guess was:", wrong_storage[key])
        print("The correct answer was:", questions[key]["correct"])
        print("")


main()