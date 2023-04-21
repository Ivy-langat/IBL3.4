from validator_collection import validators

def main():
    email_address =input("what is your email address? ")
    try:
        emailisvalid= validators.email(email_address)
        print("valid")

    except:
        print("invalid")

if __name__ == "__main__":
    main()