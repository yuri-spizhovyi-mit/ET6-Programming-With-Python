from mit_6002x.pset2.ps2 import Position, RectangularRoom
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestIsPositionInRoom(unittest.TestCase):
    """Unit tests for the isPositionInRoom method of RectangularRoom."""

    def test_positive(self):
        room = RectangularRoom(5, 5)
        self.assertTrue(room.isPositionInRoom(Position(3, 3)))

    def test_negative(self):
        room = RectangularRoom(5, 5)
        self.assertFalse(room.isPositionInRoom(Position(6, 3)))

    def test_low_boundary(self):
        room = RectangularRoom(5, 5)
        self.assertTrue(room.isPositionInRoom(Position(0, 0)))

    def test_top_boundary(self):
        room = RectangularRoom(5, 5)
        self.assertTrue(room.isPositionInRoom(Position(4.9, 4.9)))

    def test_top_boundary_negative(self):
        room = RectangularRoom(5, 5)
        self.assertFalse(room.isPositionInRoom(Position(5, 5)))

    def test_negative_coordinates(self):
        room = RectangularRoom(5, 5)
        self.assertFalse(room.isPositionInRoom(Position(-0.1, 2)))


if __name__ == "__main__":
    unittest.main()
