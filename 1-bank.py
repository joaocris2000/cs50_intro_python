# fine to pay if says "hello" is zero
# if starts with "h..." is 20
#else its 100
def main():
    greating=input("Hello!").strip().lower()    #remove all whitespace and lowercase
    fine=banks(greating)
    print(f"{fine}$")

def banks(frase):
    test=frase[0:5]       #just the first 5 charcaters
    if test=="hello":
        coima=0
    else:
        test=test[0:1]
        if test=="h":     #first letter is "h"
            coima=20
        else:
            coima=100
    return coima

main()

