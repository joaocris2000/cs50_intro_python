#validar matriculas com as regras do machachutest

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   
    if 2<= len(s)<=6:   #cond2: ter 2 a 6 caracteres
        if s[0].isalpha() and s[1].isalpha():         #cond1: as duas primeiras são letras
           
            i=1
            w=0
            while i<len(s):  #cond3: os numeros têm que estar no final
                t=i-1        
                if s[t].isnumeric() and s[i].isalpha():
                    w=w+1
                i=i+1
            
            if w<=0:
                
                h=1
                f=0
                while h<len(s):       #cond4: o primeiro numero não pode ser zero 
                    g=h-1
                    if s[h].isnumeric() and s[g]=="0":
                        f=f+1
                    h=h+1
                if f<=0:    #cond5: só  numeros e alphas
                    v=0
                    j=0
                    while j<len(s):
                        if s[j].isnumeric() or s[j].isalpha():
                           v=v+0
                        else:
                            v=v+1
                        j=j+1
                    if v<=0:
                        return True
                    else:
                        return False
                    
                else:                 
                    return False  
            else:
                return False
        else:
            return False
    else:
        return False
    


    


main()
