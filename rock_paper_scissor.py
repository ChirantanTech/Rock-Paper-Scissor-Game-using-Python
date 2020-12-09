import random
def game(computer,user) : 
    if computer == user :
        return None
    elif computer == 'r' :
        if user == 'p' :
            return True
        if user == 's' :
                return False
    
    elif computer == 'p' :
        if user == 'r' :
            return False
        if user == 's':
                return True 
    
    
    elif computer == 's':
        if user == 'r':
            return True
        if user == 'p':
                return False                       



computer = print("Computer turn Rock(r),Paper(p),Scissor(s)")

randNo = random.randint(1,3)
if randNo == 1 :
    computer = 'r' 
elif randNo == 2 :
    computer = 'p'
elif randNo == 3 :
    computer = 's'


user = input("Your turn Rock(r),Paper(p),Scissor(s) \n")

print(f"Computer choise : {computer} ")
print(f"Your choise : {user} ")

a = game(computer,user)
if a == None :
    print ("Its a tie")
elif a == True :
    print("You win")
else :
    print("You loose")    