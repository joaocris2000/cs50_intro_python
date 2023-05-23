#o utilizador põe o nome de ficheiro "blabla.ext" e diz o tipo
#deve ser insensivel a espaços e maiusculas

def main():
    file_name=input("File name: ").strip().lower()
    media_type=processo(file_name)
    print(media_type)

def processo(string):
    nome_ficheiro,extensao=string.split(".")
    match extensao:                #os casos a considerar
        case "gif":
            sentence="image/gif"
        case "jpeg":
            sentence="image/jpeg"
        case "jpg":
            sentence="image/jpeg"
        case "png":
            sentence="image/png"
        case "pdf":
            sentence="application/pdf"
        case "txt":
            sentence="text/plain"
        case "zip":
            sentence="application/zip"
        case _:
            sentence="application/octet-stream"
    return sentence

main()

