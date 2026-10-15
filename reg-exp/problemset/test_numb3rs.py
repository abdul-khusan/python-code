from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True

def test_invalid():
    assert validate("256.168.1.1") == False
    assert validate("192.168.1") == False