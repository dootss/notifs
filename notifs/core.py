from colorama import Fore, Style, init


init(autoreset=True)

SUPPORTED_COLORS = {
    'red'     : Fore.RED,
    'green'   : Fore.GREEN,
    'yellow'  : Fore.YELLOW,
    'blue'    : Fore.BLUE,
    'magenta' : Fore.MAGENTA,
    'cyan'    : Fore.CYAN,
    'white'   : Fore.WHITE,
}

def get_supported_colors():
    """Return a list of supported color names."""
    return list(SUPPORTED_COLORS.keys())

def notif(text, symbol='!', color='yellow', style='symbol'):
    """Display a notification with a given text, symbol, color, and style.

    Args:
        text (str): The text to display.
        symbol (str): The symbol to prefix the text with.
        color (str): The name of the color to use. Must be one of the supported colors.
        style (str): The style of coloring ('full', 'partial', or 'symbol').
    """
    color = color.lower()
    if color not in SUPPORTED_COLORS:
        raise ValueError(f"Invalid color '{color}'. Supported colors are: {get_supported_colors()}")
    color_code = SUPPORTED_COLORS[color]

    if style   == 'full':
        message = f"{color_code}[{symbol}] {text}{Style.RESET_ALL}"
    elif style == 'partial':
        message = f"{color_code}[{symbol}]{Style.RESET_ALL} {text}"
    elif style == 'symbol':
        message = f"[{color_code}{symbol}{Style.RESET_ALL}] {text}"
    else:
        # fake list to look like the invalid color valueError
        raise ValueError("Invalid style. Supported styles are: ['full', 'partial', 'symbol']")

    print(message)