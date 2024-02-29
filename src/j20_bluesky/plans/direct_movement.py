from dodal import Synchrotron
# from here https://github.com/DiamondLightSource/blueapi/pull/377/files


 def touch_synchrotron(sync: Synchrotron = inject("synchrotron")) -> MsgGenerator:
       # There is only one Synchrotron device, so we know which one it will always be.
       # If there is no device named "synchrotron" in the blueapi context, it will except.
       sync.specific_function()
       yield from {}

       

def pass_metadata(x: Movable, metadata: Optional[Mapping[str, Any]] = None) -> MsgGenerator:
    yield from bp.count{[x], md=metadata or {}}