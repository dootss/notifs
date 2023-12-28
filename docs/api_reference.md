# API Reference

Notifs provides a simple API to display notifications with various styles and colors.

## notif

Display a customizable notification.

**Arguments**:

- `text` (str): The text message to display.

- `symbol` (str, optional): The symbol to display at the beginning of the message. Defaults to '!'.

- `color` (str, optional): The color of the message. Supported colors: red, green, yellow, blue, magenta, cyan, white. Defaults to 'yellow'.

- `style` (str, optional): The style of the notification. Options are 'full', 'partial', 'symbol'. Defaults to 'symbol'.

**Example**:
TODO
```py
from notifs import notif

notif("Hello, World!", symbol='*', color='green', style='full')
```

This will display the message "Hello, World!" with a green asterisk and green text.