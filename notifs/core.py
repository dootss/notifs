from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define a dictionary of colors
COLORS = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
}

def warn(text, symbol='!', color='red'):
    color_code = COLORS.get(color.lower(), Fore.WHITE)
    print(f"{color_code}[{symbol}]{Style.RESET_ALL} {text}")
