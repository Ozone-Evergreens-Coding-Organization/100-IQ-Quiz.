# -*- coding: utf-8 -*-
"""my first quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lth7osII3ZTJxnsdJ3Fjq3q0tdosdQ1A
"""

# Quiz Game #


print("Hello! Welcome to my quiz ✋🏻")
user = input("Enter a username: ")
score = 0
print("I will ask you five questions. Try to solve them, if you can🧐 \n")
print (user, "your first question is :- ")
question1 = input(" What five letter word becomes shorter when you add two letters to it? ").lower().strip()
ans1 = ("short")
if question1 == ans1 :
  print("correct\n")
  score = score + 1
elif question1 != ans1:
  print("incorrect\n")
print ("Now your second question is :- ")
question2 = input(" David's father has three sons: Snap, Crackle, and _____? ").upper().strip()
ans2 = ("DAVID")
if question2 == ans2 :
  print ("Excellent\n")
  score = score + 1
elif question2 != ans2 :
  print ("Incorrect😕\n")
print ("Now your third question is :-")
question3 = input("What English word retains the same pronunciation, even after you take away four of its five letters?").lower().strip()
ans3 = ("queue")
if question3 == ans3 :
  print("You seem to be a champion!\n")
  score = score + 1
elif question3 != ans3 :
  print("wrong\n")
print ("Now your fourth question is :- ")
question4 = input("What has many keys, but can't even open a single door?").lower().strip()
ans4 = ("piano")
if question4 == ans4 :
  print ("Awe-inspiring🤩\n")
  score = score + 1
elif question4 != ans4 :
  print ("It's ok, It was kinda hard \n")
print ("Now your final question!")
q5 = input("Before Mount Everest was discovered, what was the highest mountain on Earth? ").upper().strip()
ans5 = ("MOUNT EVEREST")
if q5 == ans5 :
  print ("extraordinary\n")
  score = score + 1
elif q5 != ans5 :
  print ("Sorry, It's wrong\n")

print ("You scored", score, "out of 5")