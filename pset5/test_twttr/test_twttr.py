from twttr import shorten


def test_twttr():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("aouiet") == "t"
    assert shorten("The.") == "Th."
    assert shorten("12hjav") == "12hjv"
