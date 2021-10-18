import bcrypt
import time

#cth59, $2b$12$anjX1DI6oZEPn6NJ7rpuCe8CrhUVsEUIwCi1YRiPU/5iEE0ouWWoi
#jc4283, $2b$12$NSA150Hmp50WsGwGwpBdMOu/gLTyGEVDyU3xd49w9Myftyjs.I83y
#uau23, $2b$12$El3BYjnjUkEV4elpQkV0f.jczSOmau3LLUmCmdVWHqlee1XuYvfV6

def guessPasswd(passwd):
    passwd=passwd.encode()
    firstltr = "a"
    secondltr = "a"
    guess = "aa"
    guess = guess.encode()
    totalGuesses=0

    #Tests each guess, increments guess by 1 letter if wrong
    while not(bcrypt.checkpw(guess, passwd)):
        totalGuesses = totalGuesses + 1

        #Increments letters
        if(secondltr != "z"):
            secondltr = chr(ord(secondltr) + 1)
        else:
            secondltr = "a"
            firstltr = chr(ord(firstltr) + 1)

        #puts letters together
        guess = guess.decode()
        guess = firstltr + secondltr
        guess = guess.encode()
       
    guess = guess.decode()

    return totalGuesses, guess

#Basic function to 
def findPassword(passwd):
    totalGuesses = 0
    correctGuess = ""

    #Times and calls function to guess password
    start = time.time()
    totalGuesses, correctGuess = guessPasswd(passwd)
    end = time.time()
    timeInMins = (end - start) / 60.0

    #Prints to screen
    print("Total Guesses: " + str(totalGuesses))
    print("Correct Password: " + correctGuess)
    print("Time(mins): %.3f" %(timeInMins))

    return

#cth59
print("Guessing password for cth59...")
findPassword("$2b$12$anjX1DI6oZEPn6NJ7rpuCe8CrhUVsEUIwCi1YRiPU/5iEE0ouWWoi")

#jc4283
print("Guessing password for jc4283...")
findPassword("$2b$12$NSA150Hmp50WsGwGwpBdMOu/gLTyGEVDyU3xd49w9Myftyjs.I83y")

#uau23
print("Guessing password for uau23...")
findPassword("$2b$12$El3BYjnjUkEV4elpQkV0f.jczSOmau3LLUmCmdVWHqlee1XuYvfV6")

#---NOTES---
#Average time per guess = 0.215 seconds
#Max guesses possible = 676
#Adding another character adds 1 to the exponent
#time = guesses * 0.215s

#---QUESTIONS---
#1.)How long would it take to brute force the passwords of every student in class?
#2.)How much longer would it take if the passwords were 3 letters?
#3.)How much harder would it be if you didn't know the encryption method was bcrypt?
#4.)How much harder would it be if the passwords had 1-8 characters using upper and lower case letters?
#5.)How much harder would it be if the passwords had 8-16 characters using upper, lower case, and numbers?
#6.)Did this assignment change how you think about password security at all?
#
#
# 1. 144 students * 72.67s = 10462.48
#                           or 174.408 mins
#
# 2. 2 letters = 26 * 26 = 676 guesses
#    3 letters = 26 * 26 * 26 = 17576 guesses
#    so, 26 times as long
#
# 3. ...
#
# 4. For every letter there are 2 types, so instead of 26 possible letters it is 52.
#    and for every added letter to the length of the password adds 1 to the exponent.
#    So it would take 52^n guesses where n is the length of the password
#
# 5. Similar to before, if we added numbers there are then 62 possibilties for each character.
#    So it would take 62^n guess where n is the length of the password
#
# 6. Yes...