import requests
from colorama import init, Fore, Style
import names
import re
import random
init(convert=True)


def checkEn():
    countOfGood = 0
    countOfBad = 0
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    api_key = input('Enter an API of isitarealemail.com: ')
    try:
        emailFile = input("Enter a path to the txt with emails: ")
    except:
        print(Fore.RED + 'Invalid path to txt file!')

    emails = open(str(emailFile), 'r').read().split('\n')


    for i in range(0, len(emails)):
        isItevenEmail = email_regex.match(emails[i])
        if isItevenEmail == None or False:
            countOfBad += 1
            print(Fore.MAGENTA + f'{emails[i]} even is not an email')
        else:
            response = requests.get(
                "https://isitarealemail.com/api/email/validate",
                params = {'email': emails[i]},
                headers = {'Authorization': "Bearer " + api_key })

            status = response.json()['status']
            if status == "valid":
                with open('good-emails.txt', 'a') as f:
                    f.write(emails[i]+'\n')
                print(Fore.GREEN + emails[i] + Style.RESET_ALL)
                countOfGood += 1
            elif status == "invalid":
                countOfBad += 1
                print(Fore.RED + f"{emails[i]} is invalid" + Style.RESET_ALL)
            else:
                countOfBad += 1
                print(Fore.BLUE + f"{emails[i]} was unknown" + Style.RESET_ALL)
    print(f'Program is finished, you can look valide emails in good-emails.txt\n{Fore.RED}Bad emails: {countOfBad}\n{Fore.GREEN}Good emails: {countOfGood}')
    input('Enter to close program')



def generateAndCheckEn(count):
    for i in range(0, int(count)):
        name = names.get_first_name()
        year = random.randint(1979, 2003)
        surname = names.get_last_name()
        domains = ['gmail.com', 'yahoo.com', 'aol.com', 'yandex.ru', 'mail.ru', 'hotmail.com', 'outlook.com']
        email = f'{name}{surname}{year}@{domains[random.randint(0, len(domains) - 1)]}'.lower()
        f = open('emails.txt', 'a')
        f.write(email+'\n')

    f.close()
    print(f'Successfully {count} emails were created!')
    decision = input('Do you want to check them? y\\n\n')
    a = False
    while a == False:
        if decision == 'y':
            emails = open('emails.txt', 'r').read().split('\n')
            countOfGood = 0
            countOfBad = 0

            api_key = input('Enter an API of isitarealemail.com: ')
            for o in range(0, len(emails)):
                response = None
                try:
                    response = requests.get(
                        "https://isitarealemail.com/api/email/validate",
                        params = {'email': emails[o]},
                        headers = {'Authorization': "Bearer " + api_key })
                    status = response.json()['status']
                    if status == "valid":
                        with open('good-emails.txt', 'a') as f:
                            f.write(emails[o]+'\n')
                        print(Fore.GREEN + emails[i] + Style.RESET_ALL)
                        countOfGood += 1
                    elif status == "invalid":
                        countOfBad += 1
                        print(Fore.RED + f"{emails[o]} is invalid" + Style.RESET_ALL)
                    else:
                        countOfBad += 1
                        print(Fore.BLUE + f"{emails[o]} was unknown" + Style.RESET_ALL)
                except:
                    print('Try to use VPN, or speed up your internet connection', status)

            print(f'Program is finished, you can look valide emails in good-emails.txt\n{Fore.RED}Bad emails: {countOfBad}\n{Fore.GREEN}Good emails: {countOfGood}')
            exit()
            a == True
        elif decision == 'n':
            a = True
            exit()
        else:
            print('Wrong answer! Please write y or n')
            a = True