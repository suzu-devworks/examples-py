"""This test is for learning "aware" datetime manipulation.

An aware objects have an optional time zone information attribute tzinfo
that can be set to an instance of a subclass of the abstract tzinfo class.

References:
    - https://pythonhosted.org/pytz/
"""

from datetime import datetime, time, timedelta
from time import time as c_style_time

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
def test_pytz_timezones(zone: str, date: datetime, tzname: str, offset: timedelta, dst: timedelta) -> None:
    tz = pytz.timezone(zone)
    assert tz.zone == zone
    assert tz.tzname(date) == tzname
    assert tz.utcoffset(date) == offset
    assert tz.dst(date) == dst


def test_aware_datetime_generators() -> None:
    tz_ja = pytz.timezone("Asia/Tokyo")
    native_date = datetime(2000, 2, 29)

    # datetime (aware)
    now = datetime.now(tz=tz_ja)
    assert isinstance(now, datetime)
    assert now.tzinfo is not None
    assert now.tzinfo.tzname(native_date) == tz_ja.tzname(native_date)

    utc = datetime.now(tz=pytz.UTC)
    assert isinstance(utc, datetime)
    assert utc.tzinfo is not None
    assert utc.tzinfo.tzname(native_date) == pytz.UTC.tzname(native_date)

    today = datetime.today().astimezone(tz_ja)
    assert isinstance(today, datetime)
    assert today.tzinfo is not None
    assert today.tzinfo.tzname(native_date) == tz_ja.tzname(native_date)

    fromtimestamp = datetime.fromtimestamp(c_style_time(), tz=tz_ja)
    assert isinstance(fromtimestamp, datetime)
    assert fromtimestamp.tzinfo is not None
    assert fromtimestamp.tzinfo.tzname(native_date) == tz_ja.tzname(native_date)

    local = tz_ja.localize(datetime.now())
    assert isinstance(local, datetime)
    assert local.tzinfo is not None
    assert local.tzinfo.tzname(native_date) == tz_ja.tzname(native_date)

    # date

    # datetime.time (aware)
    now_tz_time = datetime.now(tz=tz_ja).time()
    assert isinstance(now_tz_time, time)
    assert now_tz_time.tzinfo is None

    now_tz_timetz = datetime.now(tz=tz_ja).timetz()
    assert isinstance(now_tz_timetz, time)
    assert now_tz_timetz.tzinfo is not None
    assert now_tz_timetz.tzinfo.tzname(native_date) == tz_ja.tzname(native_date)


def test_aware_datetime_calculation() -> None:
    tz_ja = pytz.timezone("Asia/Tokyo")
    datetime1 = tz_ja.localize(datetime(2000, 2, 29, 12, 34, 56, 789012))

    # datetime2(aware) = datetime1(aware) + timedelta
    datetime2 = datetime1 + timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == tz_ja.localize(datetime(2000, 3, 1, 14, 35, 26, 789012))

    # datetime2(aware) = datetime1(aware) - timedelta
    datetime2 = datetime1 - timedelta(days=1, hours=2, seconds=30)
    assert datetime2 == tz_ja.localize(datetime(2000, 2, 28, 10, 34, 26, 789012))

    # timedelta = datetime1(aware) - datetime2(aware)
    timedelta1 = datetime1 - tz_ja.localize(datetime(2000, 4, 2, 12, 34, 56, 789012))
    assert timedelta1 == timedelta(days=-33)

    # timedelta = datetime1(aware) - datetime2(native)
    with pytest.raises(TypeError) as ex:
        datetime1 - datetime(2000, 4, 2, 12, 34, 56, 789012)
    assert str(ex.value) == "can't subtract offset-naive and offset-aware datetimes"

    # datetime1(aware) < datetime2(aware)
    actual = datetime1 < tz_ja.localize(datetime(2000, 4, 2, 12, 34, 56, 789012))
    assert actual is True


def test_aware_datetime_conversion_with_string() -> None:
    tz_ja = pytz.timezone("Asia/Tokyo")
    datetime1 = tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 678901))

    # convert datetime to string(ISO8601)
    iso8601 = datetime1.isoformat()
    assert iso8601 == "2000-02-29T01:23:45.678901+09:00"

    iso8601utc = datetime1.astimezone(pytz.UTC).isoformat().replace("+00:00", "Z")
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


def test_aware_datetime_conversion_between_utc_and_jst() -> None:
    tz_ja = pytz.timezone("Asia/Tokyo")
    datetime1 = tz_ja.localize(datetime(2000, 2, 29, 1, 23, 45, 678901))

    # convert JST -> UTC
    utc = datetime1.astimezone(tz=pytz.UTC)
    assert utc.tzinfo != datetime1.tzinfo
    assert str(utc) == "2000-02-28 16:23:45.678901+00:00"

    # convert UTC -> JST
    datetime2 = utc.astimezone(tz=tz_ja)
    assert datetime2.tzinfo != utc.tzinfo
    assert str(datetime2) == "2000-02-29 01:23:45.678901+09:00"


def test_aware_datetime_conversion_according_to_dst() -> None:
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


def test_aware_datetime_conversion_with_native() -> None:
    tz_ja = pytz.timezone("Asia/Tokyo")
    datetime1 = datetime(2000, 2, 29, 1, 23, 45, 678901)

    # This is because before 1888, the time was +09:19 away from UTC.
    assert repr(tz_ja) == "<DstTzInfo 'Asia/Tokyo' LMT+9:19:00 STD>"

    # convert native -> aware(localize)
    aware = tz_ja.localize(datetime1)
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
