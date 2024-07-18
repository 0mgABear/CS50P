from twttr import shorten

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("12345") == "12345"
    assert shorten("Hello, World!") == "Hll, Wrld!"
