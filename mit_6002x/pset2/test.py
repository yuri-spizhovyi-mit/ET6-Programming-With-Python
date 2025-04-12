from ps2 import Position, RectangularRoom
import random

pos0 = Position(0, 0)
pos1 = pos0.getNewPosition(45, 1)
pos2 = pos1.getNewPosition(45, 1)


print(pos1, pos2)
positions = []
pos_1 = (1, 3)
pos_2 = (2, 2)
pos_3 = (1, 5)
pos_4 = (1, 3)
pos_5 = (3, 3)
if pos_1 == pos_3:
    print("Equal")
positions.append(pos_1)
positions.append(pos_2)
positions.append(pos_3)
print(positions)
if pos_4 not in positions:
    positions.append(pos_4)
if pos_5 not in positions:
    positions.append(pos_5)
print(positions)

room = RectangularRoom(5, 5)
room.cleanTileAtPosition(Position(0.7, 0.7))
print(room.isTileCleaned(0.7, 0.7))
print(len(positions))
print(room.getRandomPosition())
print(random.choice(range(1, 6)))
x, y = pos_2
print(x)
print(y)
print(room.isPositionInRoom(Position(0.7, 0.7)))
