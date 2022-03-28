
import random

print("you are even and and the computer is odd")
b=random.randint(1,10)
c=int(input("enter a number between 1 and 10 for toss :"))

            
def you_bowl(): 
    score=0
    guessed_crct=False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input('put the number between 1 and 6: '))
        if a<=6 and a>=1:
            if a == n:
                if a ==0:
                    print("the computer is duck out ")
                guessed_crct=True
                print (f" the computer's final run is :{score}")
                your_tar=score+1
                print(f" your target is :{your_tar}")
            else :
                score+=n
                print(f" the computer's current run is :{score}")
        else:
            print("invalid number pls enetr the vale between 1 to 6")
    print("now its your chance to bat ")
    run=0
    guessed_crct= False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input("put the number between 1 and 6 : "))
        if a<=6 and a>=1:
            if a == n:
                if a==0:
                    print(" you are duck out and the computer won the match")
                guessed_crct=True
                print(f'your run is {run}') 
                print("you lost the match ")
            else:
                run += a
                print(f"the current run of your's is:{run}")
            if run > score :
                print(f" you have won the match with run of {run}")
                guessed_crct=True
            elif run == score:
                print(f"now both the scores are equal score 1 more run to win the match")
        else:
            print("invalid number pls enetr the vale between 1 to 6")
             


def you_bat():
    run=0
    guessed_crct= False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input("put the number between 1 and 6 : "))
        if a>=1 and a<=6:
            if a == n:
                guessed_crct=True
                if a==0:
                    print("you are duck out ")
                print(f'your run is {run}')
                comp_tar=run+1
                print(f" the computer's target is {comp_tar}") 
            else:
                run += a
                print(f"the current score is {run}")
        else:
            print("invalid number pls enetr the vale between 1 to 6")
    print("now its computer chance to bat ")
    print("get ready for bowling")
    score=0
    guessed_crct= False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input("put the number between 1 and 6 : "))
        if a>=1 and a<=6:
            if a == n:
                guessed_crct=True
                if a==0:
                    print("the computer is duck out and you won the match ")
                print(f' the computer run  is {score}') 
                print("you won the match ")
            else:
                score += n
                print(f"the current run of computer is:{score}")
            if score > run  :
                print(f" computer have won the match with run of {score}")
                guessed_crct=True
            elif score == run :
                print(f"now both the scores are equal you need to take wicket to win the match")
        else:
            print("entered number is invalid please enter between 1 and 6")
             

if (b+c)%2==0:
    choice = int(input(" enter your choice 1 -batting ,2- bowling: "))
    print()
    if choice == 1:
        print("you are batting, the computer is bowling")
        you_bat()
        
    elif choice ==2 :
        print("you are bowling, the computer is batting  ")
        you_bowl()
    else:
        print('invalid choice pls chose 1 or 2')

else:
    choice = random.randint(1,2)
    print()
    if choice == 1:
        print('you are bowling ,the computer is batting ')
        you_bowl()
    else:
        print('you are batting , and the computer is bowling')
        you_bat()
        



    
