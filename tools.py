import os
import cowsay
import requests
import socket 
from bs4 import BeautifulSoup
from colorama import Fore 
from os import close, system
import platform , socket

sys = platform.system()

def Clears():
    if sys == "Windows":
        os.system("cls")
    elif sys == "Linux":
        os.system("clear")

Clears()

def extract_links(url):
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        fopen = open('url.txt' , 'w')
        for link in links:
            print(Fore.RED + f"[+]{Fore.CYAN +link}")
            txxt = f"{link} \r"
            wrike = fopen.write(txxt)
        fopen.close()
        
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except KeyboardInterrupt as h:
        print("Not Key" + h)

def url_index():

    if __name__ == "__main__":
        grenn = Fore.GREEN
        Ylo = Fore.LIGHTRED_EX 
        ip = socket.gethostname()
        ips = socket.gethostbyname(ip)
        text = f"Your system IP -> {ips}"
        cowsay.octopus(Fore.LIGHTRED_EX +text)
        url = input(Ylo +"Enter the URL: ")
        extract_links(url)

def IP_Fender_website():
    Clears()
    ip = socket.gethostname()
    ips = socket.gethostbyname(ip)
    text = f"Your system IP -> {ips}"
    cowsay.beavis(text)
    try:
        user_File = input("[?] - Enter the file name? ")
        with open(user_File , 'r') as File_open:
            read  = File_open.readlines()
            for File_pathi in read:
                Pathi = File_pathi.replace("https://" , "").replace("http://" , "").split("/")[0].strip()
                try:
                    ip = socket.gethostbyname(Pathi)
                    print(f"{Fore.GREEN}[+]{Fore.RESET} - success {ip} - > {Fore.YELLOW}{Pathi}")
                except socket.gaierror:
                    print(f"{Fore.RED}[-] {Fore.RESET}- Connection problem -> {Pathi}")
                    continue
    except FileNotFoundError:
        print("File Not Found")
    Home_inp = input("do you want to go home ? y/n  ").lower()
    if Home_inp == "y":
        Home()
    elif Home_inp == "n":
        Clears()
        exit



def Home():
    Clears()
    text1 = f"""
    {Fore.WHITE}
 ██▒   █▓ ▒█████   ██▓     ██░ ██  ▄▄▄       ██▓  ▄▄▄█████▓▓██   ██▓
▓██░   █▒▒██▒  ██▒▓██▒    ▓██░ ██▒▒████▄    ▓██▒  ▓  ██▒ ▓▒ ▒██  ██▒
 ▓██  █▒░▒██░  ██▒▒██░    ▒██▀▀██░▒██  ▀█▄  ▒██░  ▒ ▓██░ ▒░  ▒██ ██░
  ▒██ █░░▒██   ██░▒██░    ░▓█ ░██ ░██▄▄▄▄██ ▒██░  ░ ▓██▓ ░   ░ ▐██▓░
   ▒▀█░  ░ ████▓▒░░█████{Fore.YELLOW}█▒░▓█▒░██▓ ▓█   ▓██▒░██████▒▒██▒ ░   ░ ██▒▓░
   ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░▒ ░░      ██▒▒▒ 
   ░ ░░    ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░  ░     ▓██ ░▒░ 
     ░░  ░ ░ ░ ▒    ░ ░    ░  ░░ ░  ░   ▒     ░ ░   ░       ▒ ▒ ░░  
      ░      ░ ░      ░  ░ ░  ░  ░      ░  ░    ░  ░        ░ ░     
     ░                                                      ░ ░     
{Fore.RESET}
    """
    print(text1)
    user_input = input(f"""{Fore.CYAN}[1]{Fore.RESET} - Website URL indexer\n\n{Fore.CYAN}[2]{Fore.RESET} - IP Fender website\n\n{Fore.CYAN}[3]{Fore.RESET} - Exit\n\n{Fore.RED}[?]{Fore.RESET} - where are you going ? """)
    if user_input == "1":
        Clears()
        url_index()
        
    elif user_input == "3":
        Clears()
        exit
    elif user_input == "2":
        IP_Fender_website()
Home()