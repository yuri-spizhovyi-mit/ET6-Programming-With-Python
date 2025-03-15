class Coordinates(object):
    def __init__(
        self,
        x,
        y,
    ):
        self.x = x
        self.y = y


c = Coordinates(3, 4)
origin = Coordinates(0, 0)

print("C instance X: ", c.x)
print("Origin Y: ", origin.y)
