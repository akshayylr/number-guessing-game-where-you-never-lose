import random
import tkinter
print("welcome to 'NEVER LOSE' ")
actual_number=int(random.randint(1,100))
guessed_number=0
print((actual_number))
tries=0
while(guessed_number!=actual_number):
    tries=tries+1
    guessed_number = int(input("take a guess of the number between 1 and 100: "))
    if guessed_number>actual_number:
        if guessed_number%actual_number==0:
            print("your guess is multiple of the actuall number")
            continue
        else:
            print("your guess is high")
            continue
    if guessed_number<actual_number:
        if actual_number%guessed_number==0:
            print("the number is divisible by the guessed number")
            continue
        else:
            print("your guess is less, guess a larger number")
            continue
if guessed_number==actual_number:
    print("you did it!! in just "+str(tries)+" tries")
