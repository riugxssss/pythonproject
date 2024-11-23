import string
import time
from itertools import product
from tqdm import tqdm

# Caratteri utilizzabili nella password
digits = string.digits
letters = string.ascii_letters
alls = digits + letters  # Tutti i caratteri possibili

# Input utente
password = input("\033[1;37mInserisci una password composta da max 6 caratteri: \033[0m ")
lenght = len(password)
rt = input("Vuoi che faccia un \033[1;31mattacco di bruteforce\033[0m sulla tua password?! ").lower()

start_time = time.time()

if rt == "si":
    attempts = 0
    # Creazione delle combinazioni possibili
    for guess in tqdm(product(alls, repeat=lenght), desc="\033[1;31mTentativi\033[0m", total=len(alls)**lenght):
        guess = ''.join(guess)
        attempts += 1  # Incremento del numero di tentativi

        # Controllo se la combinazione è quella giusta
        if guess == password:
            print("\n\033[1;31m[ATTENZIONE]\033[0m PASSWORD TROVATA.")
            print(f"\nLa password è \033[1;31m{guess}\033[0m")
            print(f"\033[1;37mTempo impiegato per trovare la password: {time.time()-start_time:.2f} secondi")
            print(f"Numero di tentativi: {attempts}\033[0m")
            break
else:
    print("Sarà per la prossima volta!")
 
