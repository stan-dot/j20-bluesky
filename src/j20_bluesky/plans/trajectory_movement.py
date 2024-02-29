# from ophyd_async import Movable
import bluesky.preprocessors as bpp
from dls_bluesky_core.core import MsgGenerator, inject
from dodal.devices.synchrotron import Synchrotron
from ophyd import Movable


def trajectory_movement(
    start: float, motor: any, metadata: Optional[Mapping[str, Any]] = None
) -> MsgGenerator:
    yield {}
