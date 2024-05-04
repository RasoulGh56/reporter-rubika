import os,platform

def Cl():
	if platform.uname()[0] == "Windows":os.system("cls")
	else:os.system("clear")
	
Cl()

try:import pyrubi
except:os.system("pip install pyrubi")
try:import pyfiglet
except:os.system("pip install pyfiglet")
try:import colorama
except:os.system("pip install colorama")

import pyrubi,pyfiglet,colorama,time

bot = pyrubi.Client("P-D99999")
font = pyfiglet.Figlet()
n = 0
Cl()

print(colorama.Fore.LIGHTBLACK_EX+font.renderText(" RASOUL "))
print(colorama.Fore.CYAN+" Dev >>> @Rasoul_adz\n\n");time.sleep(1)

Ty = input(f" {colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.GREEN}1{colorama.Fore.LIGHTBLACK_EX}] {colorama.Fore.LIGHTCYAN_EX}Repor User Rubika\n{colorama.Fore.LIGHTBLACK_EX} [{colorama.Fore.GREEN}2{colorama.Fore.LIGHTBLACK_EX}] {colorama.Fore.LIGHTCYAN_EX}Repor Group Rubika\n{colorama.Fore.LIGHTBLACK_EX} [{colorama.Fore.GREEN}3{colorama.Fore.LIGHTBLACK_EX}] {colorama.Fore.LIGHTCYAN_EX}Repor Channel Rubika\n\n {colorama.Fore.LIGHTMAGENTA_EX}Selection : ")

Li = input(f" \n{colorama.Fore.YELLOW} Yor Link or ID : ")

if Ty == "2" or Ty == "۲" or Ty == "[2]":
	Get = bot.join_chat(Li)
	guid = Get['group']['group_guid']
	Name = Get['group']['group_title']
elif Ty == "3" or Ty == "۳" or Ty == "[3]":
	if Li.startswith("https://rubika.ir/joinc/"):
		Get = bot.join_chat(Li)
		guid = Get['channel']['channel_guid']
		Name = Get['channel']['channel_title']
	else:
		Get = bot.get_chat_info_by_username(Li)
		guid = Get['channel']['channel_guid']
		Name = Get['channel']['channel_title']
elif Ty == "1" or Ty == "۱" or Ty == "[1]":
	Get = bot.get_chat_info_by_username(Li)
	guid = Get['user']['user_guid']
	Name = Get['user']['first_name'] + Get['user']['last_name']
else:
	Cl()
	print(f"\n {colorama.Fore.RED} Not available !\n")
	
Te = input(f" \n{colorama.Fore.YELLOW} Yor description( code filteri ) : ")

Cl()

print(f" \n{colorama.Fore.LIGHTBLACK_EX} Name {colorama.Fore.BLUE}>{colorama.Fore.YELLOW}>{colorama.Fore.GREEN}> {colorama.Fore.LIGHTBLACK_EX}[{Name}]\n\n {colorama.Fore.LIGHTBLACK_EX}Guid {colorama.Fore.BLUE}>{colorama.Fore.YELLOW}>{colorama.Fore.GREEN}> {colorama.Fore.LIGHTBLACK_EX}{guid}\n\n")
time.sleep(1)
	
while True:
	try:
		bot.report_chat(guid,description=Te)
		n+=1
		print(f"{colorama.Fore.LIGHTBLACK_EX} Report {colorama.Fore.GREEN}OK {colorama.Fore.BLUE}[{colorama.Fore.LIGHTBLACK_EX}{n}{colorama.Fore.BLUE}]")
	except:pass