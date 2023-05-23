import sys
import os.path

def main():
    is_it_correct()
    i=0
    lines=[]
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line.strip()
                if line=="\n" or line.startswith("#"): #empty lines are signal with \n
                    i=i
                else:
                    lines.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

    num_lines=len(lines)
    print(num_lines)


def is_it_correct():
    try:
        lala=sys.argv[2]
        sys.exit("Too many command-line arguments ")
    except IndexError:
       root,ext =os.path.splitext(sys.argv[1])
    if ext!=".py":
        sys.exit("Not a Python file")

if __name__=="__main__":
    main()
