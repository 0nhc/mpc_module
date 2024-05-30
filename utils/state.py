class State:
    """
    vehicle state class
    """
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x # x position [m]
        self.y = y # y position [m]
        self.yaw = yaw # yaw angle [rad]
        self.v = v # velocity [m/s]