
import pytest
from datetime import date, timedelta
from date import minutes_lived


def test_one_day():
    birthday = (date.today() - timedelta(days=1)).isoformat()
    assert minutes_lived(birthday) == "One thousand, four hundred forty minutes"


def test_one_week():
    birthday = (date.today() - timedelta(days=7)).isoformat()
    assert minutes_lived(birthday) == "Ten thousand eighty minutes"


def test_one_year():
    birthday = (date.today() - timedelta(days=365)).isoformat()
    assert minutes_lived(birthday) == "Five hundred twenty-five thousand, six hundred minutes"


def test_invalid_format():
    with pytest.raises(SystemExit):
        minutes_lived("October 15, 2000")


def test_invalid_date():
    with pytest.raises(SystemExit):
        minutes_lived("2025-13-40")


def test_future_date():
    birthday = (date.today() + timedelta(days=1)).isoformat()
    with pytest.raises(SystemExit):
        minutes_lived(birthday)
