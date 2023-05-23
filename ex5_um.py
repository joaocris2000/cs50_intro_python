import re

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(r"\b[Uu]m\b",s))

if __name__ == "__main__":
    main()
