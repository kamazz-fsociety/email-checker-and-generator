from en import generateAndCheckEn, checkEn
from ru import generateAndCheckRu, checkRu
from colorama import init, Fore, Style



if __name__ == '__main__':
	print(Fore.MAGENTA + """
██████╗░██╗░██████╗░██╗░░██╗████████╗  ██████╗░███████╗░█████╗░██╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██║██╔══██╗████╗░██║
██████╔╝██║██║░░██╗░███████║░░░██║░░░  ██║░░██║█████╗░░██║░░╚═╝██║╚█████╗░██║██║░░██║██╔██╗██║
██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░  ██║░░██║██╔══╝░░██║░░██╗██║░╚═══██╗██║██║░░██║██║╚████║
██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░  ██████╔╝███████╗╚█████╔╝██║██████╔╝██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚══════╝░╚════╝░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝
						Telegram(https://t.me/+fN7NR-nVvmsxYWRi)

							Email Verifier and Generater - Чекер Почт и Генератор
""" + Style.RESET_ALL)
	print(Fore.GREEN + '1 - English\n2 - Русский' + Style.RESET_ALL)
	
	lang = input('Enter number to select language | Введите число чтобы выбрать язык: ')

	if lang == "1":
		print(f'What do you want to do?\n{Fore.GREEN}1) Check your emails from txt\n2) Generate my own txt file with emails and check them')
		mode = input("Enter number to select mode: ")
		if mode == "1":
			checkEn()
		elif mode == "2":
			count = input('How many emails do you want to generate?\n')
			try:
				int(count)
				generateAndCheckEn(count=count)
			except:
				print('Enter count in numbers!')
		else:
			print('You should enter numbers(1 or 2)')


	elif lang == "2":
		print(f'Что хотите сделать?\n{Fore.GREEN}1) Проверить ваши почты с txt файла\n2) Генерировать новые почты и проверить их')
		mode = input("Введите число чтобы выбрать: ")
		if mode == "1":
			checkRu()
		elif mode == "2":
			count = input('Сколько почт вы хотите сгенирировать?\n')
			try:
				int(count)
				generateAndCheckRu(count=count)
			except:
				print('Введите количество в цифрах!')
		else:
			print('Вы должны ввести цифру (1 или 2)!')
	else:
		print('Enter number to choose a language! 1 or 2| Вводите число для выбора языка! 1 или 2')