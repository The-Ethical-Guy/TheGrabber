# colors
red = '\033[1;31;40m'
font = '\033[1;97m'
green = '\033[1;32;40m'

#pips
import random
from scapy.all import IP, ICMP, sr1
import socket
import os
import readline

#logo
os.system("clear")
logo = """
#%#            *####%####            #%#
%%%%#     *#%%%%%%%%%%%%%%%##*     #%%%%
#%%%%%####%%%%%###%######%%%%%####%%%%%#
#%%%%%%%%%%##*             ##%%%%%%%%%%#
 #%%%%%%%##                   #%%%%%%%# 
  #%%%%%#                      ##%%%%#  
  #%%%#                          #%%%#  
  #%%%#  ####              ####  #%%%#  
 #%%%#    %%%%%##      ##%%%%%#   #%%%# 
 #%%%=     #%%%#        ##%%#      #%%# 
 #%%#                              #%%# 
 #%%%#                            *%%%# 
  #%%#     ##################     #%%%* 
  #%%%#     ##%%%%%%%%%%%%##     #%%%#  
   #%%%#      ###%%%%%%###      #%%%#   
    #%%%##                    ##%%%#                                                                                      v2.3 by TheEthicalGuy
     ##%%%%#                ##%%%%#     
       #%%%%%####      ####%%%%%#       
         ##%%%%%%%%%%%%%%%%%%##         
             ###%%%%%%%%%##               
"""
  
name = """






 ________  __                   ______                      __        __                                 
|        \|  \                 /      \                    |  \      |  \                                
 \$$$$$$$$| $$____    ______  |  $$$$$$\  ______   ______  | $$____  | $$____    ______    ______        
   | $$   | $$    \  /      \ | $$ __\$$ /      \ |      \ | $$    \ | $$    \  /      \  /      \       
   | $$   | $$$$$$$\|  $$$$$$\| $$|    \|  $$$$$$\ \$$$$$$\| $$$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\      
   | $$   | $$  | $$| $$    $$| $$ \$$$$| $$   \$$/      $$| $$  | $$| $$  | $$| $$    $$| $$   \$$      
   | $$   | $$  | $$| $$$$$$$$| $$__| $$| $$     |  $$$$$$$| $$__/ $$| $$__/ $$| $$$$$$$$| $$            
   | $$   | $$  | $$ \$$     \ \$$    $$| $$      \$$    $$| $$    $$| $$    $$ \$$     \| $$            
    \$$    \$$   \$$  \$$$$$$$  \$$$$$$  \$$       \$$$$$$$ \$$$$$$$  \$$$$$$$   \$$$$$$$ \$$    





"""

logo_lines = logo.split("\n")
name_lines = name.split("\n")

for logo_line, name_line in zip(logo_lines, name_lines):
    print(f"\033[1;97m\033[91m{logo_line}\033[0m\033[1;32;40m{name_line}")






def generate_random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def send_ping_request(ip):
    packet = IP(dst=ip) / ICMP()
    response = sr1(packet, timeout=2, verbose=False)
    if response:
        return True
    else:
        return False

def get_ip_type(ip):
    try:
        host = socket.gethostbyaddr(ip)
        if "server" in host[0].lower():
            return (f"Server | DNS: {host[0]}")
        elif "host" in host[0].lower():
            return (f"Host | DNS: {host[0]}")
        elif "network" in host[0].lower():
            return (f"Network Host | DNS: {host[0]}")
        elif "domain" in host[0].lower():
            return (f"Domain | DNS: {host[0]}")
        elif "mail" in host[0].lower():
            return (f"Mail Server | DNS: {host[0]}")
        elif "web" in host[0].lower():
            return (f"Web Server | DNS: {host[0]}")
        elif "wifi" in host[0].lower():
            return (f"wifi | DNS: {host[0]}")
        elif "proxy" in host[0].lower() or "proxy" in ip.lower():
            return (f"proxy | DNS: {host[0]}")
        elif "ftp" in host[0].lower():
            return (f"FTP Server | DNS: {host[0]}")
        elif "dsl" in host[0].lower():
            return (f"DSL Server | DNS: {host[0]}")
        elif "ddsl" in host[0].lower():
            return (f"DDSL Server | DNS: {host[0]}")
        elif ".net" in host[0].lower():
            return (f"NET | DNS: {host[0]}")
        elif ".com" in host[0].lower():
            return (f"Website | DNS: {host[0]}")
        else:
            return (f"N/A | DNS: {host[0]}")
    except socket.herror:
        return "Error"
    

def main():
    try:
        num_attempts = int(input(f"{green}ENTER THE NUMBER OF IPS TO GUESS: {font}"))
        
        save_ips = input(f"{green}Do you want to save working IPs to a file? (y/n): {font}").lower()
        if save_ips == "y":
            file_path = input(f"{green}Enter the file path to save the working IPs: {font}")
            with open(file_path, "w") as ip_file:
                for _ in range(num_attempts):
                    random_ip = generate_random_ip()
                    if send_ping_request(random_ip):
                        ip_type = get_ip_type(random_ip)
                        print(f"{green}IP: {random_ip} | STATUS: working | TYPE: {ip_type}{font}")
                        ip_file.write(f"IP: {random_ip} | STATUS: working | TYPE: {ip_type}\n")
                    else:
                        print(f"{red}IP: {random_ip} | STATUS: closed{font}")
        elif save_ips == "n":
            for _ in range(num_attempts):
                random_ip = generate_random_ip()
                if send_ping_request(random_ip):
                    ip_type = get_ip_type(random_ip)
                    print(f"{green}IP: {random_ip} | STATUS: working | TYPE: {ip_type}{font}")
                else:
                    print(f"{red}IP: {random_ip} | STATUS: closed{font}")
        else:
            print("{red}Invalid choice. Please enter 'y' or 'n' {font}")
    except KeyboardInterrupt:
        print(f"{red}Invalid choice{font}")


if __name__ == "__main__":
    main()
    
print(f"{green}CHOOSE THE IP SCAN TYPE\n[1] SCAN RANDOMLY\n[2] SCAN ON A SPECIFIED PORT\n[99] EXIT{font}\n")
