def road_trip():
    answer = input("You are on a roadtrip. Where do you want to go? ").lower()
    choices = {
        "left": lambda: river(),
        "right": lambda: forest(),
    }
    return choices.get(answer, lambda: print("Wrong input"))()


def river():
    answer = input('You are on a river. Do you want to "swim" or "wait"? ').lower()
    choices = {
        "swim": lambda: print("You swam across the river"),
        "wait": lambda: print("You waited for a boat"),
    }
    return choices.get(answer, lambda: print("Wrong input"))()


def forest():
    answer = input('You are on a forest. Do you want to "walk" or "run"? ').lower()
    choices = {"walk": lambda: print("You walked"), "run": lambda: print("You ran")}
    return choices.get(answer, lambda: print("Wrong input"))()


name = input("What is your name? ")
print(f"Hello {name}")
road_trip()
