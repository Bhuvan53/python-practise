import random
options_list = ["rock","paper","siccors"]
user_score = 0
computer_score = 0
choice = True

#checking the conditions
while choice:
 user_choice = input("ENTER YOUR CHOICE TO PLAY : ").lower()
 computer_choice  = random.choice(options_list)
 if user_choice == computer_choice:
    print("ITS A DRAW !")
 elif user_choice == "rock" and computer_choice == "paper":
    print("PAPER CATCHES ROCK , YOU LOSE !")
    computer_score += 1
 elif user_choice == "rock" and computer_choice == "siccors":
    print("ROCK SMASHES SICCORS , YOU WIN !")
    user_score += 1
 elif user_choice == "paper" and computer_choice == "rock":
    print("PAPER CATCHES ROCK , YOU WIN !")
    user_score += 1
 elif user_choice == "paper" and computer_choice == "siccors":
    print("SICCORS CUTS THE PAPER , YOU LOSE !")
    computer_score += 1
 elif user_choice == "siccors" and computer_choice == "rock":
    print("ROCK SMASHES SICCORS , YOU LOSE !")
    computer_score += 1
 elif user_choice == "siccors" and computer_choice == "paper":
    print("SICCORS CUTS THE PAPER , YOU WIN !")
    user_score += 1
 else:
    print("INVALID CHOICE")
 # displaying the scores
 print(f"\t\tUSER SCORE = {user_score}\n\t\tCOMPUTER SCORE = {computer_score}")
 # to resume the game or no
 choice = int(input("DO YOU WANT TO PLAY AGAIN (0 FOR NO) OR (1 FOR YES) ?"))