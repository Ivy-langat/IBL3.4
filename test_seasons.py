from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("2000-09-08")== ("2000","09","08")
    assert check_birthday("2000-9-8")== None

if __name__ == "__main__":
    main()