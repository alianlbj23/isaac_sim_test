import math


class OgnDiffDriveToWheelVelocity:

    @staticmethod
    def compute(db):

        vx = db.inputs.linearX
        omega = db.inputs.angularZ

        radius = db.inputs.wheelRadius
        separation = db.inputs.wheelSeparation

        if radius == 0:
            db.log_error("wheelRadius must not be zero")
            return False

        left_rad = vx / radius - (separation * omega) / (2.0 * radius)
        right_rad = vx / radius + (separation * omega) / (2.0 * radius)

        db.outputs.leftDegPerSec = left_rad * 180.0 / math.pi
        db.outputs.rightDegPerSec = right_rad * 180.0 / math.pi

        return True
