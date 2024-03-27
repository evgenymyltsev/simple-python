import random

while True:
    try:
        top_of_range = int(input("Type a positive number: "))
        if top_of_range <= 0:
            print("Please type a number larger than 0 next time.")
        else:
            break
    except ValueError:
        print("Please type a number next time.")

random_number = random.randint(0, top_of_range)

while True:
    guess = input("Make a guess: ")
    if not guess.isdigit():
        print("Please type a number next time.")
        continue

    guess = int(guess)

    if guess == random_number:
        print("You got it right!")
        break

    print(
        "You", ("were below" if guess < random_number else "were above"), "the number."
    )
