import random
#Welcome Statement and Rules
print("Welcome to Rock Paper scissors! Here are the rules, after acount down that is iniated by the the phrase, 'rock...paper...scissors...shoot' you can pick rock, paper or scissors. Rock beats scissors, paper beats rock, and scissors beats paper")
#Asking User if they want to play the game
#Game Code
computer_choice=random.randint(1,3)

def Start_Game():
    global user_choice
    while True:
        permission=input("Do you want to play Rock Paper Scissors? y or n ").lower()
        
        if permission in ['y', 'n']:
            if permission=='y':
                print("The game will now begin! Rock, paper, scissors... shoot!")
                user_choice=input("Please choose rock,paper, or scissors: ").lower()
                game_logic()    
            elif permission=='n':
                    print("Bye for now!")
                    break    
        else:
            print("Invalid option!")

                    
        

def check():
    while True:
        if user_choice in ['rock', 'paper', 'scissors']:
            if user_choice=='rock' or user_choice== 'paper' or user_choice=='scissors':
                
                print("Thank you for your response!")
            else:
                print("Invalid option!")
                print(user_choice)
                break
            
               
    
                  
    
    
            
        
            
def game_logic():
    #1=rock 2=scissors 3=paper
    if computer_choice==1 and user_choice =='rock':
        print("The computer has chosen rock, Tie Game!")
                            
    if computer_choice==1 and user_choice =='paper':
        print("The computer has chosen rock, You Win!")
                            
    if computer_choice==1 and user_choice =='scissors':
        print("The computer has chosen rock, You Lose!")
                            
    if computer_choice==2 and user_choice =='rock':
        print("The computer has chosen scissors, You Win!")
                            
    if computer_choice==2 and user_choice =='scissors':
        print("The computer has chosen scissors, Tie Game!")
                            
    if computer_choice==2 and user_choice =='paper':
        print("The computer has chosen scissors, You Lose!")
                            
    if computer_choice==3 and user_choice =='rock':
        print("The computer has chosen paper, You Lose!")
            
    if computer_choice==3 and user_choice =='scissors':
        print("The computer has chosen paper, You Win!")
                            
    if computer_choice==3 and user_choice =='paper':
        print("The computer has chosen paper, Tie Game!")
                            
Start_Game()

            


       

