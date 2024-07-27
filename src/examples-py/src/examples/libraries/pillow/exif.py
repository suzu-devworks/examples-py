import sys
from argparse import ArgumentParser, FileType, Namespace
from fractions import Fraction
from logging import getLogger
from pathlib import Path
from typing import Any, Tuple

from PIL import Image
from PIL.ExifTags import GPS, GPSTAGS, IFD, TAGS
from PIL.ExifTags import Base as EXIFTAGS

logger = getLogger(__name__)


def _do_example(args: Namespace) -> None:
    """do sample.

    References:
    - https://www.cipa.jp/std/documents/j/DC-008-2012_J.pdf
    - https://support.google.com/maps/answer/18539
    """

    infile = args.infile

    path = Path(infile)
    logger.info(f'in = "{path}"')

    def to_fraction(value: float) -> str:
        if value < 0.3:
            return str(Fraction(value))

        return str(value)

    def to_coordinate(ref: Any, value: Any) -> str:
        degree = int(value[0])
        minute = int(value[1])
        second = value[2]
        return f"{degree}°{minute}'{second}\"{ref}"

    def loginfo_all(list: list[Tuple[Any, Any, Any]]) -> None:
        for key, name, value in list:
            logger.info(f"{key:5d} {name:20s} : {str(value)}")

        logger.info("\n")

    with Image.open(path) as image:
        # gets EXIF tag.
        exif = image.getexif()
        exif_info = [(k, TAGS.get(k, k), v) for k, v in exif.items()]
        loginfo_all(sorted(exif_info))

        # gets EXIF private tag.
        exif_private = exif.get_ifd(IFD.Exif)
        exif_private_info = [(k, TAGS.get(k, k), v) for k, v in exif_private.items() if k != EXIFTAGS.MakerNote]
        loginfo_all(sorted(exif_private_info))

        shutter = to_fraction(exif_private[EXIFTAGS.ShutterSpeedValue])
        expose = to_fraction(exif_private[EXIFTAGS.ExposureTime])
        logger.info(f"----- ShutterSpeedValue    : {shutter}")
        logger.info(f"----- ExposureTime         : {expose}")
        logger.info("\n")

        # gets GPS tag.
        gps = exif.get_ifd(IFD.GPSInfo)
        gps_info = [(k, GPSTAGS.get(k, k), v) for k, v in gps.items()]
        loginfo_all(sorted(gps_info))

        lat = to_coordinate(gps[GPS.GPSLatitudeRef], gps[GPS.GPSLatitude])
        long = to_coordinate(gps[GPS.GPSLongitudeRef], gps[GPS.GPSLongitude])
        logger.info(f"----- GPSLatitude[DMS]    : {lat}")
        logger.info(f"----- GPSLongitude[DMS]   : {long}")
        logger.info("\n")

    return


# spell-checker:words getexif
# spell-checker:words infile
# spell-checker:words loginfo
# spell-checker:words EXIFTAGS
# spell-checker:words GPSTAGS


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "infile",
        help="input file",
    )
    parser.add_argument(
        "-o",
        "--out",
        dest="out",
        help="output stream",
        nargs="?",
        type=FileType("w"),
        default=sys.stdout,
    )
    parser.set_defaults(exec=lambda args: _do_example(args))
