

try:
    i=0
    namesz=[]
    while i==0:
        new_name=input("Name: ")
        namesz.append(new_name)  


except EOFError:    #control+z+enter
    if len(namesz)==1:
        print(f"Adieu, adieu, to {namesz[0]}")
    else:
        print("Adieu, adieu, to ", end="")
        for p in range (len(namesz)-1):
            print(f"{namesz[p]}, ", end="")
        print(f"and {namesz[p+1]}")
