#if the users inputs 42, propms "yes"
def main():
    frase=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()
    resposta=sera_sera(frase)
    print(resposta)

def sera_sera(strg):
    match strg:
        case "42"|"forty-two"|"forty two":
            resp="Yes"
        case _:
            resp="No"
    return resp

main()
