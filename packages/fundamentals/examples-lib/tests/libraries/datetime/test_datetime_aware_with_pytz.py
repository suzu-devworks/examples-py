"""This test is for learning "aware" datetime manipulation.

An aware objects have an optional time zone information attribute tzinfo
that can be set to an instance of a subclass of the abstract tzinfo class.

References:
    - https://pythonhosted.org/pytz/
"""

from datetime import datetime, time, timedelta
from time import time as c_style_time
from typing import Any

import pytest
import pytz

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

    tz = pytz.timezone(zone)

    assert tz.zone == zone
    assert tz.tzname(date) == tzname
    assert tz.utcoffset(date) == offset
    assert tz.dst(date) == dst


@pytest.fixture
def tz_ja() -> Any:
    return pytz.timezone("Asia/Tokyo")


def test_creation(tz_ja: Any) -> None:
    """Create a aware datetime in several ways."""

    # Given a date, convert LMT+9:19:00 to JST+9:00:00.
    jst = tz_ja.localize(datetime(2000, 2, 29)).tzinfo
    assert jst != tz_ja

    # datetime (aware)

    now = datetime.now(tz=tz_ja)
    assert isinstance(now, datetime)
    assert now.tzinfo == jst

    utc = datetime.now(tz=pytz.UTC)
    assert isinstance(utc, datetime)
    assert utc.tzinfo == pytz.UTC

    today = datetime.today().astimezone(tz_ja)
    assert isinstance(today, datetime)
    assert today.tzinfo == jst

    fromtimestamp = datetime.fromtimestamp(c_style_time(), tz=tz_ja)
    assert isinstance(fromtimestamp, datetime)
    assert fromtimestamp.tzinfo == jst

    local = tz_ja.localize(datetime.now())
    assert isinstance(local, datetime)
    assert local.tzinfo == jst

    # date

    # datetime.time (aware)

    now_tz_time = datetime.now(tz=tz_ja).time()
    assert isinstance(now_tz_time, time)
    assert now_tz_time.tzinfo is None

    now_tz_timetz = datetime.now(tz=tz_ja).timetz()
    assert isinstance(now_tz_timetz, time)
    assert now_tz_timetz.tzinfo == jst


def test_calculation(tz_ja: Any) -> None:
    """Calculate with datetime."""

    base_datetime = tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 678901))

    # datetime(aware) = datetime(aware) + timedelta
    actual = base_datetime + timedelta(days=1, hours=2, seconds=30)
    assert actual == tz_ja.localize(datetime(2000, 3, 1, 3, 24, 15, 678901))

    # datetime(aware) = datetime(aware) - timedelta
    actual = base_datetime - timedelta(days=1, hours=2, seconds=30)
    assert actual == tz_ja.localize(datetime(2000, 2, 27, 23, 23, 15, 678901))

    # timedelta = datetime(aware) - datetime(aware)
    actual = base_datetime - tz_ja.localize(datetime(2000, 4, 2, 1, 23, 45, 678901))
    assert actual == timedelta(days=-33)

    # timedelta = datetime(aware) - datetime(native)
    with pytest.raises(TypeError) as ex:
        base_datetime - datetime(2000, 4, 2, 1, 23, 45, 678901)
    assert str(ex.value) == "can't subtract offset-naive and offset-aware datetimes"

    # datetime (==|<|>) datetime
    assert base_datetime != tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 999999))
    assert base_datetime > tz_ja.localize(datetime(2000, 2, 29, 1, 23, 44, 678901))
    assert base_datetime < tz_ja.localize(datetime(2000, 2, 29, 1, 23, 46, 678901))


def test_conversion_string(tz_ja: Any) -> None:
    """Converts between date and string types."""

    base_datetime = tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 678901))

    # convert datetime to string(ISO8601)
    iso8601 = base_datetime.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901+09:00"

    iso8601utc = base_datetime.astimezone(pytz.UTC).isoformat().replace("+00:00", "Z")
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

    base_datetime = tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 678901))

    # convert JST -> UTC
    utc = base_datetime.astimezone(tz=pytz.UTC)
    assert utc.tzinfo != base_datetime.tzinfo
    assert str(utc) == "2000-02-28 16:23:45.678901+00:00"

    # convert UTC -> JST
    datetime2 = utc.astimezone(tz=tz_ja)
    assert datetime2.tzinfo != utc.tzinfo
    assert str(datetime2) == "2000-02-29 01:23:45.678901+09:00"


def test_conversion_timezone_dst() -> None:
    """Convert to daylight saving time."""

    # DST: Daylight saving time.
    # EST/EDT 2019-03-10T03:00 - 2019-11-03T01:00
    est = pytz.timezone("US/Eastern")
    edt_start = datetime(2019, 3, 10, hour=3 - 1, minute=0, second=0)
    edt_end = datetime(2019, 11, 3, hour=0, minute=59, second=59)

    edt_before = edt_start - timedelta(seconds=1)
    before_localized = est.localize(edt_before)
    before_normalized = est.normalize(est.localize(edt_before))
    assert before_normalized.tzinfo is not None
    assert before_normalized.tzinfo.tzname(before_normalized) == "EST"
    assert before_localized.tzinfo == before_normalized.tzinfo

    start_localized = est.localize(edt_start)
    start_normalized = est.normalize(est.localize(edt_start))
    assert start_localized.tzinfo is not None
    assert start_localized.tzinfo.tzname(start_localized) == "EST"
    assert start_normalized.tzinfo is not None
    assert start_normalized.tzinfo.tzname(start_normalized) == "EDT"
    assert start_normalized.tzinfo != start_localized.tzinfo

    end_localized = est.localize(edt_end)
    end_normalized = est.normalize(est.localize(edt_end))
    assert end_normalized.tzinfo is not None
    assert end_normalized.tzinfo.tzname(end_normalized) == "EDT"
    assert end_normalized.tzinfo == end_localized.tzinfo

    edt_after = edt_end + timedelta(seconds=1)
    after_localized = est.localize(edt_after)
    after_normalized = est.normalize(est.localize(edt_after))
    assert after_normalized.tzinfo is not None
    assert after_normalized.tzinfo.tzname(after_normalized) == "EST"
    assert after_normalized.tzinfo == after_localized.tzinfo


def test_conversion_native(tz_ja: Any) -> None:
    """Converts between native and aware datetime."""

    base_datetime = datetime(2000, 2, 29, 1, 23, 45, 678901)

    # This is because before 1888, the time was +09:19 away from UTC.
    assert repr(tz_ja) == "<DstTzInfo 'Asia/Tokyo' LMT+9:19:00 STD>"

    # convert native -> aware(localize)
    aware = tz_ja.localize(base_datetime)
    assert str(aware) == "2000-02-29 01:23:45.678901+09:00"
    assert aware.tzinfo is not None
    assert aware.tzinfo != tz_ja
    assert repr(aware.tzinfo) == "<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>"

    # convert aware -> native
    native = aware.replace(tzinfo=None)
    assert str(native) == "2000-02-29 01:23:45.678901"
    assert native.tzinfo is None

    # convert native -> aware (astimezone)
    as_zone = native.astimezone(tz=tz_ja)
    assert str(as_zone) == "2000-02-29 10:23:45.678901+09:00"
    assert as_zone.tzinfo is not None
    assert as_zone.tzinfo != tz_ja
    assert repr(as_zone.tzinfo) == "<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>"
    assert as_zone != aware

    aware2 = datetime(2000, 2, 29, 1, 23, 45, 678901, tzinfo=tz_ja)
    assert str(aware2) == "2000-02-29 01:23:45.678901+09:19"
    aware3 = tz_ja.localize(aware2.replace(tzinfo=None))
    assert str(aware3) == "2000-02-29 01:23:45.678901+09:00"
