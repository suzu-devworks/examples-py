"""This test is for learning "native" datetime manipulation.

A naive object does not contain enough information
to unambiguously locate itself relative to other date/time objects.
"""

from datetime import UTC, date, datetime, time, timedelta


def test_native_datetime_generators() -> None:
    # datetime (naive)
    now = datetime.now()
    assert isinstance(now, datetime)
    assert now.tzinfo is None

    utc = datetime.now(UTC)
    assert isinstance(utc, datetime)
    assert utc.tzinfo is not None

    today = datetime.today()
    assert isinstance(today, datetime)
    assert utc.tzinfo is not None

    # date
    today_date = date.today()
    assert isinstance(today_date, date)

    now_date = datetime.now().date()
    assert isinstance(now_date, date)

    # datetime.time (naive)
    now_time = datetime.now().time()
    assert isinstance(now_time, time)
    now_time.tzinfo is None


def test_native_datetime_properties() -> None:
    # fixed datetime
    fixed = datetime(2021, 7, 31, 12, 34, 56, 789012)
    assert fixed.year == 2021
    assert fixed.month == 7
    assert fixed.day == 31
    assert fixed.hour == 12
    assert fixed.minute == 34
    assert fixed.second == 56
    assert fixed.microsecond == 789012

    assert fixed.weekday() == 5  # sat = 5.
    assert fixed.timestamp() == 1627734896.789012

    # fixed date
    fixed_date = date(2000, 2, 29)
    assert fixed_date.min == date(1, 1, 1)
    assert fixed_date.max == date(9999, 12, 31)
    assert fixed_date.year == 2000
    assert fixed_date.month == 2
    assert fixed_date.day == 29

    # fixed date
    fixed_time = time(12, 34, 56, 789012)
    assert fixed_time.min == time()
    assert fixed_time.max == time(23, 59, 59, 999999)
    assert fixed_time.hour == 12
    assert fixed_time.minute == 34
    assert fixed_time.second == 56
    assert fixed_time.microsecond == 789012


def test_native_datetime_calculation() -> None:
    datetime1 = datetime(2000, 2, 29, 12, 34, 56, 789012)

    # datetime2 = datetime1 + timedelta
    datetime2 = datetime1 + timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == datetime(2000, 3, 1, 14, 35, 26, 789012)

    # datetime2 = datetime1 - timedelta
    datetime2 = datetime1 - timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == datetime(2000, 2, 28, 10, 34, 26, 789012)

    # timedelta = datetime1 - datetime2
    timedelta1 = datetime1 - datetime(2000, 4, 2, 12, 34, 56, 789012)
    assert timedelta1 == timedelta(days=-33)

    # datetime1 < datetime2
    actual = datetime1 < datetime(2000, 4, 2, 12, 34, 56, 789012)
    assert actual is True


def test_native_datetime_conversion_with_string() -> None:
    datetime1 = datetime(2000, 2, 29, 1, 23, 45, 678901)

    # convert datetime to string(ISO8601)
    iso8601 = datetime1.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901"

    # convert string(ISO8601) to datetime
    datetime2 = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S.%f")
    assert datetime2 == datetime1

    # convert datetime to string
    text = datetime1.strftime("%Y/%m/%d %H:%M:%S")
    assert text == "2000/02/29 01:23:45"
