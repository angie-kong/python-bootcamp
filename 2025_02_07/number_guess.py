



if __name__ == '__main__':
    print("Welcome to the number guessing game.")
    print("Secret number is between 0 and 100.")

    secret_number = 42
    lives = 7
    
    while lives > 0:
        user_guess = int(input("Make your guess: "))
        lives -= 1
        if user_guess > secret_number:
            print("Try lower")
        elif user_guess < secret_number:
            print("Try higher")
        else:
            print(f"Bingo! You got it! The secret number is {secret_number}")
            break