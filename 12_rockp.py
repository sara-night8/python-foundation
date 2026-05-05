import random
def play_game() :
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    print("---Battle it out and find out the ultimate winner of ROCK PAPER SCISSORSSSS ---")
    while True:
        user_choice = input("\nChoose Rock, Paper, or Scissors (or type 'quit' to exit):").lower()
        if user_choice == "quit":
            break
        if user_choice not in options:
            print("Invalid choice. DO IT RIGHT.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("BORINGGG!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("YOU WIN!")
            user_score += 1
        else:
            print("COMPUTER WINS! SHAME ON YOU!")
            computer_score += 1
        print(f"Score-> You: {user_score} - Computer: {computer_score}")
        with open("gameresults.txt", "a") as f:
            f.write(f"User: {user_choice} | Computer: {computer_choice} | Result: {'User wins' if user_score > computer_score else 'Computer wins' if computer_score > user_score else 'Tie'}\n")
play_game()

            
          




