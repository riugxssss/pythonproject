# SCANNER TOOL BY RIUGXSS

# Import necessary libraries
import socket
import threading
from datetime import datetime
import sys
import time
import ipaddress
import os

aar = []

# Function to print the tool's logo
def logo():
    """
    This function prints a custom logo with the tool's name
    and credits to the developer, Riugxss.
    """
    aa = """\033[1;35m
    
   ___  ____  ___  ______  ____________   _  ___  _________ 
  / _ \/ __ \/ _ \/_  __/ / __/ ___/ _ | / |/ / |/ / __/ _ )            \033[1;35m[\033[1;37m!\033[1;35m]\033[0m \033[1;35m \033[1;37mTool made by Riugxss\033[1;35m
 / ___/ /_/ / , _/ / /   _\ \/ /__/ __ |/    /    / _// , _/            \033[1;35m[\033[1;37m!\033[1;35m]\033[0m \033[1;35m \033[1;37mGitHub: riugxssss\033[1;35m  
/_/   \____/_/|_| /_/   /___/\___/_/ |_/_/|_/_/|_/___/_/|_|             
    
    \033[0m"""
    print(aa)

logo()

# Function to print a warning symbol in color
def colors():
    """
    Function to print a colored warning in the terminal.
    """
    colorpurple = "\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m"
    print(colorpurple)

# Function to attempt connecting to a target port
def start(target, port):
    global aar
    """
    Attempts to connect to a specific port of a target IP address.
    
    Args:
    - target (str): The target IP address to scan.
    - port (int): The port to attempt the connection.
    """
    try:
        # Create a socket for the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout to avoid long waits
        addr = (target, port)  # Address and port to connect to
        res = sock.connect_ex(addr)  # Attempt the connection
        time.sleep(1)  # Pause 1 second between connections
        if res == 0:
            # If the connection is successful, the port is open
            msg = f"\033[1;37mPort {port}\033[0m \033[1;35mis open\033[0m"
            msgg = f"Open port: {port}"
            aar.append(msgg)
            print(f"{msg}")
            
        sock.close()
    except socket.error:
        # Handle connection errors
        print("\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m \033[1;37mUnable to connect to {target}\033[0m")
        sys.exit()
    except Exception as e:
        # Handle other generic errors
        print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mAn error occurred: {e}\033[0m")
        sys.exit()

# Function to scan ports in parallel using threads
def scan(target, start_port, end_port):
    """
    Scans the ports on the target in parallel using multithreading
    to speed up the process.

    Args:
    - target (str): The target IP address.
    - start_port (int): The starting port for the scan.
    - end_port (int): The ending port for the scan.
    """
    try:
        # Initial scan information
        print(f"Scanning the \033[1;37mtarget\033[0m: {target}")
        time.sleep(1)
        print(f"\033[1;37mThe scan\033[0m started at: {datetime.now()}")
        
        threads = []  # List to hold threads
        # Loop through each port in the specified range
        for port in range(start_port, end_port + 1):
            # Create a thread for each port
            thread = threading.Thread(target=start, args=(target, port))
            threads.append(thread)  # Add thread to the list
            thread.start()  # Start the thread

        # Wait for all threads to finish before completing the scan
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        # Handle keyboard interruption
        print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m \033[1;37mUser interrupted the program (Ctrl+C).\033[0m")
        sys.exit()
    except Exception as error:
        # Handle other errors
        print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mAn error occurred: {error}\033[0m")
        sys.exit()

# Main function to handle user input
def main():
    global aar
    
    """
    Main function that gathers user input and starts the scan.
    Also handles errors from invalid input or connection issues.
    """
    if __name__ == "__main__":  # Ensures the code runs only if executed directly
        try:
            # Prompt user for the target IP address
            target = input("Enter the \033[1;37mIP address\033[0m you want to \033[1;35mscan\033[0m: ")
            
            # Validate the IP address
            if ipaddress.IPv4Address(target):
                print("\033[1;35m[VALID IP ADDRESS]\033[0m")
            else:
                print("\033[1;35m[INVALID IP ADDRESS]\033[0m")
            
            time.sleep(1)
            
            # Prompt for the port range to scan
            start_port = int(input("Enter the \033[1;35mport\033[0m to \033[1;37mstart the scan\033[0m (e.g., 1,2,3):\n"))
            end_port = int(input("Enter the \033[1;35mport\033[0m to \033[1;37mend the scan\033[0m (e.g., 400,401,402):\n"))
            
            # Validate the ports
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m\033[1;37mThe chosen ports do not meet the parameters.\033[0m")
            else:
                # Start the port scan
                scan(target, start_port, end_port)
            
            # End of scan
            print(f"\033[1;37mScan\033[0m completed at: {datetime.now()}")
            time.sleep(1)
            
            # Save log
            def log():
                while True:
                    save_logs = input("\033[1;37mDo you want to save\033[0m the \033[1;35mscan logs?\033[0m ").lower()
                    if save_logs in ["yes", "no"]:
                        if save_logs == "no":
                            print("\033[1;37mLogs will not be saved.\033[0m")
                            break
                        else:
                            print("\033[1;37m[LOG]\033[0m Logs have a default name, \033[1;35mchange it if you want!\033[0m\n")
                            if not os.path.exists("logsbyriugxss"):
                                os.makedirs("logsbyriugxss")
                            path = os.path.join("logsbyriugxss", "logs")
                            with open(path, "w") as file:
                                file.write(f"[LOG] Logs for target: {target}\n{aar}\n")
                                print(f"\033[1;37mLogs saved in\033[0m \033[1;31m{path}\033[0m")
                                break
                    else:
                        print("\033[1;31m[WARNING]\033[0m \033[1;37mYou can only enter yes or no!\033[0m")
            log()
            
            # Wait for user input to exit
            input("\033[1;37mPress Enter to exit the tool... \033[0m")
            sys.exit("\033[1;35mExiting..\033[0m")
            time.sleep(1)
        except KeyboardInterrupt:
            # Handle keyboard interruption
            print("\n\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m \033[1;37mUser interrupted the program (Ctrl+C).\033[0m")
            sys.exit()
        except ipaddress.AddressValueError:
            # Handle invalid IP error
            print("The \033[1;37mtarget\033[0m entered \033[1;35mdoes not exist.\033[0m")
            return main()  # Prompt for new input
        except ValueError:
            # Handle non-numeric input error
            print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m\033[1;37mYou must enter valid input.\033[0m")
            return main()
        except Exception as e:
            # Handle generic errors
            print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mAn error occurred: {e}\033[0m")
            sys.exit()

# Start the script
if __name__ == "__main__":
    main()

