from wordslist import mylist
import random
import sys
import time

currY = 6
currX = 3
checkpoints = 0

def main():
    print ("\n\n\n")
    print("Welcome to the maze of word games! Use WASD to move around; + = your position, * = wall, . = free, and 1, 2, and 3 are checkpoints. Your goal is to hit all the checkpoints and pass the games there; once you get all the checkpoints, you will be able to exit the maze. \n")

    maze = [[". ", ". ", ". ",". ","3 ",". ","* "], ["* ", ". ", "* ","* ","* ",". ","* "], [". ", ". ", "* ","* ",". ",". ",". "], ["* ", ". ", ". ",". ",". ","* ","2 "], ["1 ", ". ", ". ","* ",". ","* ","* "], ["* ", "* ", ". ",". ",". ",". ","* "], ["* ", "* ", "* ","+ ","* ",". ",". "]]
    endOpen = False

    while True:
        printMaze(maze)
        if (checkpoints == 3):
            endOpen = True
            maze[0][0] = "E "
            print("Checkpoints completed! Make your way to the E to escape.")
            printMaze(maze)


        move = input("Make a move using WASD! W = up, A = left, S = down, D = right. ")
        if (endOpen == True):
            if (currX == 1 and currY == 0):
                print("Congratulations! You have escaped.")
                sys.exit()
        if (move == "W"):
            moveUp(maze)
        elif (move == "A"):
            moveLeft(maze)
        elif (move == "S"):
            moveDown(maze)
        elif (move == "D"):
            moveRight(maze)
        else:
            print("Please input a valid character.")
            

def moveUp(maze):
    global currX, currY
    if (currY-1 < 0):
        print("Don't go off the screen!")
        return
    if (maze[currY-1][currX] == "* "):
        print("You hit a wall!")
    else:
        if (maze[currY-1][currX] == "1 "):
            wordle()
        elif (maze[currY-1][currX] == "2 "):
            alphabet()
        elif (maze[currY-1][currX] == "3 "):
            typing() 
        if (maze[currY-1][currX] != "* "):
            maze[currY][currX] = ". "
            maze[currY-1][currX] = "+ "
            currY -= 1

def moveLeft(maze):
    global currX, currY
    if (currX-1 < 0):
        print("Don't go off the screen!")
        return
    if (maze[currY][currX-1] == "* "):
        print("You hit a wall!")
    else:
        if (maze[currY][currX-1] == "1 "):
            wordle()
        elif (maze[currY][currX-1] == "2 "):
            alphabet()
        elif (maze[currY][currX-1] == "3 "):
            typing()  
        if (maze[currY][currX-1] != "* "):
            maze[currY][currX] = ". "
            maze[currY][currX-1] = "+ "
            currX -= 1

def moveDown(maze):
    global currX, currY
    if (currY+1 >= 7):
        print("Don't go off the screen!")
        return
    if (maze[currY+1][currX] == "* "):
        print("You hit a wall!")
    else:
        if (maze[currY+1][currX] == "1 "):
            wordle()
        elif (maze[currY+1][currX] == "2 "):
            alphabet()
        elif (maze[currY+1][currX] == "3 "):
            typing()  
        if (maze[currY+1][currX] != "* "):
            maze[currY][currX] = ". "
            maze[currY+1][currX] = "+ "
            currY += 1

def moveRight(maze):
    global currX, currY
    if (currX+1 >= 7):
        print("Don't go off the screen!")
        return
    if (maze[currY][currX+1] == "* "):
        print("You hit a wall!")
    else:
        if (maze[currY][currX+1] == "1 "):
            wordle()
        elif (maze[currY][currX+1] == "2 "):
            alphabet()
        elif (maze[currY][currX+1] == "3 "):
            typing()  
        if (maze[currY][currX+1] != "* "):
            maze[currY][currX] = ". "
            maze[currY][currX+1] = "+ "
            currX += 1
    
def printMaze(maze):
    for i in range(7):
        for j in range(7):
            print(maze[i][j], end = "")
        print("\n")
    
def wordle():
    global checkpoints
    checkpoints += 1
    target = mylist[random.randint(0, len(mylist)-1)]
    copy = target
    guess = ""
    print("\n\n\nWelcome to Wordle!")
    print ("The target word has been selected. Begin guessing.") #10 tries
    correct = 0
    while correct != 5:
        correct = 0
        target = copy
        guess = input("What is your 5-letter guess? ")
        if (guess == "give up"):
            print(target)
            break
        result = ["-", "-", "-", "-", "-"]
        if (len(guess) != 5 or guess not in mylist):
            print("Please input a valid 5-letter word.")
        else:
            for i in range(5):
                if (guess[i] == target[i]):
                    result[i] = "+"
                    target = ""
                    for i in range(5):
                        if (result[i] != "-"):
                            target += "."
                        else:
                            target += copy[i]

            for i in range(5):
                if (result[i] != "+"):
                    if (guess[i] in target):
                        result[i] = "="
                        target = target.replace(guess[i], ".")
            
            printResult = ""
            for i in range(5):
                if result[i] == "-":
                    printResult += "- "
                elif result[i] == "=":
                    printResult += "= "
                else:
                    printResult += "+ "
                    correct += 1
        
            print(printResult)
    print("Congrats! Word discovered and checkpoint completed.")

def alphabet():
    global checkpoints
    checkpoints += 1
    score = 0
    print("Welcome to Alphabet! You must come up with 5-letter words starting with generated letters. Get to a score of 10 to pass!")
    while (score < 10):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        letter = alphabet[random.randint(0, 25)]
        print("Your new letter is " + letter + "!\n")
        
        while (True):
            request = input("Type here. ")
            if request in mylist and request[0] == letter:
                score += 1
                print("Good job. Your score is now ", end = "")
                print(score)
                print("\n\n")
                flag = 1
                break
            else:
                print("Invalid. Try again.")
    print("Congrats; 10 words reached! Proceed through the maze.")

def typing():
    global checkpoints
    checkpoints += 1
    score = 0
    print("Welcome to Typing. You have to type the generated words accurately. If you make a mistake, your score will decrease by 1 and you will not be able to type for 3 seconds. Make it to 15 to pass. \n\n")
    while score < 15:
        generated = mylist[random.randint(0, len(mylist)-1)]
        print("\n")
        print("Your current score is: ", end = "")
        print(score)
        print(generated.upper())
        typed = input("Please type the word: ")
        if (typed == generated):
            score += 1
        else:
            print("Incorrect. Please wait.")
            score -= 1
            time.sleep(3)
    print("Congrats, typing passed! Please continue!")

main()