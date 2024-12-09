"""This test is for learning "native" datetime manipulation.

A naive object does not contain enough information
to unambiguously locate itself relative to other date/time objects.

References:
    - https://docs.python.org/ja/3/library/datetime.html
"""

import calendar
from datetime import UTC, date, datetime, time, timedelta


def test_creation() -> None:
    """Create a native datetime in several ways."""

    # datetime (naive)

    now = datetime.now()
    assert isinstance(now, datetime)
    assert now.tzinfo is None

    utc = datetime.now(UTC)
    assert isinstance(utc, datetime)
    assert utc.tzinfo == UTC

    today = datetime.today()
    assert isinstance(today, datetime)
    assert today.tzinfo is None

    # date

    today_date = date.today()
    assert isinstance(today_date, date)

    now_date = datetime.now().date()
    assert isinstance(now_date, date)

    # datetime.time (naive)

    now_time = datetime.now().time()
    assert isinstance(now_time, time)
    assert now_time.tzinfo is None


def test_datetime_properties() -> None:
    """Accessing datetime properties."""

    # fixed datetime (naive)

    fixed_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901)

    assert fixed_datetime.year == 2000
    assert fixed_datetime.month == 2
    assert fixed_datetime.day == 29
    assert fixed_datetime.hour == 1
    assert fixed_datetime.minute == 23
    assert fixed_datetime.second == 45
    assert fixed_datetime.microsecond == 678901
    assert fixed_datetime.weekday() == 1  # man = 1.
    assert fixed_datetime.timestamp() == 951787425.678901
    assert fixed_datetime.tzinfo is None

    # fixed date

    fixed_date = date(2000, 2, 29)

    assert fixed_date.min == date(1, 1, 1)
    assert fixed_date.max == date(9999, 12, 31)
    assert fixed_date.year == 2000
    assert fixed_date.month == 2
    assert fixed_date.day == 29

    # fixed time (naive)

    fixed_time = time(1, 23, 45, 678901)

    assert fixed_time.min == time(0, 0, 0, 0)
    assert fixed_time.max == time(23, 59, 59, 999999)
    assert fixed_time.hour == 1
    assert fixed_time.minute == 23
    assert fixed_time.second == 45
    assert fixed_time.microsecond == 678901
    assert fixed_time.tzinfo is None


def test_calculation() -> None:
    """Calculate with datetime."""

    base_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901)

    # datetime = datetime + timedelta
    actual = base_datetime + timedelta(days=1, hours=2, seconds=30)
    assert actual == datetime(2000, 3, 1, 3, 24, 15, 678901)

    # datetime = datetime - timedelta
    actual = base_datetime - timedelta(days=1, hours=2, seconds=30)
    assert actual == datetime(2000, 2, 27, 23, 23, 15, 678901)

    # timedelta = datetime - datetime2
    actual = base_datetime - datetime(2000, 4, 2, 1, 23, 45, 678901)
    assert actual == timedelta(days=-33)

    # datetime (==|<|>) datetime
    assert base_datetime != datetime(2000, 2, 29, 1, 23, 45, 999999)
    assert base_datetime > datetime(2000, 2, 29, 1, 23, 44, 678901)
    assert base_datetime < datetime(2000, 2, 29, 1, 23, 46, 678901)


def test_conversion_string() -> None:
    """Converts between date and string types."""

    base_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901)

    # convert datetime to string(ISO8601)
    iso8601 = base_datetime.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901"

    # convert datetime from string(ISO8601)
    datetime2 = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S.%f")
    assert datetime2 == base_datetime

    # convert datetime to string
    text = base_datetime.strftime("%Y/%m/%d %H:%M:%S")
    assert text == "2000/02/29 01:23:45"


def test_gets_end_of_month() -> None:
    """End of month calculation."""

    base_datetime = datetime(2000, 2, 1, 1, 23, 45, 678901)
    _, last_day = calendar.monthrange(base_datetime.year, base_datetime.month)

    end_of_month = datetime.combine(datetime(base_datetime.year, base_datetime.month, last_day), time.max)
    assert end_of_month == datetime(2000, 2, 29, 23, 59, 59, 999999)
