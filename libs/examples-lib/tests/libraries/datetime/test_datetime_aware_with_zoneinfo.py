"""This test is for learning "aware" datetime manipulation.

An aware objects have an optional time zone information attribute tzinfo
that can be set to an instance of a subclass of the abstract tzinfo class.

References:
    - https://docs.python.org/ja/3/library/zoneinfo.html
"""

from datetime import UTC, datetime, time, timedelta
from time import time as c_style_time
from typing import Any
from zoneinfo import ZoneInfo

import pytest

timezone_data = [
    ("UTC", datetime(2000, 2, 29), "UTC", timedelta(hours=0), timedelta(0)),
    ("Asia/Tokyo", datetime(2000, 2, 29), "JST", timedelta(hours=9), timedelta(0)),
    ("US/Pacific", datetime(2000, 2, 29), "PST", timedelta(hours=-8), timedelta(0)),
    ("US/Eastern", datetime(2000, 2, 29), "EST", timedelta(hours=-5), timedelta(0)),
    (
        "US/Eastern",
        datetime(2019, 3, 10, 3),
        "EDT",
        timedelta(hours=-4),
        timedelta(hours=1),
    ),
]


@pytest.mark.parametrize("zone,date,tzname,offset,dst", timezone_data)
def test_timezone_properties(zone: str, date: datetime, tzname: str, offset: timedelta, dst: timedelta) -> None:
    """Accessing timezone properties."""

    tz = ZoneInfo(zone)

    assert tz.key == zone
    assert tz.tzname(date) == tzname
    assert tz.utcoffset(date) == offset
    assert tz.dst(date) == dst


@pytest.fixture
def tz_ja() -> Any:
    return ZoneInfo("Asia/Tokyo")


def test_creation(tz_ja: Any) -> None:
    """Create a aware datetime in several ways."""

    # datetime (aware)

    now = datetime.now(tz=tz_ja)
    assert isinstance(now, datetime)
    assert now.tzinfo is not None
    assert now.tzinfo == tz_ja

    utc = datetime.now(tz=UTC)
    assert isinstance(utc, datetime)
    assert utc.tzinfo == UTC

    today = datetime.today().astimezone(tz_ja)
    assert isinstance(today, datetime)
    assert today.tzinfo == tz_ja

    fromtimestamp = datetime.fromtimestamp(c_style_time(), tz=tz_ja)
    assert isinstance(fromtimestamp, datetime)
    assert fromtimestamp.tzinfo == tz_ja

    # date

    # datetime.time (aware)

    now_tz_time = datetime.now(tz=tz_ja).time()
    assert isinstance(now_tz_time, time)
    assert now_tz_time.tzinfo is None

    now_tz_timetz = datetime.now(tz=tz_ja).timetz()
    assert isinstance(now_tz_timetz, time)
    assert now_tz_timetz.tzinfo == tz_ja


def test_calculation(tz_ja: Any) -> None:
    """Calculate with datetime."""

    base_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)

    # datetime(aware) = datetime(aware) + timedelta
    actual = base_datetime + timedelta(days=1, hours=2, seconds=30)
    assert actual == datetime(2000, 3, 1, 3, 24, 15, 678901, tzinfo=tz_ja)

    # datetime(aware) = datetime(aware) - timedelta
    actual = base_datetime - timedelta(days=1, hours=2, seconds=30)
    assert actual == datetime(2000, 2, 27, 23, 23, 15, 678901, tzinfo=tz_ja)

    # timedelta = datetime(aware) - datetime(aware)
    timedelta1 = base_datetime - datetime(2000, 4, 2, 1, 23, 45, 678901, tzinfo=tz_ja)
    assert timedelta1 == timedelta(days=-33)

    # timedelta = datetime(aware) - datetime(utc)
    timedelta1 = base_datetime - datetime(2000, 4, 2, 1, 23, 45, 678901, tzinfo=UTC)
    assert timedelta1 == timedelta(days=-34, hours=15)

    # timedelta = datetime(aware) - datetime(native)
    with pytest.raises(TypeError) as ex:
        base_datetime - datetime(2000, 2, 28, 10, 34, 26, 789012)
    assert str(ex.value) == "can't subtract offset-naive and offset-aware datetimes"

    # datetime (==|<|>) datetime
    assert base_datetime != datetime(2000, 2, 29, 1, 23, 45, 999999, tzinfo=tz_ja)
    assert base_datetime > datetime(2000, 2, 29, 1, 23, 44, 678901, tzinfo=tz_ja)
    assert base_datetime < datetime(2000, 2, 29, 1, 23, 46, 678901, tzinfo=tz_ja)


def test_conversion_string(tz_ja: Any) -> None:
    """Converts between date and string types."""

    base_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)

    # convert datetime to string(ISO8601)
    iso8601 = base_datetime.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901+09:00"

    iso8601utc = base_datetime.astimezone(UTC).isoformat().replace("+00:00", "Z")
    assert iso8601utc == "2000-02-28T16:23:45.678901Z"

    # convert datetime from string(ISO8601)
    datetime2 = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S.%f%z")
    assert datetime2 == base_datetime

    datetime2 = datetime.strptime(iso8601utc, "%Y-%m-%dT%H:%M:%S.%f%z")
    assert datetime2 == base_datetime

    # convert datetime to string
    text = base_datetime.strftime("%Y/%m/%d %H:%M:%S %z %Z")
    assert text == "2000/02/29 01:23:45 +0900 JST"
    assert text != "2000/02/29 01:23:45 +09:00 JST"


def test_conversion_timezone_utc(tz_ja: Any) -> None:
    """Converts between JST and UTC timezone."""

    datetime1 = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)

    # convert JST -> UTC
    utc = datetime1.astimezone(tz=UTC)
    assert utc.tzinfo != datetime1.tzinfo
    assert str(utc) == "2000-02-28 16:23:45.678901+00:00"

    # convert UTC -> JST
    datetime2 = utc.astimezone(tz=tz_ja)
    assert datetime2.tzinfo != utc.tzinfo
    assert str(datetime2) == "2000-02-29 01:23:45.678901+09:00"
