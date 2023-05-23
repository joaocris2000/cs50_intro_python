import sys
import os.path
import csv

def main():
    is_it_possible()
    students_before=[]
    #import from csv
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_before.append({"name": row["name"], "house": row["house"]})

    #spliting names, creating new dict
    students_after=[]
    for row in students_before:
        last,first=row["name"].split(",")
        students_after.append({"first":first,"last":last,"house":row["house"]})


    #order from the first name
    #save in the final csv
    with open(sys.argv[2], "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last", "house"])
        writer.writerow({"first": "first", "last": "last", "house":"house"})
        for row in sorted(students_after, key=lambda row: row["first"]):
            writer.writerow({"first": row["first"].strip(), "last":row["last"], "house":row["house"]})

def is_it_possible():
    try:
        lala=sys.argv[3]
        sys.exit("Too many command-line arguments ")
    except IndexError:
       try:
           root1,ext1 =os.path.splitext(sys.argv[1])
           root2, ext2 = os.path.splitext(sys.argv[2])
       except IndexError:
           sys.exit("To few command line arguments")
    if ext1!=".csv" or ext2!=".csv":
        sys.exit("Not a CSV file")

if __name__=="__main__":
    main()
