from commands2 import Subsystem
from phoenix6.hardware import TalonFX
from wpimath.kinematics import ChassisSpeeds, SwerveDrive4Kinematics, SwerveModulePosition, SwerveModuleState
import phoenix6

class SwerveModule(Subsystem):
    
    def __init__(self, mod_name, drive_motor_constants, direction_motor_constants):
        self.name = mod_name
        self.drive_const = drive_motor_constants
        self.direction_const = direction_motor_constants

        self.drive_motor = TalonFX(drive_motor_constants.motor_id, "rio")
        drive_motor_constants.apply_configuration(self.drive_motor)

        self.direction_motor = TalonFX(direction_motor_constants.motor_id, "rio")
        direction_motor_constants.apply_configuration(self.direction_motor)

    def setDirectionAngle():
        pass
        
