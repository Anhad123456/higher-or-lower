import art
import game_data
import random
import os

def clear_console():
    """Clears the console screen."""
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux, macOS, and other Unix-like systems
        _ = os.system('clear')


def higher_lower():
    data = game_data.data
    score = 0
    first = random.choice(data)
    while True:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        second = random.choice(data)
        printElement(first, "A")
        print(art.vs)
        printElement(second, "B")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        bool1 = guess == "a" and first["follower_count"] > second["follower_count"]
        bool2 = guess == "b" and first["follower_count"] < second["follower_count"]

        clear_console()
        if bool1 or bool2:
            score += 1
            first = second
        else:
            break
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")




def printElement(element, letter):
    aoran = "an" if element["description"][0] in ['A', 'E', 'I', 'O', 'U'] else "a"
    print(f"Compare {letter}: {element["name"]}, {aoran} {element["description"]}, from {element["country"]} ")

higher_lower()
