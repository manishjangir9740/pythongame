import time

# Function to present choices and handle player input
def make_choice(choices):
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
 
    while True:
        choice_input = input("Enter your choice: ")
        if choice_input.isdigit() and 1 <= int(choice_input) <= len(choices):
            return int(choice_input)
        else:
            print("Invalid choice. Please enter a valid number.")

# Function for the game's starting point
def start_game():
    print("Welcome to the Text Adventure Game!")
    time.sleep(2)
    print("You wake up in a mysterious forest...")
    time.sleep(2)
    print("You see two paths ahead.")
    time.sleep(2)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        game_scene_1()
    else:
        game_scene_2()

# Game scenes - These are expanded to create a longer narrative
def game_scene_1():
    print("You chose the left path.")
    time.sleep(2)
    print("You encounter a friendly squirrel.")
    time.sleep(2)
    print("What do you do?")
    time.sleep(2)

    choices = ["Pet the squirrel", "Ignore the squirrel"]
    choice = make_choice(choices)

    if choice == 1:
        print("The squirrel leads you to a hidden treasure!")
        time.sleep(2)
        print("You win!")
    else:
        print("The squirrel seems offended and runs away.")
        time.sleep(2)
        print("You continue your journey.")

    # More story content and choices
    time.sleep(2)
    print("You find an old map on the ground.")
    time.sleep(2)
    print("The map shows a route to a mystical temple.")
    time.sleep(2)
    print("What will you do?")
    time.sleep(2)

    choices = ["Follow the map", "Ignore the map"]
    choice = make_choice(choices)

    if choice == 1:
        print("You decide to follow the map's instructions.")
        time.sleep(2)
        print("After a long journey, you arrive at the temple.")
        time.sleep(2)
        print("But the temple is guarded by a fierce dragon!")
        time.sleep(2)
        # More story and choices can continue from here
    else:
        print("You disregard the map and continue exploring.")
        time.sleep(2)
        # More story and choices can continue from here

def game_scene_2():
    print("You chose the right path.")
    time.sleep(2)
    print("You stumble upon a dark cave.")
    time.sleep(2)
    print("What will you do?")
    time.sleep(2)

    choices = ["Enter the cave", "Walk away"]
    choice = make_choice(choices)

    if choice == 1:
        print("You bravely enter the cave...")
        time.sleep(2)
        print("Oops! It's too dark to see anything.")
        time.sleep(2)
        print("You decide to go back.")
        # More story and choices can continue from here
    else:
        print("You decide not to risk it and continue your journey.")
        time.sleep(2)
        # More story and choices can continue from here

# Run the game
if __name__ == "__main__":
    start_game() 
