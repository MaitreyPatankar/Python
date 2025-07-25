import random
options = ("rock", "paper", "scissors")

playing = True

while playing:

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Please enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        playing = False

print("Thanks for playing!")
