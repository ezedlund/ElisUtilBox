"""
      :::::::::: :::        ::::::::::: 
     :+:        :+:            :+:      
    +:+        +:+            +:+       
   +#++:++#   +#+            +#+        
  +#+        +#+            +#+         
 #+#        #+#            #+#          
########## ########## ###########       
Created by: Eli
aka 3li
https://github.com/ezedlund/
# USE AT YOUR OWN RISK #
# EDUCATIONAL USE ONLY #
"""


import os
import subprocess
import time
import requests
import json
import random

from InquirerPy import inquirer


VERSION = "EUB v1.1"
"""
v1.0 12/29/2023 'the initial'
v1.1 01/04/2024 'the master list update'
"""

# color codes
Bl = "\033[30m"
Re = "\033[1;31m"
Gr = "\033[1;32m"
Ye = "\033[1;33m"
Blu = "\033[1;34m"
Mage = "\033[1;35m"
Cy = "\033[1;36m"
Wh = "\033[1;37m"

# toggles
kill_spotify = False
kill_discord = False
kill_steam = False

# random seed
random.seed(version=2)


def space_text(text):
    """
    Add a space after each character of provided string
    """
    new_text = ""
    for char in text:
        new_text += f"{char} "
    return new_text


def get_username():
    """
    Grab devices login name
    """
    try:
        return str(os.getlogin())
    except:
        return space_text("unknown")


def processes_setup():
    """
    get processes from master list on github
    """
    os.system("cls")
    url = "https://raw.githubusercontent.com/ezedlund/ElisUtilBox/main/process_master_list.txt"
    processes = []
    resp = requests.get(url)
    data = resp.text
    # print msg
    print(f"{Gr}startup~# ")
    # save each line if it doesnt contain a '#'
    for line in enumerate(data.split("\n")):
        os.system("cls")
        if not "#" in line:
            print(f"{Gr}startup~# loading processes [{line[0]}]")
        time.sleep(0.01)
    os.system("cls")
    print(f"{Gr}startup~# finished [{line[0]}]")
    time.sleep(1.5)
    return processes


def kill_process(process_name):
    """
    attempt to kill process with provided process_name
    """
    try:
        p = subprocess.Popen(
            ["taskkill", "/f", "/im", process_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        _out, err = p.communicate()
        if "ERROR" in str(err, "utf-8"):
            print(f"{Cy}@process_killer~# {Ye}{process_name} was not killed...{Wh}")
        else:
            print(f"{Cy}@process_killer~# {Gr}{process_name} was killed...{Wh}")
    except Exception as err:
        print(f"{Re}Error: {err}{Wh}")


def process_killer(process_list):
    """
    kills tasks using kill_process()
    """
    try:
        for process in process_list:
            kill_process(process)
    except Exception as err:
        print(f"Error: {err}")


def print_credits():
    """
    Print credits
    """
    # setup
    cred_strings = [
        r"      ___           ___              ",
        r"     /  /\         /  /\       ___   ",
        r"    /  /::\       /  /:/      /__/\  ",
        r"   /  /:/\:\     /  /:/       \__\:\ ",
        r"  /  /::\ \:\   /  /:/        /  /::\ ",
        r" /__/:/\:\ \:\ /__/:/      __/  /:/\/ ",
        r" \  \:\ \:\_\/ \  \:\     /__/\/:/    ",
        r"  \  \:\ \:\    \  \:\    \  \::/     ",
        r"   \  \:\_\/     \  \:\    \  \:\     ",
        r"    \  \:\        \  \:\    \__\/     ",
        r"     \__\/         \__\/     ",
        f"Version: {VERSION}",
        "Created by: Eli",
        "aka 3li",
        "https://github.com/ezedlund",
        f"# USE AT YOUR OWN RISK {get_username().upper()} #",
    ]
    # print
    for line in cred_strings:
        # randomly color line
        random_num = random.uniform(0.1, 0.2)
        if random_num > 0.19:
            print(f"{Re}{line}{Wh}")
        elif random_num > 0.17:
            print(f"{Mage}{line}{Wh}")
        elif random_num > 0.14:
            print(f"{Cy}{line}{Wh}")
        else:
            print(f"{Gr}{line}{Wh}")
        time.sleep(0.14)
    time.sleep(1)


def print_menu_msg():
    """
    print menu message
    """
    print(
        rf"""{Cy}               ______    __    _
              / ____/   / /   (_)   _____
             / __/     / /   / /   / ___/
            / /___    / /   / /   (__  )
           /_____/   /_/   /_/   /____/
       __  __   __     _     __    _    __
      / / / /  / /_   (_)   / /   (_)  / /_   __  __
     / / / /  / __/  / /   / /   / /  / __/  / / / /
    / /_/ /  / /_   / /   / /   / /  / /_   / /_/ /
    \____/   \__/  /_/   /_/   /_/   \__/   \__, /
               ____                        /____/
              / __ )  ____    _  __
             / __  | / __ \  | |/_/
            / /_/ / / /_/ / _>  <
           /_____/  \____/ /_/|_|{Wh}
            {Gr}{space_text(VERSION)}{Wh}
        {Gr}{space_text('created by: Eli')}{Wh}
        {Gr}{space_text('not for public use')}{Wh}
        {Gr}{space_text('enjoy your stay, ')}{Ye}{space_text(username)}{Wh}
        """
    )


def IP_lookup():
    """
    uses ipwho.is api to lookup infor about an ip address provided by user input
    """
    os.system("cls")
    try:
        # get ip input
        ip = input(f"{Wh}\n enter IP :{Gr}")
        os.system("cls")
        print(space_text(f"{Gr}getting info for you, {Ye}{username}{Gr}...{Wh}"))
        # use ipwho.is api for ip lookup
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        time.sleep(1)
        # print ip info
        print(f"{Wh}============= {Gr}       IP INFO       {Wh}=============")
        print(f"{Wh}\n IP              :{Gr}", ip)
        print(f"{Wh} IP Type         :{Gr}", ip_data["type"])
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        lat = int(ip_data["latitude"])
        lon = int(ip_data["longitude"])
        print(
            f"{Wh} Maps(ctrl+click):{Gr}",
            f"https://www.google.com/maps/@{lat},{lon},8z",
        )
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
        print(f"{Wh}============= {Gr}       IP INFO       {Wh}=============")
    except:
        os.system("cls")
        print(space_text("error bad IP..."))
        time.sleep(0.8)


if __name__ == "__main__":
    os.system("cls")
    username = get_username()
    print_credits()
    #####################
    #       TODO        #
    #####################
    # loading sequenece #
    process_list = processes_setup()
    # starting menu message
    os.system("cls")
    print_menu_msg()
    # menu loop
    while True:
        # menu setup
        menu_input = inquirer.select(
            message=f"@EUB~# ",
            choices=[
                "[ 1 ] clean tasks",
                "[ 2 ] ip lookup",
                "[ 3 ] options",
                "[ 4 ] clear screen",
                "[ 0 ] exit",
            ],
        ).execute()
        # options
        if "[ 1 ]" in str(menu_input):
            process_killer(process_list)
        elif "[ 2 ]" in str(menu_input):
            IP_lookup()
            pass
        elif "[ 3 ]" in str(menu_input):
            #####################
            #       TODO        #
            #####################
            print(f"{Re}COMING SOON...{Wh}")
            time.sleep(0.5)
            pass
        elif "[ 4 ]" in str(menu_input):
            os.system("cls")
            print_menu_msg()
        else:
            os.system("cls")
            break
    input(f"{Gr}thanks for using me\n{Re}press [enter] to exit...{Wh}")
