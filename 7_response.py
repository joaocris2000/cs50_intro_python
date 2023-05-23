import validator_collection
from validator_collection import validators

def main():
    print(validation(input("Whats the email? ")))

def validation(email):
    try:
        validator_collection.email(email)
        return "Valid"
    except validator_collection.errors.InvalidEmailError:
        return "Invalid"
if __name__=="__main__":
    main()
