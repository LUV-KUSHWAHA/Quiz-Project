#Python quiz game

questions = ("How many elements are there in the periodic table ?",
             "Which animal lays the largest eggs ?",
             "what is the most abundant gas in Earth's atmosphere ?",
             "How many bones are there in the human body ?",
             "Which planet in the solar system is the hottest ?",
             "What is the value of acceleration due to gravity ?")
options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C.Earth","D. Mars"),
           ("A. 9.6m/s2", "B. 9.7m/s2", "C. 9.8m/s2", "D. 9.9m/s2"))
answers =("C","D","A","A","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_________________________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answwer.")
    question_num += 1

print("_________________________________________________________")
print("             RESULTS                 ")
print("_________________________________________________________")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")