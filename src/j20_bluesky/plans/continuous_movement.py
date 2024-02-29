from typing import Any, Mapping, Optional

from bluesky import MsgGenerator


def continuous_movement(metadata: Optional[Mapping[str, Any]] = None) -> MsgGenerator:
    yield {}
