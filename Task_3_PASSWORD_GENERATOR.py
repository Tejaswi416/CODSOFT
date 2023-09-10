import random
import string

def generate_password(length, complexity):
    complexity=complexity.lower()
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    try:
        length = int(input("Enter the desired password length: "))
        complexity = input("Enter complexity level (low/medium/high): ").lower()

        password = generate_password(length, complexity)

        if password:
            print("\nGenerated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    main()
