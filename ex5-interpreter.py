#é uma calcuadora para quem n ão sabe python

def main():
    expression=input("Expression:" )
    result=round(calc(expression), 1)
    print(result)

def calc(expr):
    
    x, y, z = expr.split(" ")
    x=float(x)
    z=float(z)
    match y:
        case "+":
            resl=x+z
        case "-":
            resl=x-z
        case"*":
            resl=x*z
        case"/":
            if y!=0:
                resl=x/z
            else:
                resl="impossivel"
    return resl


main()
