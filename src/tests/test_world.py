import unittest

from src.ecosim.config import STARTING_FOOD, WORLD_WIDTH, WORLD_HEIGHT
from src.ecosim.simulation.food import Food
from src.ecosim.simulation.genome import Genome
from src.ecosim.simulation.organism import Organism
from src.ecosim.simulation.world import World


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.world = World()

        self.genome = Genome(
            size=1,
            speed=1,
            vision=100,
            metabolism=1,
        )

    def test_update_advances_time(self):
        self.world.update(1)
        self.assertEqual(self.world.time, 1)

    def test_update_removes_organism_when_energy_reaches_zero(self):
        organism = Organism(
            x=100,
            y=100,
            genome=self.genome,
            alive=True,
            energy=1
        )

        self.world.organisms = [organism]
        self.world.update(dt=1)
        self.assertEqual(len(self.world.organisms), 0)

    def test_remove_dead(self):
        alive_organism = Organism(
            x=100,
            y=100,
            genome=self.genome,
            alive=True,
        )
        dead_organism = Organism(
            x=200,
            y=200,
            genome=self.genome,
            alive=False,
        )

        self.world.organisms = [alive_organism, dead_organism]
        self.world.remove_dead()

        self.assertEqual(len(self.world.organisms), 1)
        self.assertIs(self.world.organisms[0], alive_organism)

    def test_world_starts_with_config_food_amount(self):
        self.assertEqual(len(self.world.food), STARTING_FOOD)

    def test_world_food_items(self):
        for food_item in self.world.food:
            self.assertIsInstance(food_item, Food, "Is food")
            self.assertLessEqual(food_item.x, WORLD_WIDTH, "In x upper bound")
            self.assertGreaterEqual(food_item.x, 0, "In x lower bound")
            self.assertLessEqual(food_item.y, WORLD_HEIGHT, "In y upper bound")
            self.assertGreaterEqual(food_item.y, 0, "In y lower bound")


if __name__ == "__main__":
    unittest.main()
