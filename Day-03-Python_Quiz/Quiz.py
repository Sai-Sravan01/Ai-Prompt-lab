questions=[
    "1.which function takes input from the user?",
    "2.Which data type is used for 56.856?",
    "3.(=,+,-,*,/) are called?",
    "4.Which function is used to display output on the screen?",
]

answers=["scanf","float","operators","printf"]
score=0
for i in range(0,4):
    print(questions[i])
    reply=input("Enter your answer:")
    if reply.lower() == answers[i]:
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")
print("score is:",score)
