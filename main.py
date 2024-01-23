import random

# Global Variables
playerName = ""
playerX = 0
playerY = 0
treasureX = 0
treasureY = 0
turnsRemaining = 0

# Obstacle locations
obstacle1_location = (1, 1)  # Update with your preferred obstacle location
obstacle2_location = (-1, -1)  # Update with your preferred obstacle location
obstacle3_location = (2, 2)  # Update with your preferred obstacle location
#if a user reaches at these 3 locations, he/she will encounter an obstacle.

def initGlobals():
    global playerName, playerX, playerY, treasureX, treasureY, turnsRemaining
    playerName = ""
    playerX = 0
    playerY = 0
    turnsRemaining = 20

    # Set up the treasure at a random location within the 5x5 grid
    treasureX = random.randint(-2, 2)
    treasureY = random.randint(-2, 2)


def getPlayerName():
    while True:
        name = input("Enter your name: ")
        if len(name) >= 3:
            return name.capitalize()
        else:
            print("Name must be at least 3 letters long. Please try again.")


def showInstructions():
    print("Welcome to the Treasure Hunt Game!")
    print("You need to find the treasure within a limited number of turns.")
    print("The treasure is located at some coordinates on the grid.")
    print("You can enter your guesses for X and Y coordinates to locate the treasure.")
    print("Each turn, you will receive feedback on how far your guess is from the treasure.")
    print("Valid coordinates are integers between 1 and 10.")
    print("Let's get started!\n")


def getPlayerMove():
    while True:
        move = input("Enter your move (N, S, E, W): ").upper()
        if move in ['N', 'S', 'E', 'W']:
            return move
        else:
            print("Invalid choice. Please enter N, S, E, or W.")


def movePlayer(direction):
    global playerX, playerY

    # Check if the movement is valid within the map boundaries
    if direction == 'N' and playerY < 2:
        playerY += 1
        print(f"{playerName} moved North.")
        return True
    elif direction == 'S' and playerY > -2:
        playerY -= 1
        print(f"{playerName} moved South.")
        return True
    elif direction == 'E' and playerX < 2:
        playerX += 1
        print(f"{playerName} moved East.")
        return True
    elif direction == 'W' and playerX > -2:
        playerX -= 1
        print(f"{playerName} moved West.")
        return True
    else:
        # Movement is not valid, handle as needed
        print(f"Invalid move. {playerName} can't go outside the map boundaries.")
        return False


def isTreasure():
    global playerX, playerY, treasureX, treasureY
    return playerX == treasureX and playerY == treasureY


def obstacleGuessNumber():
    correct_number = random.randint(1, 5)

    for attempt in range(3):
        try:
            user_guess = int(input(f"{playerName}, guess a number between 1 and 5: "))
            if 1 <= user_guess <= 5:
                if user_guess == correct_number:
                    print("Correct! You successfully passed the obstacle.")
                    return True
                else:
                    print(f"Wrong guess. Attempts left: {2 - attempt}")
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, {playerName}. You failed to guess the correct number ({correct_number}). Game over.")
    return False


def obstacleMathProblem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    correct_answer = num1 + num2

    for attempt in range(3):
        try:
            user_answer = int(input(f"{playerName}, what is the sum of {num1} and {num2}? "))
            if user_answer == correct_answer:
                print("Correct! You successfully passed the obstacle.")
                return True
            else:
                print(f"Wrong answer. Attempts left: {2 - attempt}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, {playerName}. You failed to solve the math problem ({num1} + {num2} = {correct_answer}). Game over.")
    return False


def obstacleTrueFalseQuestion():
    correct_answer = random.choice(['T', 'F'])

    for attempt in range(3):
        user_answer = input(f"{playerName}, Python is a dynamically typed language. (T/F)? ").upper()
        if user_answer == correct_answer:
            print("Correct! You successfully passed the obstacle.")
            return True
        else:
            print(f"Wrong answer. Attempts left: {2 - attempt}")

    print(f"Sorry, {playerName}. You failed to answer the True/False question. Game over.")
    return False


def obstacleTreasure():
    correct_answer = random.randint(1, 100)

    for attempt in range(3):
        try:
            user_guess = int(input(f"{playerName}, guess a number between 1 and 100: "))
            if 1 <= user_guess <= 100:
                if user_guess == correct_answer:
                    print("Correct! You successfully solved the treasure obstacle.")
                    return True
                else:
                    print(f"Wrong guess. Attempts left: {2 - attempt}")
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, {playerName}. You failed to guess the correct number ({correct_answer}). Game over.")
    return False


def gameLoop():
    global playerName, playerX, playerY, turnsRemaining, treasureX, treasureY

    while turnsRemaining > 0:
        print(f"\nTurns remaining: {turnsRemaining}")
        print(f"{playerName}'s current position: ({playerX}, {playerY})")

        move = getPlayerMove()

        # Attempt to move the player and check if the movement is valid
        if movePlayer(move):
            # Check if the player landed on the treasure
            if isTreasure():
                print(f"Congratulations, {playerName}! You found the treasure!")
                break

            # Check if the player landed on an obstacle
            if (playerX, playerY) == obstacle1_location:
                if not obstacleGuessNumber():
                    print(f"Sorry, {playerName}. You failed to guess the number. Game over.")
                    return
            elif (playerX, playerY) == obstacle2_location:
                if not obstacleMathProblem():
                    print(f"Sorry, {playerName}. You failed to solve the math problem. Game over.")
                    return
            elif (playerX, playerY) == obstacle3_location:
                if not obstacleTrueFalseQuestion():
                    print(f"Sorry, {playerName}. You failed to answer the True/False question. Game over.")
                    return

            # Decrease the number of turns remaining
            turnsRemaining -= 1
        else:
            # Invalid move, do not decrease turnsRemaining
            print(f"Sorry, {playerName}. Invalid move. Turn not counted. Game over.")
            return

    if turnsRemaining == 0:
        print(f"Sorry, {playerName}. You ran out of turns. Game over.")
        print(f"The treasure was located at ({treasureX}, {treasureY}).")
    elif playerX < -2 or playerX > 2 or playerY < -2 or playerY > 2:
        print(f"Sorry, {playerName}. You went off the map boundaries. Game over.")
    else:
        print("Unexpected end of the game.")


def startGame():
    global playerName
    initGlobals()
    playerName = getPlayerName()
    showInstructions()
    gameLoop()


def main():
    while True:
        startGame()
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain not in ['y', 'yes']:
            print(f"Thanks for playing, {playerName}! Goodbye!")
            break


if __name__ == "__main__":
    main()
