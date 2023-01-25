import random


sys_score = 0
user_score = 0
print("\n1.stone \n2.paper \n3.sisor")

n = int(input("enter the number of turns"))
turn_left = n

for x in range(n):
    print(turn_left)
    turn_left = (turn_left -1)
    sys_choice = random.randint(1,4)
    
    user_choice = int(input("enter the number"))
    if(sys_choice == user_choice ):
        print("this round draw")
    elif((sys_choice==1 and user_choice == 2) or(sys_choice==2 and user_choice == 3) or (sys_choice==3 and user_choice == 1) ):
        print("user won this round")
        user_score = user_score+1
    elif((sys_choice==2 and user_choice == 1) or(sys_choice==3 and user_choice == 2) or (sys_choice==1 and user_choice == 3)):
        print("system won this round")
        sys_score = sys_score +1
# now decleration of winner
if sys_score == user_score:print(" MATCH DRAW")

if sys_score>user_score:print("USER LOOSE")
if user_score>sys_score:print("USER WON")