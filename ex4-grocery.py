#lista de compras
list_gro = dict()
i=0

while True:
    try:
        item = input().upper()
        if item in list_gro:
            list_gro[item]=list_gro[item]+1
        else:
            list_gro[item]=1
            i=i+1

    except EOFError:    #control z enter
        ordered_list=sorted(list_gro.items())   #ordem alfabetica
       
        for d in ordered_list:
            print(d[0],d[1])
            
        break
