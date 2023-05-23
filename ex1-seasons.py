from datetime import datetime
import re
import sys
import inflect
p=inflect.engine()

def main():
    c_date=datetime.today()
    b_date=get_date()
    delta=c_date-b_date
    sing(delta.days)

def get_date():
    date=input("b-day: ")
    matches = re.search(r"((?:1|2)\d\d\d)-(0\d|1[012])-([012]\d|3[01])", date)
    if matches:
        return datetime(int(matches.group(1)),int( matches.group(2)), int(matches.group(3)))
    else:
        sys.exit("Invalid date")

def sing(d):
    print(p.number_to_words(d))

if __name__ == "__main__":
    main()
