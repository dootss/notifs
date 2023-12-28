SUPPORTED_COLORS = {
    'red'     : '\033[31m',
    'green'   : '\033[32m',
    'yellow'  : '\033[33m',
    'blue'    : '\033[34m',
    'magenta' : '\033[35m',
    'cyan'    : '\033[36m',
    'white'   : '\033[37m',
}

RESET = "\033[0m"

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
        message = f"{color_code}[{symbol}] {text}{RESET}"
    elif style == 'partial':
        message = f"{color_code}[{symbol}]{RESET} {text}{RESET}"
    elif style == 'symbol':
        message = f"[{color_code}{symbol}{RESET}] {text}{RESET}"
    else:
        # fake list to look like the invalid color valueError
        raise ValueError(f"Invalid style '{style}'. Supported styles are: ['full', 'partial', 'symbol']")

    print(message)