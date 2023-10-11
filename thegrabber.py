# colors
red = '\033[1;31;40m'
font = '\033[1;97m'
green = '\033[1;32;40m'

#pips
import random
from scapy.all import IP, ICMP, sr1
import os
import readline
import subprocess

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



#selcet module

print(f"{green}CHOOSE THE IP SCAN TYPE\n[1] NORMAL SCAN\n[2] SCAN ON A SPECIFIC PORT\n[99] EXIT{font}\n")

while True:
    try:
        user_choice = input(f"{green}#> {font}")
        if user_choice == '1':
            path_to_file = "modules/randomscan.py"
            subprocess.call(["python", path_to_file])

        elif user_choice == '2':
            path_to_file = "modules/portscan.py"
            subprocess.call(["python", path_to_file])
        elif user_choice == '99':
            break
        else:
            print(f"{red}Invalid option selected{font}")
            continue
    except KeyboardInterrupt:
        print(f"{red}press '99' to exit{font}")

