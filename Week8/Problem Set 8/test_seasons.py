from seasons import convert

def test_date():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(0) == "Zero minutes"
    assert convert(1) == "One thousand, four hundred forty minutes"
    assert convert(30) == "Forty-three thousand, two hundred minutes"
    assert convert(10000) == "Fourteen million, four hundred thousand minutes"
