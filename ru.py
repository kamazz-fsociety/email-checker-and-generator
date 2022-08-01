import requests
from colorama import init, Fore, Style
import names
import re
import random
init(convert=True)




def checkRu():
    countOfGood = 0
    countOfBad = 0
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    api_key = input('Введите API сайта isitarealemail.com: ')
    try:
        emailFile = input("Введите путь к txt файлу с почтами: ")
    except:
        print(Fore.RED + 'Неверный путь до файла!')

    emails = open(str(emailFile), 'r').read().split('\n')


    for i in range(0, len(emails)):
        isItevenEmail = email_regex.match(emails[i])
        if isItevenEmail == None or False:
            countOfBad += 1
            print(Fore.MAGENTA + f'{emails[i]} это даже не элэктронная почта')
        else:
            response = requests.get(
                "https://isitarealemail.com/api/email/validate",
                params = {'email': emails[i]},
                headers = {'Authorization': "Bearer " + api_key })

            status = response.json()['status']
            if status == "valid":
                with open('good-emails.txt', 'a') as f:
                    f.write(emails[i]+'\n')
                print(Fore.GREEN + f"Валидная почта: {emails[i]}" + Style.RESET_ALL)
                countOfGood += 1
            elif status == "invalid":
                countOfBad += 1
                print(Fore.RED + f"Невалидная почта: {emails[i]}" + Style.RESET_ALL)
            else:
                countOfBad += 1
                print(Fore.BLUE + f"Неизвестная почта: {emails[i]}" + Style.RESET_ALL)
    print(f'Программа закончена, вы можете посмотреть валидные почты в txt файле good-emails.txt\n{Fore.RED}Кол.Невалидных почт: {countOfBad}\n{Fore.GREEN}Кол.Валидных почт: {countOfGood}')
    input('Нажмите Enter чтобы закрыть программу')



def generateAndCheckRu(count):
    for i in range(0, int(count)):
        name = names.get_first_name()
        year = random.randint(1979, 2003)
        surname = names.get_last_name()
        domains = ['gmail.com', 'yahoo.com', 'aol.com', 'yandex.ru', 'mail.ru', 'hotmail.com', 'outlook.com']
        email = f'{name}{surname}{year}@{domains[random.randint(0, len(domains) - 1)]}'.lower()
        f = open('emails.txt', 'a')
        f.write(email+'\n')

    f.close()
    print(f'Было успешно создано {count} почт!')
    decision = input('Хотите проверить их? y\\n\n')
    a = False
    while a == False:
        if decision == 'y':
            emails = open('emails.txt', 'r').read().split('\n')
            countOfGood = 0
            countOfBad = 0

            api_key = input('Введите API сайта isitarealemail.com: ')
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
                        print(Fore.RED + f"Невалидная почта: {emails[o]}" + Style.RESET_ALL)
                    else:
                        countOfBad += 1
                        print(Fore.BLUE + f"Неизвестная почта: {emails[o]}" + Style.RESET_ALL)
                except:
                    print('Попробуй использовать VPN, или ускорь свой интернет', status)

            print(f'Программа закончена, вы можете посмотреть валидные почты в txt файле good-emails.txt\n{Fore.RED}Кол.Невалидных почт: {countOfBad}\n{Fore.GREEN}Кол.Валидных почт: {countOfGood}')
            exit()
            a == True
        elif decision == 'n':
            a = True
            exit()
        else:
            print('Неверный ответ, пожалуйста введите y или n')
            a = True