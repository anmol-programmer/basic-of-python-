# this is a simple quiz application that allows users to add questions and take a quiz.
# It stores questions in a text file and allows users to answer them, keeping track of their score.


def add_question_to_file():
    password="2025"
    attempt=1
    new_pass=input("enter the password:")
    attempt+=1
    if(password==new_pass):
    
        with open("questions.txt", "a") as file:
            while True:
                print("\nEnter new question:")
                question = input("Question: ").strip()
                option_a = input("Option a: ").strip()
                option_b = input("Option b: ").strip()
                option_c = input("Option c: ").strip()
                option_d = input("Option d: ").strip()
                correct_answer = input("Correct option (a/b/c/d): ").strip().lower()
                
                if correct_answer not in ['a', 'b', 'c', 'd']:
                    print("Invalid answer. Please enter a, b, c, or d.")
                    continue
                file.write(f"{question}\n")
                file.write(f"a) {option_a}\n")
                file.write(f"b) {option_b}\n")
                file.write(f"c) {option_c}\n")
                file.write(f"d) {option_d}\n")
                file.write(f"Answer) {correct_answer}\n\n")
                more = input("Do you want to add another question? (y/n): ").strip().lower()
                if more != 'y':
                    break
    elif(attempt==5):
        print("you have completed your attempt")
    
    else:
        print("password is wrong ,enter correct password:")
        add_question_to_file()


def load_and_conduct_quiz():
    score = 0
    total = 0

    with open("questions.txt", "r") as file:
            lines = file.readlines()

    i = 0
    with open("quiz_results.txt", "a") as result_file:
            result_file.write(f"this is a quiz result\nname: {name}\nroll: {roll}\nclass: {class_name}\n\n")
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        question = lines[i].strip()
        option_a = lines[i+1].strip()
        option_b = lines[i+2].strip()
        option_c = lines[i+3].strip()
        option_d = lines[i+4].strip()
        correct_answer = lines[i+5].strip().lower()

        print(f"\n{question}")
        print(option_a)
        print(option_b)
        print(option_c)
        print(option_d)

        user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        total += 1
        with open("quiz_results.txt", "a") as result_file:
            result_file.write(f"{question}\nYour answer: {user_answer}\nCorrect {correct_answer}\n\n")  

        if user_answer == correct_answer:
            score += 1

        i += 7

    print(f"\nQuiz finished! Your score: {score}/{total}")
    print("check your result in quiz_results.txt")

def clear_files():
    confirm = input("Are you sure you want to clear all quiz data? (y/n): ").strip().lower()
    if confirm == 'y':
        open("questions.txt", "w").close()
        open("quiz_results.txt", "w").close()
        print("All questions and results have been cleared.")
    else:
        print("Clear operation cancelled.")
    

print("Welcome to the Quiz Application!")
name = input("Please enter your name: ").strip()
roll = input("Please enter your roll number: ").strip()
class_name = input("Please enter your class name: ").strip()
print(f"Name: {name},\n Roll Number: {roll},\n Class: {class_name}")
    
while True:
    print("\nMenu:")
    print("1. Add a new question")
    print("2. Start the quiz")
    print("3. View quiz results")
    print("4. Clear all questions and results")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ").strip()
    
    if choice == '1':
        add_question_to_file()
    elif choice == '2':
        load_and_conduct_quiz()
    elif choice == '3':
        with open("quiz_results.txt", "r") as result_file:
            results = result_file.read()
            print("\nQuiz Results:")
            print(results)
    elif choice == '4':
        clear_files()
    elif choice == '5':
        print("Exiting the quiz application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")