import crayons
from random import randint

arch_tools_logo = """
 █████╗ ██████╗  ██████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██████╔╝██║     ███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██╔══██╗██║     ██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║  ██║╚██████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
"""

arch_logo = """
      /\\      
     /**\\     
    /****\\    
   /******\\   
  /***,,***\\  
 /***|  |**-\\ 
/_-''    ''-_\\
"""


def colorize(text):
    """Pass a block of ascii art here to color them by rows."""

    lines = text.split('\n')
    del lines[0]
    string = ''
    count = 0
    maximum = 5
    for i in range(len(lines)):
        if count == 0:
            string += crayons.red(lines[i] + '\n')
        elif count == 1:
            string += crayons.magenta(lines[i] + '\n')
        elif count == 2:
            string += crayons.blue(lines[i] + '\n')
        elif count == 3:
            string += crayons.cyan(lines[i] + '\n')
        elif count == 4:
            string += crayons.green(lines[i] + '\n')
        elif count == maximum:
            string += crayons.yellow(lines[i] + '\n')
        count = count + 1 if count < maximum else 0

    return string


def make_div(sym, length, col):
    """Makes a colored divider for console output"""
    div = ''
    if col == 'red':
        div = crayons.red(f'{sym[0] * length}')
    elif col == 'blue':
        div = crayons.blue(f'{sym[0] * length}')
    elif col == 'cyan':
        div = crayons.cyan(f'{sym[0] * length}')
    elif col == 'green':
        div = crayons.green(f'{sym[0] * length}')
    elif col == 'magenta':
        div = crayons.magenta(f'{sym[0] * length}')
    elif col == 'yellow':
        div = crayons.yellow(f'{sym[0] * length}')
    else:
        div = f'{sym[0] * length}'
    return div


def random_color():
    colors = {
        0: "red",
        1: "blue",
        2: "cyan",
        3: "green",
        4: "magenta",
        5: "yellow"
    }
    return colors[randint(0, 5)]


def dye(txt, col):
    """Colors text"""
    col = col.lower()
    if col == 'red':
        txt = crayons.red(txt)
    elif col == 'blue':
        txt = crayons.blue(txt)
    elif col == 'green':
        txt = crayons.green(txt)
    elif col == 'yellow':
        txt = crayons.yellow(txt)
    if col == 'magenta':
        txt = crayons.magenta(txt)
    elif col == 'cyan':
        txt = crayons.cyan(txt)
    return txt


def get_arch_logo():

    text = arch_tools_logo.split("\n")
    logo = arch_logo.split("\n")

    for index, line in enumerate(logo):

        if 0 < index < len(logo) - 1:
            print(dye(logo[index], "blue"), dye(text[index - 1], "green"))

        else:
            print(dye(logo[index], "blue"))

