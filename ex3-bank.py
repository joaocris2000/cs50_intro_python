# a multa a pagar se dizer hello é 0, se dizer algo que começa por h 20, se nenhum anterior 100

def main():
    greating=input("Hello!").strip().lower()    #retirar espaços brancos e tudo minusculo
    fine=banks(greating)
    print(f"{fine}$")

def banks(frase):
    test=frase[0:5]       #apenas os primeiros cinco caracteres
    if test=="hello":
        coima=0
    else:
        test=test[0:1]
        if test=="h":     #primeira letra do cumprimento é h
            coima=20
        else:
            coima=100
    return coima

main()

