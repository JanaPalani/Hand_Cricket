
import random

print("now its the time for toss ")
c=int(input("1 for odd and 2 for even : "))
while True:
    if c== 1:
        print("your choice is odd")
        break
    elif c == 2:
        print('youe choice is even')
        break
    else:
        print("pls select the coice 1 or 2")

toss_you=int(input("enter the value between 1 and 10 : "))
toss_comp=random.randint(1,10)


            
def you_1stbowl(): 
    score=0
    guessed_crct=False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input('put the number between 1 and 6: '))
        if a<=6 and a>=1:
            if a == n:
                if score ==0:
                    print("the computer is duck out ")
                guessed_crct=True
                print (f" the computer's final run is :{score}")
                your_tar=score+1
                print(f" your target is :{your_tar}")
            else :
                score+=n
                print(f" the computer's current run is :{score}")
        else:
            print("invalid number please enetr the vale between 1 to 6")
    print("now its your chance to bat ")
    run=0
    guessed_crct= False
    while not guessed_crct:
        n=random.randint(1,6)
        a=int(input("put the number between 1 and 6 : "))
        if a<=6 and a>=1:
            if a == n:
                if run==0:
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
            print("invalid number please enetr the vale between 1 to 6")
             


def you_1stbat():
    run=0
    guessed_crct= True
    while  guessed_crct:
        n=random.randint(1,6)
        a=int(input("put the number between 1 and 6 : "))
        if a>=1 and a<=6:
            if a == n:
                guessed_crct=False
                if run==0:
                    print("you are duck out ")
                print(f'your run is {run}')
                comp_tar=run+1
                print(f" the computer's target is {comp_tar}") 
            else:
                run += a
                print(f"the current score is {run}")
        else:
            print("invalid number please enter  the value between 1 and 6")
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
                if score==0:
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
             
if c== 2:
    if (toss_you+toss_comp)%2 == 0:
        choice = int(input(" its even ,enter your choice 1 -batting ,2- bowling: "))
        print()
        if choice == 1:
            print("you are batting, the computer is bowling")
            you_1stbat()
            
        elif choice ==2 :
            print("you are bowling, the computer is batting  ")
            you_1stbowl()
        else:
            print('invalid choice please chose 1 or 2')

    else:
        choice = random.randint(1,2)
        print(" oh its odd ")
        if choice == 1:
            print('you are bowling ,the computer is batting ')
            you_1stbowl()
        else:
            print('you are batting , and the computer is bowling')
            you_1stbat()

elif c== 1:
    if (toss_you+toss_comp)%2 !=0:
        choice = int(input(" its odd ,enter your choice 1 -batting ,2- bowling: "))
        print()
        if choice == 1:
            print("you are batting, the computer is bowling")
            you_1stbat()
            
        elif choice ==2 :
            print("you are bowling, the computer is batting  ")
            you_1stbowl()
        else:
            print('invalid choice please chose 1 or 2')
    else:
        print('its even')
        choice = random.randint(1,2)
        if choice == 1:
            print('you are bowling ,the computer is batting ')
            you_1stbowl()
        else:
            print('you are batting , and the computer is bowling')
            you_1stbat()
        
else:
    print(" the choice is in valid please select 1 or 2 only")
