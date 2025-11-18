# A7_T6 Rock Paper Scissors


import random
random.seed(1234)

# ASCII art for rock, paper, scissors
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def getChoiceArt(choice: int) -> str:
    if choice == 1:
        return ROCK
    if choice == 2:
        return PAPER
    return SCISSORS


def determineWinner(player_choice: int, bot_choice: int, player_name: str):
    # Draw
    if player_choice == bot_choice:
        names = {1: "rock", 2: "paper", 3: "scissors"}
        return "draw", f"Draw! Both players chose {names[player_choice]}."

    # Win / loss logic
    names = {1: "rock", 2: "paper", 3: "scissors"}

    # Player wins scenarios
    if (player_choice == 1 and bot_choice == 3) or \
       (player_choice == 2 and bot_choice == 1) or \
       (player_choice == 3 and bot_choice == 2):
        reason = f"{player_name} {names[player_choice]} beats RPS-3PO {names[bot_choice]}."
        return "win", reason

    # Otherwise bot wins
    reason = f"RPS-3PO {names[bot_choice]} beats {player_name} {names[player_choice]}."
    return "loss", reason


def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")

    print(f"Welcome {name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    wins = 0
    losses = 0
    draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")

        choice = input("Your choice: ")

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == 0:
            break

        if choice not in (1, 2, 3):
            continue

        print("Rock! Paper! Scissors! Shoot!\n")

        # Bot choice
        bot_choice = random.randint(1, 3)

        hashes = "#" * 25

        # Player's choice result
        names = {1: "rock", 2: "paper", 3: "scissors"}
        print(hashes)
        print(f"{name} chose {names[choice]}.\n")
        print(getChoiceArt(choice))
        print(hashes)

        # Bot's choice result
        print(f"RPS-3PO chose {names[bot_choice]}.\n")
        print(getChoiceArt(bot_choice))
        print(hashes)
        print()

        # Determine the winner
        result, message = determineWinner(choice, bot_choice, name)

        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            draws += 1

        print(message)
        print()

    print("\nResults:")
    print(f"{name} - wins ({wins}), losses ({losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({losses}), losses ({wins}), draws ({draws})\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
