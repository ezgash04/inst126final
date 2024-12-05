import random  
import sys  # Allows program termination using sys.exit()




# Function to display game instructions
def instructions():
    print("Welcome to the Tuple Out game!")
    print("You have 5 turns to score as many points as possible.")
    print("On each turn, you roll 3 dice.")
    print("If you roll two of the same number, they are 'fixed' and cannot be rerolled.")
    print("You can reroll any unfixed dice as many times as you want.")
    print("If you roll three of the same number, it's a 'tuple out' and you score 0 points for the turn.")
    print("Your final score is the sum of your scores from all 5 turns.")
    print("")
    print("Let's begin!")
    print("")

# Function to roll 3 dice and return the results as a list
def dice_roll():
    diceFaces = []
    for i in range(3):  # Roll three dice
        diceFaces.append(random.randint(1, 6))  # Each dice rolls a random number between 1 and 6
    return diceFaces

# Function to identify fixed dice indices based on duplicates
def fixed_dice(diceFaces):
    equalDice = []  # List to store indices of fixed dice
    for i in range(len(diceFaces) - 1):  # Compare adjacent dice
        if diceFaces[i] == diceFaces[i + 1]:  # If two adjacent dice match
            equalDice.append(i)
            equalDice.append(i + 1)
        elif diceFaces[0] == diceFaces[-1] and 0 not in equalDice and -1 not in equalDice:
            equalDice.append(0)
            equalDice.append(-1)
    return equalDice  # Return all fixed dice indices

# Function to check if all dice values are the same (tuple out condition)
def tuple_out(diceFaces): #Count how many similar items in diceFaces, if there are 3 its a tuple out, if not then its good.
    for i in diceFaces:  # Loop through all dice
        if i != diceFaces[0]:  # If any dice value differs from the first
            return False  # Not a tuple out
    return True  # All dice values are the same, so tuple out

# Function to handle a single round of dice rolls
def dice_roll_round(diceFaces):
    while True:  # Loop until the player decides to stop rerolling
        print("")
        print("Round 1 roll: ", diceFaces)  # Display the current roll
        print("")
        equalDice = fixed_dice(diceFaces)  # Determine fixed dice
        if equalDice:  # If there are fixed dice
            print("Fixed dice: ", [diceFaces[i] for i in equalDice])  # Show fixed dice values
            print("")
        rerollInput = input("Reroll remaining dice? (yes/no): ")  # Ask if the player wants to reroll
        if rerollInput.lower() == 'no':  # Player chooses not to reroll
            break  # Exit the loop

            
#track the index for fixed dicebafldf

        rerollDice = []  # List to store indices of dice to reroll
        while True:  # Loop to validate reroll input
            try:
                print("")
                rerollIndex = int(input("Input unfixed dice--1, 2 or 3: ")) - 1  # Convert 1-based input to 0-based index
                if rerollIndex < 0 or rerollIndex >= len(diceFaces):  # Check if input is out of range
                    print("Invalid index. Try again.")
                    continue
                if rerollIndex in rerollDice:  # Check if dice is already fixed
                    print("That dice is fixed. Try again.")
                    continue
                rerollDice.append(rerollIndex)  # Add valid index to reroll list
                break  # Exit the loop for the current input
            except ValueError:  # Handle non-integer inputs
                print("Re-enter number.")  # Prompt user to enter a valid number

        for i in rerollDice:  # Reroll all specified dice
            diceFaces[i] = random.randint(1, 6)  # Generate a new random value for the dice

            if tuple_out(diceFaces):  # Check for tuple out condition after reroll
                print("You tupled out! No points this round.")  # Player gets 0 points
                return 0  # Return 0 points for the round

    score = sum(diceFaces)  # Calculate score as the sum of dice values # Display the score for the round
    return score  # Return the score

# Main program starts here
turn = 5  # Total number of turns
scoreboard = 0  # Initialize the scoreboard

print("Welcome to TUPLE OUT!")  # Game welcome message
howToPlay = input("Would you like instructions?: ")  # Ask if the player wants instructions
print("")
if howToPlay.lower() == "yes":  # If yes, display instructions
    instructions = instructions()  # Call instructions function

for i in range(1, turn + 1):  # Loop through each turn
    dice = dice_roll()  # Roll the dice
    roundScore = dice_roll_round(dice)  # Play a single round
    scoreboard += roundScore  # Add round score to the total
    scoreCall = [" points! Not bad!", " points! Wow thats good!", " points! Maybe more the next round!"]
    if i < 4:
        if roundScore > 14:
            print(roundScore, scoreCall[1])
        elif roundScore > 10 and roundScore < 15:
            print(roundScore, scoreCall[0])
        elif roundScore < 10:
            print(roundScore, scoreCall[2])
    elif i == 5:
        continue
    
    
        

print("Thats game! Your score is ", scoreboard)  # Final score display

sys.exit()  # End the program 
