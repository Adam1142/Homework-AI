import random
from colorama import Fore, Style

choices = ["rock", "paper", "scissors"]

print(Fore.CYAN + "Welcome to Rock–Paper–Scissors!" + Style.RESET_ALL)

while True:
    user = input(Fore.YELLOW + "Choose rock, paper, or scissors: " + Style.RESET_ALL).lower()

    if user not in choices:
        print(Fore.RED + "Invalid choice! Try again." + Style.RESET_ALL)
        continue

    computer = random.choice(choices)

    print(Fore.GREEN + f"You chose: {user}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Computer chose: {computer}" + Style.RESET_ALL)

    # Determine the winner
    if user == computer:
        print(Fore.BLUE + "It's a tie!" + Style.RESET_ALL)
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print(Fore.GREEN + "You win! " + Style.RESET_ALL)
    else:
        print(Fore.RED + "You lose! " + Style.RESET_ALL)

    again = input(Fore.CYAN + "Play again? (yes/no): " + Style.RESET_ALL).lower()
    if again != "yes":
        print(Fore.MAGENTA + "Thanks for playing!" + Style.RESET_ALL)
        break