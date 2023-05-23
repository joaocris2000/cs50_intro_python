#acordingly with time ##:## says if its meal time

def main():
    time=input("What time is it? HH:MM ")
    time=convert(time)
    if 7<=time<=8:
            print("breakfast time")
    elif 12<=time<=13:
            print("lunch time")
    elif 18<=time<=19:
        print("dinner time")


def convert(tempo):
    horas,minutos=tempo.split(":")     #slit hour form minute
    horas=float(horas)                #turn str into float
    minutos=float(minutos)
    tempo_decimal=horas+(minutos/60)
    return tempo_decimal

main()
