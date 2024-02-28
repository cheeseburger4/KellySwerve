from commands2 import Subsystem
import phoenix6

class SwerveModule(Subsystem):
    
    def __init__(self, mod_name, drive_motor_constants, direction_motor_constants, driveID, directionID, coderID):
        self.name = mod_name
        self.drive_const = drive_motor_constants
        self.direction_const = direction_motor_constants

        self.drive_motor = phoenix6.hardware.TalonFX(driveID, "rio")
        self.direction_motor = phoenix6.hardware.TalonFX(directionID, "rio")

    def setDirectionAngle():
        pass
        
