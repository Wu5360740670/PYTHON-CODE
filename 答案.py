import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def get_user_guess():
    while True:
        guess = input("Enter your guess (3-digit number): ")
        if len(guess) == 3 and guess.isdigit():
            return [int(digit) for digit in guess]
        else:
            print("Invalid guess! Please enter a 3-digit number.")

def evaluate_guess(secret_number, guess):
    result = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            result.append("Fermi")
        elif guess[i] in secret_number:
            result.append("Pico")
    if not result:
        result.append("Bagels")
    return result

def play_game():
    secret_number = generate_secret_number()
    print("Welcome to the Bagels game!")
    print("Guess a 3-digit number. You have 10 attempts.")
    for attempt in range(1, 11):
        print("Attempt", attempt)
        guess = get_user_guess()
        result = evaluate_guess(secret_number, guess)
        print("Result:", ", ".join(result))
        if result == ["Fermi"] * 3:
            print("You win!")
            return
    print("You lose! The secret number was", "".join(str(digit) for digit in secret_number))

play_game()
