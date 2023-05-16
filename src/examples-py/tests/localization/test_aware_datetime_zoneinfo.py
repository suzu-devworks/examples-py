"""
This test to learn "aware" datetime manipulation.

An aware objects have an optional time zone information attribute tzinfo
that can be set to an instance of a subclass of the abstract tzinfo class.
"""

from datetime import datetime, time, timedelta, timezone
from time import time as cstyle_time
from zoneinfo import ZoneInfo

import pytest

timezonedata = [
    ("Asia/Tokyo", datetime(2000, 2, 29), "JST", timedelta(hours=9), timedelta(0)),
    ("UTC", datetime(2000, 2, 29), "UTC", timedelta(hours=0), timedelta(0)),
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


@pytest.mark.parametrize("zone,basedate,tzname,offset,dst", timezonedata)
def test_timezone(
    zone: str, basedate: datetime, tzname: str, offset: timedelta, dst: timedelta
):
    tz = ZoneInfo(zone)
    assert tz.key == zone
    assert tz.tzname(basedate) == tzname
    assert tz.utcoffset(basedate) == offset
    assert tz.dst(basedate) == dst


def test_timezone_utc():
    basedate = datetime(2000, 2, 29)

    tz = timezone.utc
    # assert tz.key == "UTC"
    assert tz.tzname(basedate) == "UTC"
    assert tz.utcoffset(basedate) == timedelta(0)
    assert tz.dst(basedate) is None


def test_datetime_generators():
    tz_ja = ZoneInfo("Asia/Tokyo")
    nativedate = datetime(2000, 2, 29)

    # datetime (aware)
    now = datetime.now(tz=tz_ja)
    assert isinstance(now, datetime)
    assert now.tzinfo is not None
    assert now.tzinfo.tzname(nativedate) == tz_ja.tzname(nativedate)

    utc = datetime.now(tz=timezone.utc)
    assert isinstance(utc, datetime)
    assert utc.tzinfo is not None
    assert utc.tzinfo.tzname(nativedate) == timezone.utc.tzname(nativedate)

    today = datetime.today().astimezone(tz_ja)
    assert isinstance(today, datetime)
    assert today.tzinfo is not None
    assert today.tzinfo.tzname(nativedate) == tz_ja.tzname(nativedate)

    fromtimestamp = datetime.fromtimestamp(cstyle_time(), tz=tz_ja)
    assert isinstance(fromtimestamp, datetime)
    assert fromtimestamp.tzinfo is not None
    assert fromtimestamp.tzinfo.tzname(nativedate) == tz_ja.tzname(nativedate)

    # date

    # datetime.time (aware)
    now_tz_time = datetime.now(tz=tz_ja).time()
    assert isinstance(now_tz_time, time)
    assert now_tz_time.tzinfo is None

    now_tz_timetz = datetime.now(tz=tz_ja).timetz()
    assert isinstance(now_tz_timetz, time)
    assert now_tz_timetz.tzinfo is not None
    assert now_tz_timetz.tzinfo.tzname(nativedate) == tz_ja.tzname(nativedate)


def test_datetime_calculation():
    tz_ja = ZoneInfo("Asia/Tokyo")
    datetime1 = datetime(2000, 2, 29, 12, 34, 56, 789012, tzinfo=tz_ja)

    # datetime2(aware) = datetime1(aware) + timedelta
    datetime2 = datetime1 + timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == datetime(2000, 3, 1, 14, 35, 26, 789012, tzinfo=tz_ja)

    # datetime2(aware) = datetime1(aware) - timedelta
    datetime2 = datetime1 - timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == datetime(2000, 2, 28, 10, 34, 26, 789012, tzinfo=tz_ja)

    # timedelta = datetime1(aware) - datetime2(aware)
    timedelta1 = datetime1 - datetime(2000, 4, 2, 12, 34, 56, 789012, tzinfo=tz_ja)
    assert timedelta1 == timedelta(days=-33)

    # timedelta = datetime1(aware) - datetime2(utc)
    timedelta1 = datetime1 - datetime(
        2000, 4, 2, 12, 34, 56, 789012, tzinfo=timezone.utc
    )
    assert timedelta1 == timedelta(days=-34, hours=15)

    # timedelta = datetime1(aware) - datetime2(native)
    with pytest.raises(TypeError) as ex:
        datetime1 - datetime(2000, 4, 2, 12, 34, 56, 789012)
    assert str(ex.value) == "can't subtract offset-naive and offset-aware datetimes"

    # datetime1(aware) < datetime2(aware)
    actual = datetime1 < datetime(2000, 4, 2, 12, 34, 56, 789012, tzinfo=tz_ja)
    assert actual is True


def test_datetime_convert_tostring():
    tz_ja = ZoneInfo("Asia/Tokyo")
    datetime1 = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)

    # convert datetime to string(ISO8601)
    iso8601 = datetime1.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901+09:00"

    iso8601utc = datetime1.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    assert iso8601utc == "2000-02-28T16:23:45.678901Z"

    # convert string(ISO8601) to datetime
    datetime2 = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S.%f%z")
    assert datetime2 == datetime1

    datetime2 = datetime.strptime(iso8601utc, "%Y-%m-%dT%H:%M:%S.%f%z")
    assert datetime2 == datetime1

    # convert datetime to string
    text = datetime1.strftime("%Y/%m/%d %H:%M:%S %z %Z")
    assert text == "2000/02/29 01:23:45 +0900 JST"
    assert text != "2000/02/29 01:23:45 +09:00 JST"


def test_datetime_convert_timezone():
    tz_ja = ZoneInfo("Asia/Tokyo")
    datetime1 = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)

    # convert JST -> UTC
    utc = datetime1.astimezone(tz=timezone.utc)
    assert utc.tzinfo != datetime1.tzinfo
    assert str(utc) == "2000-02-28 16:23:45.678901+00:00"

    # convert UTC -> JST
    datetime2 = utc.astimezone(tz=tz_ja)
    assert datetime2.tzinfo != utc.tzinfo
    assert str(datetime2) == "2000-02-29 01:23:45.678901+09:00"
