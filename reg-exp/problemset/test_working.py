from working import convert


def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_pm_to_am():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"


def test_am_to_am():
    assert convert("8:30 AM to 11:45 AM") == "08:30 to 11:45"


def test_pm_to_pm():
    assert convert("1:15 PM to 11:30 PM") == "13:15 to 23:30"
