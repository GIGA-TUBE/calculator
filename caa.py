class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + bcolors.BOLD + "Hello I am you calculator" + bcolors.ENDC)
button_first = input(bcolors.OKBLUE + bcolors.BOLD + "Type First Number: " + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + "You chose " + button_first + bcolors.ENDC)
button_second = input(bcolors.OKBLUE + bcolors.BOLD + "Type Second Number: " + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + "You chose " + button_second + bcolors.ENDC)
button_third = input(bcolors.OKBLUE + bcolors.BOLD + "Type + - * or /: " + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + "You chose " + button_third + bcolors.ENDC)
if button_third == "+":
    number1 = int(button_first) + int(button_second)
    print(bcolors.OKBLUE + bcolors.BOLD + "You got: " + str(number1) + bcolors.ENDC)
elif button_third == "-":
    number2 = int(button_first) - int(button_second)
    print(bcolors.OKBLUE + bcolors.BOLD + "You got: " + str(number2) + bcolors.ENDC)
elif button_third == "*":
    number3 = int(button_first) * int(button_second)
    print(bcolors.OKBLUE + bcolors.BOLD + "You got: " + str(number3) + bcolors.ENDC)
elif button_third == "/":
    number4 = int(button_first) / int(button_second)
    print(bcolors.OKBLUE + bcolors.BOLD + "You got: " + str(number4) + bcolors.ENDC)