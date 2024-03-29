from typing import Any, Mapping, Optional

import bluesky.preprocessors as bpp
from bluesky.plans import count
from dls_bluesky_core.core import MsgGenerator, inject
from dodal.devices.synchrotron import Synchrotron
from ophyd import Movable
from ophyd.sim import det1, motor  # simulated detector, motor

# from here https://github.com/DiamondLightSource/blueapi/pull/377/files


def direct_movement(
    motor: any,
    metadata: Optional[Mapping[str, Any]] = None,
) -> MsgGenerator:
    dets = [det1]
    yield count(dets, num=1, delay=0.5, per_shot=None, md=None)
