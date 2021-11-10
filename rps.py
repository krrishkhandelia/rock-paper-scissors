import random 
lst = ['r','p','s']

chances = 10
#no of rounds played 
noc = 0 
#user's point
up = 0
#computer's point
cp = 0

print("====>THIS IS ROCK, PAPER AND SCISSORS<====") 
print("USE\n 'r' FOR ROCK\n 'p' FOR PAPER\n 's' FOR SCISSORS")

while noc < chances:
    ui = input("ROCK, PAPER OR SCISSORS: \n") #userinput
    ci = random.choice(lst) #computerinput

    if ui == ci:
        print("IT IS A TIE")

    #when the user enters rock
    if ui == "r" and ci == "p":
        print("COMPUTER GETS A POINT")
        print(f"THE COMPUTER GUESSED {ci} AND YOU GUESSD {ui}")
        cp += 1
    if ui == "r" and ci == "s":
        print("YOU GET A POINT")
        print(f"THE COMPUTER GUESSED {ci} AND YOU GUESSED {ui}")
        up += 1

    #when the user enters paper 
    if ui == "p" and ci == "s":
        print("COMPUTER GETS A POINT")
        print(f"THE COMPUTER GUESSED {ci} AND YOU GUESSD {ui}")
        cp += 1
    if ui == "p" and ci == "r":
        print("YOU GET A POINT")
        print(f"THE COMPUTER GUESSED {ci} AND YOU GUESSED {ui}")
        up += 1

    #when the user enters scissor 
    if ui == "s" and ci == "r":
        print("COMPUTER GETS A POINT")
        print(f"THE COMPUTER GUESSED {ci} AND YOU GUESSD {ui}")
        cp += 1
    if ui == "s" and ci == "p":
        print("YOU GET A POINT")
        print(f"THE COMPUTER GUESSED {ci} ADN YOU GUESSED {ui}")
        up += 1

    noc += 1
if noc >= chances:
    print("GAME OVER")
if up == cp:
    print("IT IS A TIE... TRY AGAIN SOMETIME")
if up > cp:
    print("CONGRATULATIONS!!!!! YOU WON!")
elif cp > up:
    print("OOPS YOU LOSE. BETTER LUCK NEXT TIME")

print(f"YOUR SCORE WAS {up} AND THE COMPUTER'S SCORE WAS {cp}")



