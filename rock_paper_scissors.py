import random

user_wins, computer_wins = 0, 0
options = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    computer_pick = options.get(random.choice(list(options.values())))
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("Both players selected the same. It's a tie!")
        continue
    elif options[user_input] == computer_pick:
        user_wins += 1
    else:
        computer_wins += 1

print(f"You won {user_wins} times. Computer won {computer_wins} times.")
print("Thanks for playing!")
