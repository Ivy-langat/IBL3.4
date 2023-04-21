from um import count

def main():
    test_lower_case()
    test_word_with_um()


def test_lower_case():
    assert count("um, hi.")==1
    assert count("um, hi, um.")== 2

def test_word_with_um():
    assert count("yumi")==0

if __name__ == "__main__":
    main()   