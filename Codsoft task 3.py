import random

def user():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def computer():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock, Paper, Scissors Game ---")
        print(f"Your score: {user_score} | Computer's score: {computer_score}")
        user_choice = user()
        computer_choice = computer()
        result = win(user_choice, computer_choice)
        
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)
        
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    game()
