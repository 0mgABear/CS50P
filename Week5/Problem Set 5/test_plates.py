from plates import is_valid

def test_plate_start():
    assert is_valid('CS50') == True
    assert is_valid('C50') == False
    assert is_valid("H") == False

def test_plate_numbers():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_plate_end():
    assert is_valid('CS50P') == False

def test_plate_contents():
    assert is_valid("P13.14") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS@50") == False

def test_plate_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

def test_plate_zeros():
    assert is_valid("AB0") == False
    assert is_valid("AB50") == True
