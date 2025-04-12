import random

from mit_6002x.pset2.ps2 import Position, RectangularRoom
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestIsPositionInRoom(unittest.TestCase):
    def setUp(self):
        self.room = RectangularRoom(5, 5)

    def test_positive(self):
        self.assertTrue(self.room.isPositionInRoom(Position(3, 3)))

    def test_negative(self):
        self.assertFalse(self.room.isPositionInRoom(Position(6, 3)))

    def test_low_boundary(self):
        self.assertTrue(self.room.isPositionInRoom(Position(0, 0)))

    def test_top_boundary(self):
        self.assertTrue(self.room.isPositionInRoom(Position(4.9, 4.9)))

    def test_top_boundary_negative(self):
        self.assertFalse(self.room.isPositionInRoom(Position(5, 5)))

    def test_negative_coordinates(self):
        self.assertFalse(self.room.isPositionInRoom(Position(-0.1, 2)))


class TestCleanTileAtPosition(unittest.TestCase):
    def setUp(self):
        self.room = RectangularRoom(5, 5)

    def test_clean_once(self):
        self.room.cleanTileAtPosition(Position(1.2, 3.4))
        self.assertTrue(self.room.isTileCleaned(1, 3))

    def test_clean_twice_same_tile(self):
        self.room.cleanTileAtPosition(Position(1.2, 3.4))
        self.room.cleanTileAtPosition(Position(1.6, 3.9))
        self.assertEqual(self.room.getNumCleanedTiles(), 1)


class TestGetNumTiles(unittest.TestCase):
    def test_5x5_room(self):
        room = RectangularRoom(5, 5)
        self.assertEqual(room.getNumTiles(), 25)

    def test_3x4_room(self):
        room = RectangularRoom(3, 4)
        self.assertEqual(room.getNumTiles(), 12)


class TestGetNumCleanedTiles(unittest.TestCase):
    def setUp(self):
        self.room = RectangularRoom(5, 5)

    def test_get_nums(self):
        self.assertEqual(self.room.getNumCleanedTiles(), 0)


class TestGetRandomPosition(unittest.TestCase):
    """Tests for the getRandomPosition method of RectangularRoom"""

    def setUp(self):
        self.room = RectangularRoom(5, 5)

    def test_random_position_is_in_room(self):
        # Run 100 samples and make sure they are all valid positions
        for _ in range(100):
            pos = self.room.getRandomPosition()
            self.assertIsInstance(
                pos, Position, "Returned value is not a Position instance"
            )
            self.assertTrue(
                self.room.isPositionInRoom(pos), f"Position {pos} is out of room bounds"
            )

    def test_random_positions_are_varied(self):
        # Optional: check that we get more than 1 unique result (not required, but interesting)
        positions = {
            (round(p.getX(), 1), round(p.getY(), 1))
            for p in [self.room.getRandomPosition() for _ in range(100)]
        }
        self.assertGreater(
            len(positions), 1, "Random positions do not vary — check RNG"
        )


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
