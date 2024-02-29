from typing import Any, Mapping, Optional

import bluesky.preprocessors as bpp
from dls_bluesky_core.core import MsgGenerator, inject
from dodal.devices.synchrotron import Synchrotron
from ophyd import Movable


def trajectory_scan(
    start: float,
    stop: float,
    motor: any,
    detector: any,
    metadata: Optional[Mapping[str, Any]] = None,
) -> MsgGenerator:
    """based on a TTL signal from a Zebra box"""
    yield {}
