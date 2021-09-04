import random
import time

print("Welcome to the random password generator!")
time.sleep(0.2) 


alphabets = ["a", "B", "c", "D", "e", "F", "g", "H", "i", "J", "k", "L", "m", "N", "o", "P", "q", "R", "s", "T", "u", "V", "w", "X", "y", "Z"]
abcd = random.randint(10, 40)
roundoff = round(abcd/10)
eight = int(10000000)
twothree = eight + random.randint(0, 100000) 
print("your password is: " + alphabets[roundoff] + str(twothree))