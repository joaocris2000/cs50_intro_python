#removes vowels

def main():
    ff=input("INPUT: ")
    print("OUTPUT: ", end="")
    remove_vowals(ff)

def remove_vowals(word):
    for c in word:
        match c.lower():
            case "a"|"e"|"i"|"o"|"u":
                print("", end="")
            case _:
                print(c, end="")

main()
