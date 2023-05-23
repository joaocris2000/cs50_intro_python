import sys
from pyfiglet import Figlet
figlet=Figlet()
from random import choice

def main():
    try:
        if sys.argv[1]=="-f" or sys.argv=="--font":
            if sys.argv[2] in figlet.getFonts():
                define_font(sys.argv[2])
                the_string=get_string()
                print_figlet(the_string)
            else:
                prog_fail()
        else:
            prog_fail()

    except IndexError:
        list_of_fonts = figlet.getFonts()
        the_string = get_string()
        define_font(choice(list_of_fonts))
        print_figlet(the_string)


def get_string():
    bb=input("Input: ")
    return bb

def prog_fail():
    sys.exit("Invalid usage")

def define_font(jj):
    figlet.setFont(font=jj)

def print_figlet(nn):
    print("Output:", figlet.renderText(nn))


main()
