#password generator
import string
from random import choices


def colors():
    yellow = "\033[1;33m" #Color usage
    end = "\033[0m" #End usage
    white_intense = "\033[1;37m" #Color usage
    red = "\033[1;31m" #ALLERT usage
def main():
    try:
        print("\033[1;37mHi,\033[0m Welcome in the \033[1;33mpassword generator!\033[0m")
        while True:
            rr = input("Do you want to \033[1;33mgenerate a password?\033[0m\033[1;37m(yes/no)\033[0m\n").lower()

            if rr == "yes":
                print("\033[1;37mAwesome!\033[0m")
                aya = input("\033[1;37mIn your password do you want\033[0m \033[1;33mspecial punctuation?\033[0m ").lower()
                if aya == "yes":
                        alle = string.digits + string.ascii_letters + string.punctuation
                        argh = int(input("How many \033[1;33mcharacters\033[0m do you need for \033[1;33myour password?\033[0m "))
                        if argh <= 0:
                            print("\033[1;31m[!]\033[0m white_intenseYou can't put a number lower than 0.\033[0m")
                        else:
                            password = ''
                            password = ''.join(choices(alle, k=argh))
                            print(f"\033[1;37mThere is your password:\033[0m yellow{password}\033[0m")
                elif aya == "no":
                        art = string.digits + string.ascii_letters
                        argh = int(input("How many \033[1;33mcharacters\033[0m do you need for \033[1;33myour password?\033[0m "))
                        if argh <= 0:
                            print("\033[1;31m[!]\033[0m \033[1;37mYou can't put a number lower than 0.\033[0m")
                        else:
                            password = ''
                            password = ''.join(choices(art, k=argh))
                            print(f"\033[1;37mThere is your password:\033[0m yellow{password}\033[0m")
                else:
                        print("You can choose \033[1;31monly YES or NO\033[0m")
            elif rr == "no":
                print("Comeback \033[1;31many time!\033[0m")
                return False
            else:
                print("You can choose \033[1;31monly YES or NO\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;37mThe user press the exiting combination (Ctrl+C),\033[0m \033[1;31mexiting..\033[0m")
    except ValueError:
        print("Please, \033[1;31mPut a valid VALUE.\033[0m")
main()
