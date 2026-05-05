import random 
def cheat():
    secnum = random.randint(1,100)
    attempts = 0
    maxattempts = 10
    lastdis = None
    print("---MS SHEENAZS SECRET PASSWORD---")
    print("Ms. Sheenaz has a secret password that is a number between 1 and 100. Can you guess it? You have 10 attempts to get it right!")
    while attempts < maxattempts:
        userin = input(f"\nAttempt {attempts + 1}: Enter your guess:").lower().strip()
        if userin == "isaadmin":
            print(f"[SYSTEM OVERRIDE]: THE SECRET NUMBER IS {secnum}")
            try:
                guess = int(userin)
                attempts += 1
                currentdis = abs(secnum - guess)
                if guess == secnum:
                    print(f"NOW YOU HACK THE COMPUTERS!! jk but you guessed in {attempts} tries!")
                if lastdis is not None:
                if currentdis < lastdis:
                    print("WARMER!")
        else:
                    print("COLDER!")

        if guess < secnum:
            print("Hint:higher")
        else
            print("hint:lower")
            lastdis = currentdis 
        ValueError:
        print("Enter a number or a valid command!!")
    print(f"\nGame Over. The number was {secnum}")
    cheat()
    
    
    

