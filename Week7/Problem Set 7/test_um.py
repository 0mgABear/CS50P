from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3
    assert count("Um, um, UM") == 3

def test_um_in_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("Um, thanks for the album.") == 1

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("um...") == 1
    assert count("um, um...") == 2

def test_um_with_other_words():
    assert count("hello, um, world") == 1
    assert count("um, thanks, um...") == 2
    assert count("Um, thanks, um...") == 2

if __name__ == "__main__":
    test_single_um()
    test_multiple_ums()
    test_um_in_words()
    test_um_with_punctuation()
    test_um_with_other_words()
    print("All tests passed!")
