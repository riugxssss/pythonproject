# SCANNER TOOL BY RIUGXSS

# Importazione delle librerie necessarie
import socket
import threading
from datetime import datetime
import sys
import time
import ipaddress
import os

aar = []
# Funzione per stampare il logo del tool
def logo():
    """
    Questa funzione stampa un logo personalizzato con il nome del tool
    e i crediti per lo sviluppatore, Riugxss.
    """
    aa = """\033[1;35m
    
   ___  ____  ___  ______  ____________   _  ___  _________ 
  / _ \/ __ \/ _ \/_  __/ / __/ ___/ _ | / |/ / |/ / __/ _ )            \033[1;35m[\033[1;37m!\033[1;35m]\033[0m \033[1;35m \033[1;37mTool made by Riugxss\033[1;35m
 / ___/ /_/ / , _/ / /   _\ \/ /__/ __ |/    /    / _// , _/            \033[1;35m[\033[1;37m!\033[1;35m]\033[0m \033[1;35m \033[1;37mGitHub: riugxssss\033[1;35m  
/_/   \____/_/|_| /_/   /___/\___/_/ |_/_/|_/_/|_/___/_/|_|             
    
    \033[0m"""
    print(aa)
logo()
# Funzione per stampare il simbolo di avviso in colore
def colors():
    """
    Funzione per stampare un avviso colorato nel terminale.
    """
    colorpurple = "\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m"
    print(colorpurple)

# Funzione per tentare di connettersi a una porta del target
def start(target, port):
    global aar
    """
    Tenta di connettersi a una porta specifica di un indirizzo IP (target).
    
    Args:
    - target (str): L'indirizzo IP del target da scansionare.
    - port (int): La porta su cui tentare la connessione.
    """
    try:
        # Creazione di un socket per la connessione
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout per evitare attese lunghe
        addr = (target, port)  # Indirizzo e porta da connettere
        res = sock.connect_ex(addr)  # Tenta la connessione
        time.sleep(1)  # Pausa di 1 secondo tra le connessioni
        if res == 0:
            # Se la connessione è riuscita, la porta è aperta
            msg = f"\033[1;37mLa port {port}\033[0m \033[1;35mè aperta\033[0m"
            msgg = f"Port aperte: {port}"
            aar.append(msgg)
            print(f"{msg}")
            
        sock.close()
    except socket.error:
        # In caso di errore durante la connessione
        print("\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m \033[1;37mImpossibile connettersi a {target}\033[0m")
        sys.exit()
    except Exception as e:
        # Gestione di altri errori generici
        print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mSi è verificato un errore {e}\033[0m")
        sys.exit()

# Funzione per eseguire la scansione delle porte in parallelo usando i thread
def scansione(target, port_iniziale, port_finale):
    
    
    """
    Esegue la scansione delle porte sul target in parallelo, utilizzando il multithreading
    per velocizzare il processo.

    Args:
    - target (str): L'indirizzo IP del target.
    - port_iniziale (int): La porta iniziale da cui partire per la scansione.
    - port_finale (int): La porta finale fino alla quale eseguire la scansione.
    """
    try:
        # Informazioni iniziali sulla scansione
        print(f"Scansiono il \033[1;37mtarget\033[0m: {target}")
        time.sleep(1)
        print(f"\033[1;37mLa scansione\033[0m è iniziata alle ore: {datetime.now()}")
        
        threads = []  # Lista per contenere i thread
        # Ciclo per ogni porta nell'intervallo specificato
        for port in range(port_iniziale, port_finale + 1):
            # Creazione di un thread per ogni porta
            thread = threading.Thread(target=start, args=(target, port))
            threads.append(thread)  # Aggiungi il thread alla lista
            thread.start()  # Avvia il thread

        # Aspetta che tutti i thread finiscano prima di terminare la scansione
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        # Gestisce l'interruzione da tastiera
        print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m \033[1;37mL'utente ha interrotto il programma (Ctrl+C).\033[0m")
        sys.exit()
    except Exception as error:
        # Gestisce altri errori
        print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mSi è verificato un errore {error}\033[0m")
        sys.exit()

# Funzione principale che gestisce l'input dell'utente
def main():
    global aar
    
    """
    Funzione principale che raccoglie l'input dell'utente e avvia la scansione.
    Gestisce anche gli errori dovuti a input non validi o problemi di connessione.
    """
    if __name__ == "__main__":  # Assicura che il codice venga eseguito solo se avviato direttamente
        try:
            # Richiesta all'utente dell'indirizzo IP target
            target = input("Inserisci l'\033[1;37mindirizzo ip\033[0m che vuoi \033[1;35mscansionare\033[0m: ")
            
            # Verifica che l'indirizzo IP sia valido
            if ipaddress.IPv4Address(target):
                print("\033[1;35m[INDIRIZZO IP VALIDO]\033[0m")
            else:
                print("\033[1;35m[INDIRIZZO IP NON VALIDO]\033[0m")
            
            time.sleep(1)
            
            # Richiesta dell'intervallo di porte da scansionare
            port_iniziale = int(input("Inserisci la \033[1;35mport\033[0m da cui deve \033[1;37miniziare lo scan\033[0m (es: 1,2,3):\n"))
            port_finale = int(input("Inserisci la \033[1;35mport\033[0m con cui \033[1;37mdeve finire lo scan\033[0m (es: 400,401,402):\n"))
            
            # Verifica che le porte siano valide
            if port_iniziale < 1 or port_finale > 65535 or port_iniziale > port_finale:
                print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m\033[1;37mLe porte scelte non rispettano i parametri.\033[0m")
            else:
                # Avvia la scansione delle porte
                scansione(target, port_iniziale, port_finale)
            
            # Fine della scansione
            print(f"\033[1;37mScansione\033[0m completata alle: {datetime.now()}")
            time.sleep(1)
            def log():
                while True:
                    osfile = input("\033[1;37mVuoi salvare\033[0m i \033[1;35mlog dello scan?\033[0m ").lower()
                    if osfile in ["si", "no"]:
                        if osfile == "no":
                            print("\033[1;37mI log non verranno salvati.\033[0m")
                            break
                        else:
                            print("\033[1;37m[LOG]\033[0m I log hanno un nome predefinito, \033[1;35mcambialo se vuoi!\033[0m\n")
                            if not os.path.exists("logsbyriugxss"):
                                os.makedirs("logsbyriugxss")
                            percorso = os.path.join("logsbyriugxss", "logs")
                            with open(percorso, "w") as file:
                                file.write(f"[LOG] log del target: {target}\n{aar}\n")
                                print(f"\033[1;37mLog salvati in\033[0m \033[1;31m{percorso}\033[0m")
                                break
                    else:
                        print("\033[1;31m[ATTENZIONE]\033[0m \033[1;37mpuoi inserire solo si o no!\033[0m")
            log()
                # Attende l'input dell'utente per uscire
            input("\033[1;37mPremi Enter per uscire dal tool... \033[0m")
            sys.exit("\033[1;35mExiting..\033[0m")
            time.sleep(1)
        except KeyboardInterrupt:
            # Gestisce l'interruzione da tastiera
            print("\n\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m \033[1;37mL'utente ha interrotto il programma (Ctrl+C).\033[0m")
            sys.exit()
        except ipaddress.AddressValueError:
            # Gestisce un errore relativo a un IP non valido
            print("Il \033[1;37mtarget\033[0m inserito \033[1;35mnon è esistente.\033[0m")
            return main()  # Richiede un nuovo input
        except ValueError:
            # Gestisce un errore per input non numerico
            print("\033[1;35m[""\033[1;37m!""\033[1;35m]\033[0m\033[1;37mDevi inserire un'input valido.\033[0m")
            return main()
        except Exception as e:
            # Gestisce errori generici
            print(f"\033[1;35m[""\033[1;37m!"f"\033[1;35m]\033[0m\033[1;37mSi è verificato un errore {e}\033[0m")
            sys.exit()

# Avvio dello script
main()
