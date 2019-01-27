# -*- coding: utf-8 -*-
# Coded by alexyadev

import time

# Lib for making requests
import requests
import string
import sys
from sys import stdout
import shutil

_old_excepthook = sys.excepthook

# Lib for making PARSING of webpage
from bs4 import BeautifulSoup

# Colorama
from colorama import Fore, Back, Style, init

# Import the random library
import random
import re


# Welcomes user with
class Lightshot(object):

    parsealphabet = list(string.ascii_lowercase)
    parsenumbers = list(string.digits) 

    def welcomeUser():  
        print(Fore.CYAN + Style.BRIGHT +
            '''
            
 ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓  ██████  ██░ ██  ▒█████  ▄▄▄█████▓
 ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▒██    ▒ ▓██░ ██▒▒██▒  ██▒▓  ██▒ ▓▒
 ▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░░ ▓██▄   ▒██▀▀██░▒██░  ██▒▒ ▓██░ ▒░
 ▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░   ▒   ██▒░▓█ ░██ ▒██   ██░░ ▓██▓ ░ 
 ░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██████▒▒░▓█▒░██▓░ ████▓▒░  ▒██▒ ░ 
 ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░░  
 ░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░     ░    
 ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░      ░  ░  ░   ░  ░░ ░░ ░ ░ ▒    ░        
     ░  ░ ░        ░  ░  ░  ░               ░   ░  ░  ░    ░ ░           
                                                                      
            '''
        + Style.RESET_ALL) 
        
        print("\n")

        print(Fore.GREEN + Style.BRIGHT + '> Welcome to the' + Fore.RED + Style.BRIGHT +' lightshot parser.' + Style.RESET_ALL)
        print(Fore.GREEN + '  Author: feekcode, Github link:' + Style.DIM + ' https://github.com/despirito' + Style.RESET_ALL)
        print(Fore.GREEN + '  To any contribution, make pull-request to the repository' + Style.RESET_ALL)
        print('\n')


def generateCode():
    # Linking to Lightshot arrays
    alph            = Lightshot.parsealphabet
    num             =  Lightshot.parsenumbers

    # Init a secure hash random
    secure_random = random.SystemRandom()

    l1 = random.sample(alph, 1); l2 = random.sample(alph, 1);
    rd1 = random.sample(num, 1); rd2 = random.sample(num, 1); 
    rd3 = random.sample(num, 1); rd4 = random.sample(num, 1);

    data = l1 + l2 + rd1 + rd2 + rd3 + rd4
    resulter = ''.join(map(str, data))

    return resulter



def getHTML(code: str):
    myrandom = requests.get("http://prnt.sc/" + str(code), stream = True ,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3578.98 Safari/520.36'}).text
    return myrandom

# get image from under-image

def parseHTML(code: str):
    soup = BeautifulSoup(getHTML(code), features="html.parser")
    tags = soup.findAll("img", "no-click screenshot-image")

    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tags[0]['src'])

    if len(url) > 0:
        return tags[0]['src']
    else:
        return False

        

def main():
    
    Lightshot.welcomeUser()

    while(True):
        result = True
        ab = parseHTML(generateCode())

        if ab is False:
            result = False
        else:
            response = requests.get(ab, stream = True)
            result = True

        if result is True:
            filename = ab.split("/")[-1]
            with open(filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
        elif result is False:
                pass

    

def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[F")
        print(Fore.RED + Style.BRIGHT + '\n\n' + 'Parsing has stopped' + Style.RESET_ALL)
    else:
        _old_excepthook(exctype, value, traceback)

sys.excepthook = myexcepthook



if __name__ == "__main__":
    init()
    main()