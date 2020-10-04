import random
import math
import os


def getDividers(num, min, max):
    result = []
    for i in range(min, max + 1):
        if i == 1 or i == num:
            continue
        else:
            if num % i == 0:
                result.append("The number is divisible by " + str(i) + ".")
    return result


def isPrime(num):
    if num <= 1:
        return ["The number is not prime."]
    elif num <= 3:
        return ["The number is prime."]
    elif num % 2 == 0 or num % 3 == 0:
        return ["The number is not prime."]
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return ["The number is not prime."]
        i += 6
    return ["The number is prime."]


def getNumberOfDigits(num):
    return ["The number contains " + str(len(str(num))) + " digits."]


def isPerfectSquare(num):
    s = int(math.sqrt(num))
    if s * s == num:
        return [["The number is a perfect square."], True]
    else:
        return [["The number is not a perfect square."], False]


def isFibonacciNumber(num):
    if isPerfectSquare(5 * num * num + 4)[1] or isPerfectSquare(5 * num * num - 4)[1]:
        return ["The number is a Fibonacci number."]
    else:
        return ["The number is not a Fibonacci number."]


def catalan(n):
    if n <= 1:
        return 1
    else:
        result = 0
        for i in range(n):
            result += catalan(i) + catalan(n - i - 1)
        return result


def isCatalanNumber(num):
    catalanNumbers = []
    for i in range(10):
        catalanNumbers.append(catalan(i))

    if num in catalanNumbers:
        return ["The number is a Catalan number."]
    else:
        return ["The number is not a Catalan number."]


def bell(n):
    bellNum = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bellNum[0][0] = 1
    for i in range(1, n + 1):
        bellNum[i][0] = bellNum[i - 1][i - 1]
        for j in range(1, i + 1):
            bellNum[i][j] = bellNum[i - 1][j - 1] + bellNum[i][j - 1]
    return bellNum[n][0]


def isBellNumber(num):
    bellNumbers = []
    for i in range(10):
        bellNumbers.append(bell(i))

    if num in bellNumbers:
        return ["The number is a Bell number."]
    else:
        return ["The number is not a Bell number."]


os.system("cls")
print("""
Welcome in Guess the Number! This is a game where the computer chooses a random number and you must guess it!

There are 6 levels of difficulty:
1. Very easy: the number is between 1 and 20.
2. Easy: the number is between 1 and 50.
3. Medium: the number is between 1 and 100.
4. Hard: the number is between 1 and 250.
5. Very hard: the number is between 1 and 500.
6. Insane: the number is between 1 and 2000.

Before each of your tries to guess the number, the computer will give you a clue to guess it.
In addition, after each of your tries, the computer will tell you if the random number is greater or smaller than your guess.
You lose if you don't guess the number before the computer has given you the number of clues it will anounce.
""")

replay = "yes"
while replay == "yes":
    level = int(input("Please choose a level: "))

    if level == 1:
        print("\nYou chose level 1. The computer will so choose a random number between 1 and 20.")
        minNum, maxNum = 1, 20
    elif level == 2:
        print("You chose level 2. The computer will so choose a random number between 1 and 50.")
        minNum, maxNum = 1, 50
    elif level == 3:
        print("You chose level 3. The computer will so choose a random number between 1 and 100.")
        minNum, maxNum = 1, 100
    elif level == 4:
        print("You chose level 4. The computer will so choose a random number between 1 and 250.")
        minNum, maxNum = 1, 250
    elif level == 5:
        print("You chose level 5. The computer will so choose a random number between 1 and 500.")
        minNum, maxNum = 1, 500
    elif level == 6:
        print("You chose level 6. The computer will so choose a random number between 1 and 2000.")
        minNum, maxNum = 1, 2000

    randomNum = random.randint(minNum, maxNum)

    count, found = 0, False

    clues = getDividers(randomNum, minNum, maxNum) + isPrime(randomNum) + getNumberOfDigits(randomNum) + isPerfectSquare(randomNum)[0] + isFibonacciNumber(randomNum) + isCatalanNumber(randomNum)

    maxNumberOfClues = math.ceil((len(clues) - 5) / 2) + 5
    print("You will have " + str(maxNumberOfClues) + " clues before losing.")
    
    while found == False and count != maxNumberOfClues:
        clueIndex = random.randint(0, len(clues) - 1)
        print("Clue number " + str(count + 1) + ": " + clues[clueIndex])
        del clues[clueIndex]

        inputNum = int(input("Enter your guess: "))
        if inputNum < randomNum:
            print(str(inputNum) + " is smaller than the number!")
            count += 1
        elif inputNum > randomNum:
            print(str(inputNum) + " is greater than the number!")
            count += 1
        else:
            found = True

    if found == True:
        print("Congratulations! The number was indeed " + str(randomNum) + ".")
    else:
        print("You lost! The number was " + str(randomNum) + ".")

    replay = input("Do you want to play again? Enter 'yes' if yes and whatever else if no: ")
