import random

def main():
    level=get_level()
    the_integer=get_random(level)
    the_guess=guess_number(level)
    resultado(the_integer, the_guess)


def get_level():
    while True:
        try:
            number=int(input("Level: "))
            if number>0:
                return  number
        except ValueError:
            True

def get_random(jj):
    possibilities=[]
    k=1
    while k<=jj:
        possibilities.append(k)
        k=k+1
    rand_number=random.choice(possibilities)
    return rand_number

def guess_number(gg):
    while True:
        try:
            number=int(input("Guess: "))
            if 0<number<=gg:
                return  number
        except ValueError:
            True

def resultado(a,b):
    if a>b:
        print("Too small!")
    elif a<b:
        print("Too Large!")
    else:
        print("Just right!")
main()
