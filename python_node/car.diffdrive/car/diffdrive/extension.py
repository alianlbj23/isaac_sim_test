import omni.ext

from .ogn.OgnDiffDriveToWheelVelocityDatabase import OgnDiffDriveToWheelVelocityDatabase
from .ogn.nodes.OgnDiffDriveToWheelVelocity import OgnDiffDriveToWheelVelocity


class Extension(omni.ext.IExt):
    def on_startup(self, ext_id):
        try:
            OgnDiffDriveToWheelVelocityDatabase.deregister()
        except Exception:
            pass
        OgnDiffDriveToWheelVelocityDatabase.register(OgnDiffDriveToWheelVelocity)

    def on_shutdown(self):
        try:
            OgnDiffDriveToWheelVelocityDatabase.deregister()
        except Exception:
            pass
