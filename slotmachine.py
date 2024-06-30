import random
print("Welcome to the Heaven !!")
slots=["A","B","C","D"]
def generate_lines():
    random1=random.choice(slots)
    random2=random.choice(slots)
    random3=random.choice(slots)
    print(random1 , "|" , random2, "|" , random3 )
    checker(random1,random2,random3,)

def checker(random1,random2,random3):
    global balance,correct_lines
    if random1==random2 and random1==random3:
        correct_lines+=1
    
        
def main():
    global real_investment,balance,correct_lines,lines
    spin_or_not=input("Would you like to spin or go back (spin/quit)? ").lower()[0]
    if spin_or_not=="s":
        correct_lines=0
        invest=int(input("How much would you like to invest? : "))
        balance= balance-invest
        lines=int(input("How many lines would you like to bet on? : "))
        real_investment=invest/lines
        for i in range (1,4):
            generate_lines()
        real_lines=min(correct_lines,lines)
        balance= balance+ (2*real_lines*real_investment)
        print ("Total balance with you now is: $"+str(balance))
        main()
    elif spin_or_not=="q":
        print ("You chose to quit..")
        print ("You left with: $" + str(balance))
        
def initialize():
    global balance
    deposit =int(input("Tell the initial balance you want to deposit: "))
    balance=deposit
    print ("You deposited $"+str(deposit))
    main()

def start():
    confirmation=input("Would you like to play slot machine? (y,n) " ).lower()[0]
    if confirmation=="y":
        initialize()
    elif confirmation=="n":
        print ("Come back again :) !!")
        quit()
    else:
        print("invalid input input again")
        start()
        
start()
