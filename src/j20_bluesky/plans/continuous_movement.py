from typing import Any, Mapping, Optional

from dls_bluesky_core.core import MsgGenerator, inject


def continuous_movement(metadata: Optional[Mapping[str, Any]] = None) -> MsgGenerator:
    yield {}
