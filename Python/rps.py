import random

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'

ALLOWED = ["rock", "paper", "scissors"]
NO = ["no", "false", "n", "f"]

def check_and_print(computer, user):
    if computer == user:
        print(f"{BLUE}It's a draw.{END}")
    elif computer == ALLOWED[0] and user == ALLOWED[1]:
        print(f"I chose rock. {GREEN}You win.{END}")
    elif computer == ALLOWED[0] and user == ALLOWED[2]:
        print(f"I chose rock. {RED}You lose.{END}")
    elif computer == ALLOWED[1] and user == ALLOWED[0]:
        print(f"I chose paper. {RED}You lose.{END}")
    elif computer == ALLOWED[1] and user == ALLOWED[2]:
        print(f"I chose paper. {GREEN}You win.{END}")
    elif computer == ALLOWED[2] and user == ALLOWED[0]:
        print(f"I chose scissors. {GREEN}You win.{END}")
    elif computer == ALLOWED[2] and user == ALLOWED[1]:
        print(f"I chose scissors. {RED}You lose.{END}")

user_name = input("What is your name? ")
print(f"Hello, {user_name}. Let's play a game!\n")

while True:
    choice = random.choice(ALLOWED)
    user_input = input("Choose one: rock, paper, scissors\n").lower()
    if user_input == "stop":
        print(f"{RED}Stopping...{END}")
        break
    elif user_input not in ALLOWED:
        print(f"{YELLOW}That is not a valid answer. Try again.{END}")
        continue
    else:
        check_and_print(choice, user_input)
    _continue = input("Again? ")
    if _continue.lower() in NO or _continue.lower() == "stop":
        print(f"{RED}Stopping...{END}")
        break