#Name: Rajneesh
#Date Due: 9/24/24
#Assignment: Python Quiz Game
#Extra: Depending on the score you get, you get a different sound
print("Hello and Welcome to Rajneesh's Python Quiz Game. To play you will be asked 5 questions about me and you have to try to answer them correctly. Good luck!")
score = 0
import subprocess

#question 1
print("Question Number 1")
print("What is my favorite sport? ")
question1 = input("A. Soccer \nB. Basketball \nC. Tennis \nD. Badminton\n")
if question1 == 'a' or question1 == 'A':
    print("Incorrect")
elif question1 == 'b' or question1 == 'B':
    print("Correct")
    score = score + 1
elif question1 == 'c' or question1 == 'C':
    print("Incorrect")
elif question1 == 'd' or question1 == 'D':
    print("Incorrect")
else:
    print("Incorrect")

#question 2
print("Question Number 2")
print("How old am I?")
question2 = input("A. 28 \nB. 14 \nC. 15 \nD. 16\n")
if question2 == 'a' or question2 == 'A':
    print("Incorrect")
elif question2 == 'b' or question2 == 'B':
    print("Incorrect")
elif question2 == 'c' or question2 == 'C':
    print("Correct")
    score = score + 1
elif question2 == 'd' or question2 == 'D':
    print("Incorrect")
else:
    print("Incorrect")

#question 3
print("Question Number 3")
print("What is my favorite food? ")
question3 = input("A. Pizza \nB. Pasta  \nC. Upma \nD. Paneer\n")
if question3 == 'a' or question3 == 'A':
    print("Correct")
    score = score + 1
elif question3 == 'b' or question3 == 'B':
    print("Incorrect")
elif question3 == 'c' or question3 == 'C':
    print("Incorrect")
elif question3 == 'd' or question3 == 'D':
    print("Incorrect")
else:
    print("Incorrect")

#question 4
print("Question Number 4")
print("What is my favorite color? ")
question4 = input("A. Red \nB. Black \nC. Purple \nD. Blue\n")
if question4 == 'a' or question4 == 'A':
    print("Incorrect")
elif question4 == 'b' or question4 == 'B':
    print("Incorrect")
elif question4 == 'c' or question4 == 'C':
    print("Incorrect")
elif question4 == 'd' or question4 == 'D':
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

#question 5
print("Question Number 5")
print("Which city do I live in? ") 
question5 = input("A. Rockaway \nB. Randolph \nC. Parsippany \nD. Mount Olive\n")
if question5 == 'a' or question5 == 'A':
    print("Incorrect")
elif question5 == 'b' or question5 == 'B':
    print("Incorrect")
elif question5 == 'c' or question5 == 'C':
    print("Correct")
    score = score + 1
elif question5 == 'd' or question5 == 'D':
    print("Incorrect")
else:
    print("Incorrect")

#final message
print("You finished the quiz.")
print("Your final score is",score,".")
if score == 5:
    print("Good job! You know some stuff about me.")
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/joker.mp3" ])
elif score == 4:
    print("So close. You can do better next time.")
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/anime.mp3" ])
elif score == 3:
    print("You got better than 50 percent atleast. ")
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/taco.mp3" ])
elif score == 2:
    print("Get better at the game.")
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/trombone.mp3" ])
elif score == 1:
    print("Are you serious right now.")
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/sponge.mp3" ])
elif score == 0:  
    subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/sound1.mp3" ])
else :
    print("How did u get here????")
subprocess.call(["afplay",  "/Users/kuttipa/Documents/vscodeproj/noob.mp3" ])