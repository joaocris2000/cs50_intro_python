import sys
from PIL import Image
from PIL import ImageOps
import os.path

def main():
    # check the arguments
    is_it_possilbe()

    #import images
    try:
        image_person=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Item does not exist")
    image_shirt=Image.open("shirt.jpg")

    #crop the person image to shirt size
    size=image_shirt.size
    image_person=ImageOps.fit(image_person, size)  #resto default

    #overlay the shirt on the person
    image_person.paste(image_shirt,mask=image_shirt)

    #save the result
    image_person.save((sys.argv[2]))


def is_it_possilbe():
    try:
        lala=sys.argv[3]
        sys.exit("To many arguments")
    except IndexError:
        sys.argv[1].strip().lower()
        sys.argv[1].strip().lower()
        root_i,ext_i=os.path.splitext(sys.argv[1])
        root_o,ext_o =os.path.splitext(sys.argv[2])
    if ext_i!=ext_o:
        sys.exit("Input and output have different extensions")

if __name__=="__main__":
    main()