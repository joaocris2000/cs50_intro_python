#indicar a percentagem no deposito

while True:
    gasoleo=input("Whats the fraction ")
    try:
        x,y=gasoleo.split("/")
        x=int(x)
        y=int(y)
        deposito=x/y
        if 0<=deposito<=1:
            break

    except ZeroDivisionError:
        True
    except ValueError:
        True

if deposito>0.99:
    print("F")
elif deposito<0.01:
    print("E")
else:
    print(f"{deposito:.2f}%")