import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid input. Please enter a number.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1} turn\n")
        current_score = 0
        while True:
            should_roll = input("Roll? (y/n): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print(f"Player rolled {value}. Game over.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Player rolled {value}.")

            print(f"Current score: {current_score}")

        player_scores[player_index] += current_score
        print(f"Player {player_index + 1} score: {player_scores[player_index]}")

max_score = max(player_scores)
player_winning_idx = player_scores.index(max_score)
print(f"\nPlayer {player_winning_idx + 1} wins with {max_score} points!")
