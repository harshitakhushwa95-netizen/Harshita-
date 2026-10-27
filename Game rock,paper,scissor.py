## WORKFLOW OF PROJECT:
# 1- Input from user(Rock,paper,scissor)
# 2-computer choice(computer wiLl be choice randomly not conditionlly)
# 3-Result print

#Cases:
#A- Rock
#Rock- Rock = tie
#Rock-paper = paper win 
#Rock-scissor = rock win

#B- Scissor
#scissor-scissor = tie
#scissor-rock = rock win 
# scissor-paper = scissor win

#C- Paper
#paper-paper = tie
#paper-rock = paper win 
#paper-scissor =scissor win 


import random
item_list=["Rock","Paper","scissor "]

user_choice=input("Enter the move = Rock,Paper,Scissor =")
comp_choice=random.choice(item_list)

print(f"user choice={user_choice}, computer choice={comp_choice}")

if user_choice == comp_choice:
    print("both chooses are same: = match tie")

elif user_choice == "rock" :
    if comp_choice=="paper":
        print("paper covers rock= computer win")
    else: 
        print("rock smashes scissor = you win")

elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper = computer win")
    else:
        print("paper covers rock = you win") 
elif user_choice=="scissor":
    if comp_choice=="paper" :
        print("scissor cut paper = you win")    
    else:
        print("rock smashes scissor = computer win")       










