#validate if it is IP adress
# its like -> #.#.#.#

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches:=re.search(r"^(1?\d?\d\.|2[0-6]\d\.|27[0-5]\.){3}(1?\d?\d|2[0-6]\d|27[0-5])$",ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
