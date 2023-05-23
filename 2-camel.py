#transforms camle (firstName) into snake (first_Name)

def main():
    ff=input("insert your camel sentence ")
    camel_to_snake(ff)

def camel_to_snake(camel):
    for c in camel:
        if c.islower():
            print(c, end="")
        else:
            c=c.lower()
            print(f"_{c}", end="")

main()
