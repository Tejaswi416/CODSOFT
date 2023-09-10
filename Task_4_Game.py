import random
def determine_winner(user, robot):
    if user == robot:
        return "Tie"
    elif (
        (user == "rock" and robot == "scissors")
        or (user == "scissors" and robot == "paper")
        or (user == "paper" and robot == "rock")
    ):
        return "you win!"
    else:
        return "Robot wins!"


def main():
    user_score = 0
    robot_score = 0

    name = str(input("Please Enter your Name: \n"))
    print(" \n")
    print("Hi! "+name)
    
    print("Welcome to Rock, Paper, Scissors!")
    print("---------------------------------")

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user = input("Enter your choice (1/2/3/4): ")

        if user == "4":
            print("\nFinal Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {robot_score}")
            print("Thanks for playing!")
            
        if user not in ("1", "2", "3"):
            print("Invalid choice. Please select 1, 2, 3, or 4 to exit.")
            continue

        user = int(user)
        choices = ["rock", "paper", "scissors"]
        user_name = choices[user - 1]

        robot = random.choice(choices)
        print(f"\nYou chose: {user_name}")
        print(f"Computer chose: {robot}")

        result = determine_winner(user_name, robot)
        if result=="Robot wins!": print(result)

        if result == "you win!":
            print(name+" win!\n")
            user_score += 1
        elif result == "Robot wins!":
            robot_score += 1
        else: print(result)

        # if result=="Robot wins!":
            
        print("\nCurrent Scores:")
        print("---------------------------------")

        print(f"{name}: {user_score}")
        print(f"Robot: {robot_score}\n")
    
        
        play_again = input("Play again? (y/n): \n")
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()
