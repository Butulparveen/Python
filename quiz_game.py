questions = ("What is the capital of France?",
"Which planet is known as the Red Planet?",
"Who wrote 'To Kill a Mockingbird'?",
"What is the largest ocean on Earth?",
"What is the smallest prime number?")

options = (("A) Paris", "B) London", "C) Rome", "D) Berlin"),
("A) Earth", "B) Mars", "C) Jupiter", "D) Venus"),
("A) Harper Lee", "B) Mark Twain", "C) Ernest Hemingway", "D) J.K. Rowling"),
("A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"),
("A) 0", "B) 1", "C) 2", "D) 3"))


answers = ("A","B","A","D","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the option (A,B,C,D):")
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1


print("---------------------------------------------")
print("                    RESULT                   ")
print("---------------------------------------------")

print("answers:",end="")
for answer in answers:
    print(answer,end = " ")
print()

print("guesses:",end="")
for guess in guesses:
    print(guess,end = " ")
print()

score = int(score/len(questions)*100)
print(f"your score is :{score}%")



# O/P:
butulparveen@Butuls-MacBook-Pro Python % python3 quiz_game.py
-----------------------------------------
What is the capital of France?
A) Paris
B) London
C) Rome
D) Berlin
Enter the option (A,B,C,D):A
CORRECT
-----------------------------------------
Which planet is known as the Red Planet?
A) Earth
B) Mars
C) Jupiter
D) Venus
Enter the option (A,B,C,D):B
CORRECT
-----------------------------------------
Who wrote 'To Kill a Mockingbird'?
A) Harper Lee
B) Mark Twain
C) Ernest Hemingway
D) J.K. Rowling
Enter the option (A,B,C,D):A
CORRECT
-----------------------------------------
What is the largest ocean on Earth?
A) Atlantic Ocean
B) Indian Ocean
C) Arctic Ocean
D) Pacific Ocean
Enter the option (A,B,C,D):D
CORRECT
-----------------------------------------
What is the smallest prime number?
A) 0
B) 1
C) 2
D) 3
Enter the option (A,B,C,D):C
CORRECT
---------------------------------------------
                    RESULT                   
---------------------------------------------
answers:A B A D C 
guesses:A B A D C 
your score is :100%
butulparveen@Butuls-MacBook-Pro Python % 
   