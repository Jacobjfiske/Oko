import unittest

from src.ecosim.config import FOOD_ENERGY
from src.ecosim.simulation.food import Food


class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food(x=100, y=200)

    def test_food_initialization(self):
        self.assertEqual(
            100,
            self.food.x,
            msg=f"Food x coordinate: expected 100, got {self.food.x}",
        )
        self.assertEqual(
            200,
            self.food.y,
            msg=f"Food y coordinate: expected 200, got {self.food.y}",
        )

        self.assertEqual(
            FOOD_ENERGY,
            self.food.energy,
            msg=(
                f"Food default energy: expected {FOOD_ENERGY}, "
                f"got {self.food.energy}"
            ),
        )


if __name__ == "__main__":
    unittest.main()
