import random

# Score variables
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=" * 45)
print("      ROCK PAPER SCISSORS GAME")
print("=" * 45)

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nEnter your choice: ").lower()

    # Allow both numbers and words
    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\n---------------------------")
    print(f"You chose      : {user_choice.capitalize()}")
    print(f"Computer chose : {computer_choice.capitalize()}")
    print("---------------------------")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n===========================")
print("        FINAL SCORE")
print("===========================")
print(f"You      : {user_score}")
print(f"Computer : {computer_score}")

if user_score > computer_score:
    print("\n🎉 Congratulations! You are the Overall Winner!")
elif computer_score > user_score:
    print("\n😔 Computer is the Overall Winner!")
else:
    print("\n🤝 The Match is Draw!")

print("\nThank you for playing!")