import string
import time
from itertools import product
from tqdm import tqdm

# Characters available for the password
digits = string.digits
letters = string.ascii_letters
alls = digits + letters  # All possible characters

# User input
password = input("\033[1;37mEnter a password with a maximum of 6 characters: \033[0m ")
length = len(password)
rt = input("Do you want me to perform a \033[1;31mbrute force attack\033[0m on your password?! ").lower()

start_time = time.time()

if rt == "yes":
    attempts = 0
    # Generate possible combinations
    for guess in tqdm(product(alls, repeat=length), desc="\033[1;31mAttempts\033[0m", total=len(alls)**length):
        guess = ''.join(guess)
        attempts += 1  # Increment the number of attempts

        # Check if the combination is correct
        if guess == password:
            print("\n\033[1;31m[WARNING]\033[0m PASSWORD FOUND.")
            print(f"\nThe password is \033[1;31m{guess}\033[0m")
            print(f"\033[1;37mTime taken to find the password: {time.time()-start_time:.2f} seconds")
            print(f"Number of attempts: {attempts}\033[0m")
            break
else:
    print("Maybe next time!")
