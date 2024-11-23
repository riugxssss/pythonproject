#importing libraries
import sys    
import time    

# Introduction
print("\033[1;39mWelcome to the program made by riugxs.\033[0m")

# Function to ask the user if they want to perform another calculation
def play_again():
    """
    Continuously asks the user if they want to perform another calculation.
    If the user says "no", the program exits gracefully. If "yes", it returns
    to the main loop for another calculation.
    """
    while True:
        
        continue_game = input("Do you want to perform \033[1;31manother calculation?\033[0m (yes/no): ").strip().lower()
        if continue_game in ["yes", "no"]:
            if continue_game == "no":
            
                time.sleep(1)
                print("\033[1;37mRiugxs thanks you\033[0m, come back soon my friend!")
                sys.exit()  # Terminate the program
            else:
                # If "yes", return to allow the main program to continue
                print("\033[1;37mI'm glad!\033[0m Thank you for typing \033[1;31m'yes'\033[0m\n")
                return
        else:
            
            print("\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mYou can only type: yes or no.\033[0m")

# Main function to handle temperature conversions
def main():
 
    try:
        while True:
            # Display menu for choosing the type of conversion
            aa = int(input("\033[1;39mChoose the type of conversion:\n\033[1;34m1: Celsius\n2: Fahrenheit\n3: Kelvin\n\033[0m"))
            
            if aa == 1:  # Conversion from Celsius
                print("You chose \033[1;31mCelsius\033[0m")
                # Get the input temperature in Celsius
                r = float(input("\033[1;39mWhat number would you like to convert? \033[1;31m(number in Celsius)\n\033[0m"))
               
                sws = int(input("\033[1;34mChoose how to convert your number\n\033[1;34m1: Kelvin\n2: Fahrenheit\n\033[0m"))
                if sws == 2:
                    # Convert Celsius to Fahrenheit and display the result
                    print(f"Your converted number is: \033[1;31m{(r*(9/5)+32):.2f}\033[0m F ")
                elif sws == 1:
                    # Convert Celsius to Kelvin and display the result
                    print(f"Your converted number is: \033[1;31m{(r + 273.15):.2f}\033[0m K")
                else:
                   
                    print("\033[1;31m[!] Please enter only valid numbers.\033[0m")
                    continue

            elif aa == 2:  # Conversion from Fahrenheit
                print("You chose \033[1;31mFahrenheit\033[0m")
                # Get the input temperature in Fahrenheit
                r = float(input("\033[1;39mWhat number would you like to convert? \033[1;31m(number in Fahrenheit)\n\033[0m"))
                
                sws = int(input("\033[1;39mChoose how to convert your number\n\033[1;34m1: Celsius\n2: Kelvin\n\033[0m"))
                if sws == 2:
                    # Convert Fahrenheit to Kelvin and display the result
                    print(f"Your converted number is: \033[1;31m{((r-32)*5/9+273.15):.2f}\033[0m K ")
                elif sws == 1:
                    # Convert Fahrenheit to Celsius and display the result
                    print(f"Your converted number is: \033[1;31m{((r-32) * 5/9):.2f}\033[0m C")
                else:
                    
                    print("\033[1;31m[!] Please enter only valid numbers.\033[0m")
                    continue

            elif aa == 3:  # Conversion from Kelvin
                print("You chose \033[1;31mKelvin\033[0m")
                # Get the input temperature in Kelvin
                r = float(input("What number would you like to convert? \033[1;31m(number in Kelvin)\n\033[0m"))
                sws = int(input("\033[1;39mChoose how to convert your number\n\033[1;34m1: Celsius\n2: Fahrenheit\n\033[0m"))
                if sws == 2:
                    # Convert Kelvin to Fahrenheit and display the result
                    print(f"Your converted number is: \033[1;31m{((r-273.15) * 9/5 + 32):.2f}\033[0m F ")
                elif sws == 1:
                    # Convert Kelvin to Celsius and display the result
                    print(f"Your converted number is: \033[1;31m{(r-273.15):.2f}\033[0m C")
                else:
                    
                    print("\033[1;31m[!] Please enter only valid numbers.\033[0m")
                    continue
            else:
                # Handle invalid main menu choice
                print("\033[1;31m[!] Please enter only valid numbers.\033[0m")
                continue

            # Ask if the user wants to perform another calculation
            play_again()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] The user interrupted the program (Ctrl+C).\033[0m")
        sys.exit()
    except ValueError:
        print("\033[1;31m[!] Please enter a valid value.\033[0m")
        return main()

main()
