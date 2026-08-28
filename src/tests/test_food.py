import unittest

from src.ecosim.config import FOOD_ENERGY
from src.ecosim.simulation.food import Food


class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food(x=100, y=200)

    def test_food_initialization(self):
        self.assertEqual(self.food.x, 100)
        self.assertEqual(self.food.y, 200)

        self.assertEqual(self.food.energy, FOOD_ENERGY)


if __name__ == "__main__":
    unittest.main()
