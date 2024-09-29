import time
import os
import subprocess
from colorama import Fore, init

class Colors:
    def __init__(self):
        self.green = "\033[38;5;28m"

ga = Colors()
init()

print(Fore.RESET + '''
                                    AA
                                   AAA
                                  AAA
                                 AAA AAA
                                AAA  AAAA
                               AAA  AAAAAA
                              AAA  AAA  AAA
                             AAA  AAA    AAA
                            AAA  AAA      AAA
                           AAAAAAAAAAAAAAAAAAA
                               AAAA
                              AAAA
                            AAAA
''')
print(ga.green + '''
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
''')
print(Fore.RESET+'''
v2.4    
This tool helps you to change your IP address to be AnOnyMoUs...
Copyright: @ALHARAM             
''')
try:
    import requests
except Exception:
    print(ga.green+'[+]', Fore.RESET+'python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print(Fore.CYAN+'[!]', Fore.RESET+'python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print(ga.green+'[+]', Fore.RESET+'tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print(Fore.CYAN+'[!]', Fore.RESET+'tor is installed succesfully ')

def Anonymous():
    url='http://checkip.amazonaws.com'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print (ga.green+'[+]', Fore.RESET+'Your IP has been Changed to: '+str(Anonymous()))


os.system("service tor start")

time.sleep(3)
print(ga.green+"[*]", Fore.RESET+"Change your  SOCKES to 127.0.0.1:9050")
os.system("service tor start")
s = input(Fore.CYAN+"[*] Time to change your ip [type=60] >> ")
l = input(Fore.CYAN+"[*] How many times do you want to change your IP? enter to infinite IP change] >> ") or "0\n"

try:
    l = int(l)
    if l == 0:
        print(ga.green+"[*]", Fore.RESET+"Starting infinite IP change. Press Ctrl+C to stop.\n")
        while True:
            try:
                time.sleep(int(s)) 
                change()  
            except KeyboardInterrupt:
                print(Fore.RED+'[x]', Fore.RESET+'Anonymous script is closed.')
                break
    else:
        for _ in range(l):
            time.sleep(int(s)) 
            change() 

except ValueError:
    print(Fore.RED+"[x]", Fore.RESET+"Invalid input. Please enter a valid number.")
