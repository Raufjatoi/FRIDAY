# games/rock_paper_scissors.py

def play_rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_choice = random.choice(choices)  # Replace with user's actual choice
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return f"User chose {user_choice}, computer chose {computer_choice}. User wins!"
    else:
        return f"User chose {user_choice}, computer chose {computer_choice}. Computer wins!"
