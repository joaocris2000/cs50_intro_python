import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches:=re.search(f"^(1?[012]|\d):([0-5][\d]) (AM|PM) to (1?[012]|\d):([0-5][\d]) (AM|PM)\s*$",s):
        if matches.group(3)=="AM":
            horas_primeiro=int(matches.group(1))
        else:
            horas_primeiro=int(matches.group(1))+12
        if matches.group(6)=="AM":
            horas_segundo=int(matches.group(4))
        else:
            horas_segundo=int(matches.group(4))+12
        minutos_primeiro = int(matches.group(2))
        minutos_segundo =int=(matches.group(5))
        hours = f"{horas_primeiro:02}" + f":{minutos_primeiro:02}" + " to " + f"{horas_segundo:02}" + f":{minutos_segundo:02}"
        return hours
    elif matches:=re.search(f"^(1?[012]|\d) (AM|PM) to (1?[012]|\d) (AM|PM)\s*$",s):
        if matches.group(2) == "AM":
            horas_primeiro = int(matches.group(1))
        else:
            horas_primeiro = int(matches.group(1)) + 12
        if matches.group(4) == "AM":
            horas_segundo = int(matches.group(3))
        else:
            horas_segundo = int(matches.group(3)) + 12
        minutos_primeiro = 0
        minutos_segundo = 0
        hours = f"{horas_primeiro:02}" + f":{minutos_primeiro:02}" + " to " + f"{horas_segundo:02}" + f":{minutos_segundo:02}"
        return hours
    else:
        return ValueError

if __name__ == "__main__":
    main()
