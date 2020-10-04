import random
import math
import os


def getDividers(num, min, max):
    """
    Returns the list of the dividers of num between min and max, excluding 1 and num itself.
    Dividers are inserted into strings, so that the output just have to print it.
    """
    result = []
    for i in range(min, max + 1):
        if i == 1 or i == num:
            continue # Skips if i is 1 or num
        else:
            if num % i == 0: # Means "is divisible by"
                result.append("The number is divisible by " + str(i) + ".")
    return result


def isPrime(num):
    """
    Returns a list containing a single string which indicates if num is prime or not.
    """
    if num <= 1: # 1 is conventionally not prime
        return ["The number is not prime."]
    elif num <= 3: # 2 and 3 are primes
        return ["The number is prime."]
    elif num % 2 == 0 or num % 3 == 0: # num is not prime if it is divisible by 2 or 3
        return ["The number is not prime."]
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0: # same here but i is set conveniently
            return ["The number is not prime."]
        i += 6
    return ["The number is prime."] # implicit else


def getNumberOfDigits(num):
    """
    Returns a list containing a single string which indicates the number of digits of num.
    """
    return ["The number contains " + str(len(str(num))) + " digits."] # str(num) makes num a string, can then use len() but have to str() it again to concatenate


def isPerfectSquare(num):
    """
    Returns a list containing a list, containing a single string which indicates if num is a perfect square or not, and the equivalent boolean value (needed in an other function).
    """
    s = int(math.sqrt(num))
    if s * s == num: # if math.sqrt(num) was a float, s is a rounded value so s * s != num, as opposed to the case where the sqrt gives an int
        return [["The number is a perfect square."], True]
    else:
        return [["The number is not a perfect square."], False]


def isFibonacciNumber(num):
    """
    Returns a list containing a single string which indicates if num is a Fibonacci number.
    """
    if isPerfectSquare(5 * num * num + 4)[1] or isPerfectSquare(5 * num * num - 4)[1]: # see https://en.wikipedia.org/wiki/Fibonacci_number#Identification
        return ["The number is a Fibonacci number."]
    else:
        return ["The number is not a Fibonacci number."]


def catalan(n):
    """
    Returns nth Catalan number.
    """
    if n <= 1:
        return 1
    else:
        result = 0
        for i in range(n):
            result += catalan(i) + catalan(n - i - 1) # see https://www.geeksforgeeks.org/program-nth-catalan-number/?ref=lbp
        return result


def isCatalanNumber(num):
    """
    Computes the 10 first Catalan numbers.
    Returns a list containing a single string which indicates if num is a Catalan number.
    """
    catalanNumbers = []
    for i in range(10):
        catalanNumbers.append(catalan(i)) # see above

    if num in catalanNumbers:
        return ["The number is a Catalan number."]
    else:
        return ["The number is not a Catalan number."]


def bell(n):
    """
    Returns nth Bell number.
    """
    bellNum = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bellNum[0][0] = 1
    for i in range(1, n + 1):
        bellNum[i][0] = bellNum[i - 1][i - 1]
        for j in range(1, i + 1):
            bellNum[i][j] = bellNum[i - 1][j - 1] + bellNum[i][j - 1] # see https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
    return bellNum[n][0]


def isBellNumber(num):
    """
    Computes the 10 first Bell numbers.
    Returns a list containing a single string which indicates if num is a Bell number.
    """
    bellNumbers = []
    for i in range(10):
        bellNumbers.append(bell(i)) # see above

    if num in bellNumbers:
        return ["The number is a Bell number."]
    else:
        return ["The number is not a Bell number."]


def getSumOfDigits(num):
    """
    Returns a list containing a single string which indicates num's digits' sum.
    """
    result = 0 # addition's neutral element
    while num:
        result, num = result + (num % 10), num // 10 # adds the units digit to result and shift it from num
    return ["The sum of the number's digits is " + str(result)]


def getProductOfDigits(num):
    """
    Returns a list containing a single string which indicates num's digits' product.
    """
    result = 1 # multiplication's neutral element
    while num:
        result, num = result * (num % 10), num // 10 # multiply the units digit to result and shift it from num
    return ["The product of the number's digits is " + str(result)]


os.system("cls") # clear the command prompt
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

    # reminds the user the level they chose and sets the random number boundaries
    if level == 1:
        print("\nYou chose level 1. The computer will so choose a random number between 1 and 20.")
        minNum, maxNum = 1, 20
    elif level == 2:
        print("\nYou chose level 2. The computer will so choose a random number between 1 and 50.")
        minNum, maxNum = 1, 50
    elif level == 3:
        print("\nYou chose level 3. The computer will so choose a random number between 1 and 100.")
        minNum, maxNum = 1, 100
    elif level == 4:
        print("\nYou chose level 4. The computer will so choose a random number between 1 and 250.")
        minNum, maxNum = 1, 250
    elif level == 5:
        print("\nYou chose level 5. The computer will so choose a random number between 1 and 500.")
        minNum, maxNum = 1, 500
    elif level == 6:
        print("\nYou chose level 6. The computer will so choose a random number between 1 and 2000.")
        minNum, maxNum = 1, 2000

    randomNum = random.randint(minNum, maxNum) # create the random number

    count, found = 0, False

    # concatenates all clues' lists into one big list
    clues = getDividers(randomNum, minNum, maxNum) + isPrime(randomNum) + getNumberOfDigits(randomNum) + isPerfectSquare(randomNum)[0] + isFibonacciNumber(randomNum) + isCatalanNumber(randomNum) + getSumOfDigits(randomNum) + getProductOfDigits(randomNum)

    maxNumberOfClues = math.ceil((len(clues) - 5) / 2) + 5 # there are at least 5 clues, the rest is divided by 2 so there are not too much clues
    print("You will have " + str(maxNumberOfClues) + " clues before losing.")
    
    while found == False and count != maxNumberOfClues:
        clueIndex = random.randint(0, len(clues) - 1) # chooses a random clue
        print("Clue number " + str(count + 1) + ": " + clues[clueIndex]) # prints it
        del clues[clueIndex] # deletes it from the list

        inputNum = int(input("\nEnter your guess: "))
        if inputNum < randomNum:
            print("\n" + str(inputNum) + " is smaller than the number!")
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

    replay = input("Do you want to play again? Enter 'yes' if yes and whatever else if no: ") # determines if the while loop starts over
