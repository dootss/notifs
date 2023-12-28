from notifs import notif

# Default notification
notif("nothing changed.")

# Custom symbol
notif("symbol *.", symbol='*')

# Custom color
notif("color blue.", color='blue')

# Full style with custom color and symbol
notif("symbol >, color green, style full.", symbol='>', color='green', style='full')

# Partial style with custom color and symbol
notif("symbol >>, color magenta, style partial.", symbol='>>', color='magenta', style='partial')

# Symbol style (default) with custom color and symbol
# and a prettier way of formatting it
notif(
    "symbol !, color cyan, style symbol.",
    symbol='!',
    color='cyan',
    style='symbol'
    )

# Missing style (defaults to symbol style)
notif("symbol @, color red, missing style.", symbol='@', color='red')

# funny symbol demo
notif("anything you want", symbol="you can set the symbol to")

# Invalid color, should raise ValueError
try:
    notif("Invalid color provided.", color='invalid_color')
except ValueError as e:
    notif(e)

# Invalid style, should raise ValueError
    # we also pass it through another notif here lol, same above
try:
    notif("Invalid style provided.", style='invalid_style')
except ValueError as e:
    notif(e)