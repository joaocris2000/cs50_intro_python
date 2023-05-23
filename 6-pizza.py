import csv
import sys
import os.path
import tabulate

def main():
    is_it_correct()
    pizzas=[]
    #import info
    try:
        with open(sys.argv[1], newline="") as file:
            reader=csv.reader(file)
            for row in reader:
                pizzas.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
        
    print(tabulate.tabulate(pizzas,headers="firstrow", tablefmt="grid"))


def is_it_correct():
    try:
        lala=sys.argv[2]
        sys.exit("Too many command-line arguments ")
    except IndexError:
       root,ext =os.path.splitext(sys.argv[1])
    if ext!=".csv":
        sys.exit("Not a CSV file")

if __name__=="__main__":
    main()
