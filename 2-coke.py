# it cost 50 cents and the machine acceps only coins of 0.05, 0.10 e 0.15

def main():
    troco=-come_dinheiro()
    print(f"Changed Owed: {troco}$")
   

def come_dinheiro():
    preco=float("0.5")
    while preco>0:
        print(f"Amount Due: {preco}$")
        metido=float(input(f"Insert Coin: "))
        if metido in [0.05,0.1,0.15]:
            preco=round(preco-metido,2)
            
    return preco

main()


            
    
