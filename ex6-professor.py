import random

def main():
    level=get_level()
    integers=generate_integer(level)
    righ_aws=play_game(integers)
    print("Score: ", righ_aws)

def get_level():
    levels=[1,2,3]
    while True:
        level=int(input("Level: "))
        if level in levels:
            return level

def generate_integer(level):
    num_list=[]
    if level==1:
        h=1
        while h<10:
            num_list.append(h)
            h=h+1

    elif level==2:
        h = 10
        while h < 100:
            num_list.append(h)
            h = h + 1

    else:    #level==3
        h = 100
        while h < 1000:
            num_list.append(h)
            h = h + 1

    return num_list

def play_game(num_list):
    i=0
    points=0
    while i<10:
        try:
            x=random.choice(num_list)
            y=random.choice(num_list)
            print(x,"+",y,"=", end="")
            awns=int(input())
            if awns!=(x+y):
                raise ValueError
            i=i+1
            points=points+1
        except ValueError:
            print("EEE")
            i=i+1

    return points
if __name__ == "__main__":
    main()
