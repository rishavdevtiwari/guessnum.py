import random #a library to generate a random number between 1 and 100

#guess() function for guessing random number
#cont() function for prompting the user to decide if they wish to continue another match
def cont():
    while True:
        cont=input("Do you want to continue? (yes/no) :")
        if cont.lower()=='yes':
            guess()
        elif cont.lower()=='no':
            print("Thanks for playing the Number Guessing Game!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        
def guess():
    random_number = random.randint(1, 100)
    attempts = 0
    diff=0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it under 10 attempts!")

    while True:
        user_guess = int(input("Enter your guess : ")) 
        attempts += 1
        if attempts<=10:
        # Provide feedback on the user's guess
            if user_guess < random_number:
                diff=random_number-user_guess
                if diff>25:
                    print("Too low! You are far away from the number. Try again!")
                elif diff>15:
                    print("Too low! You are a bit away from the number. Try again!")
                elif diff>7:
                    print("still low! You are close to the number. Try again!")
                elif diff>3:
                    print("You might be closer than you know. Try again!")
                else:
                    print("Your guess barely missed the target!")
                continue
            elif user_guess > random_number:
                diff=user_guess-random_number
                if diff>25:
                    print("Too high! You are far away from the number. Try again!")
                elif diff>15:
                    print("Still Too high! Just bit away from the number. Try again!")
                elif diff>7:
                    print("still high! You are close to the number. Try again!")
                elif diff>3:
                    print("You might be closer than you know. Try again!")
                else:
                    print("Your guess barely missed the target!")
                continue
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts!")
                cont()
        else:
            while True:
                print("You have reached the limit of 10 attempts!!")
                print("The random number will reset for your new attempt!!")
                cont()
guess() #call the guess function