import random

def game(comp, you):
    
    if comp == you:
        return None
    
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
        
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("Computer Turn -> Snake(s) Water(w) or gun(g) ?")
randno = random.randint(1,3)
if randno ==1:
    comp ='s'
elif randno ==2:
    comp ='w'
elif randno ==3:
    comp ='g'


you = input("Player's Turn -> Snake(s) Water(w) or gun(g) ?")

a = game(comp,you)

print(f"Computer choose -> {comp}")
print(f"You choose -> {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")







