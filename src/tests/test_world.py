import unittest

from src.ecosim.config import STARTING_FOOD, WORLD_WIDTH, WORLD_HEIGHT, CORPSE_REMOVAL_DT
from src.ecosim.simulation.corpse import Corpse
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
        self.assertEqual(
            1,
            self.world.time,
            msg=f"World time after a 1-second update: expected 1, got {self.world.time}",
        )

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
        self.assertEqual(
            0,
            len(self.world.organisms),
            msg=(
                "Organism reaching zero energy should be removed: "
                f"expected 0 organisms, got {len(self.world.organisms)}"
            ),
        )

    def test_remove_dead_organisms(self):
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
        self.world.remove_dead_organisms()

        self.assertEqual(
            1,
            len(self.world.organisms),
            msg=(
                "Removing dead organisms should leave one survivor: "
                f"expected 1 organism, got {len(self.world.organisms)}"
            ),
        )
        self.assertIs(
            alive_organism,
            self.world.organisms[0],
            msg="The remaining organism should be the original living organism",
        )

    def test_world_starts_with_config_food_amount(self):
        self.assertEqual(
            STARTING_FOOD,
            len(self.world.food),
            msg=(
                f"Starting food count: expected {STARTING_FOOD}, "
                f"got {len(self.world.food)}"
            ),
        )

    def test_world_food_items(self):
        for food_item in self.world.food:
            self.assertIsInstance(
                food_item,
                Food,
                msg=f"World food item should be Food, got {type(food_item).__name__}",
            )
            self.assertLessEqual(
                food_item.x,
                WORLD_WIDTH,
                msg=f"Food x={food_item.x} exceeds world width {WORLD_WIDTH}",
            )
            self.assertGreaterEqual(
                food_item.x,
                0,
                msg=f"Food x={food_item.x} is below the lower bound 0",
            )
            self.assertLessEqual(
                food_item.y,
                WORLD_HEIGHT,
                msg=f"Food y={food_item.y} exceeds world height {WORLD_HEIGHT}",
            )
            self.assertGreaterEqual(
                food_item.y,
                0,
                msg=f"Food y={food_item.y} is below the lower bound 0",
            )

    def test_overlapping_food_increases_energy_and_is_removed(self):
        organism = Organism(
            x=100,
            y=100,
            genome=self.genome,
            alive=True,
        )
        food_item = Food(
            x=100,
            y=100,
        )
        energy_after_consume = organism.energy + food_item.energy

        self.world.organisms = [organism]
        self.world.food = [food_item]

        self.world.handle_food()

        self.assertEqual(
            energy_after_consume,
            organism.energy,
            msg=(
                f"Overlapping food should increase organism energy: "
                f"expected {energy_after_consume}, got {organism.energy}"
            ),
        )
        self.assertEqual(
            [],
            self.world.food,
            msg=f"Consumed food should be removed, got {self.world.food}",
        )

    def test_food_remains_no_energy_consumed(self):
        organism = Organism(
            x=200,
            y=200,
            genome=self.genome,
            alive=True,
        )
        food_item = Food(
            x=100,
            y=100,
        )

        energy_after_consume = organism.energy + food_item.energy

        self.world.organisms = [organism]
        self.world.food = [food_item]

        self.world.handle_food()

        self.assertNotEqual(
            energy_after_consume,
            organism.energy,
            msg="Distant food should not increase organism energy",
        )
        self.assertNotEqual(
            [],
            self.world.food,
            msg="Distant food should remain in the world",
        )

    def test_food_remains_with_no_organisms(self):
        self.world.organisms = []
        self.world.handle_food()
        self.assertNotEqual(
            [],
            self.world.food,
            msg="Food should remain when the world has no organisms",
        )

    def test_uneaten_food_is_not_duplicated(self):
        organism1 = Organism(
            x=200,
            y=200,
            genome=self.genome,
            alive=True,
        )
        organism2 = Organism(
            x=300,
            y=300,
            genome=self.genome,
            alive=True,
        )
        food_item = Food(
            x=100,
            y=100,
        )

        self.world.organisms = [organism1, organism2]
        self.world.food = [food_item]

        self.world.handle_food()

        self.assertEqual(
            [food_item],
            self.world.food,
            msg=(
                "Uneaten food should remain exactly once: "
                f"expected {[food_item]}, got {self.world.food}"
            ),
        )

    def test_closest_organism_consumes_food(self):
        energy_after_consume = 120

        zero_index_organism = Organism(
            x=105,
            y=100,
            genome=self.genome,
            alive=True,
        )
        closest_organism = Organism(
            x=100,
            y=100,
            genome=self.genome,
            alive=True,
        )
        food_item = Food(
            x=100,
            y=100,
        )

        self.world.organisms = [zero_index_organism, closest_organism]
        self.world.food = [food_item]

        self.world.handle_food()

        self.assertEqual(energy_after_consume, closest_organism.energy, "closest organism should consume food")

    def test_remove_dead_creates_corpse_at_organism_position(self):
        dead_organism = Organism(
            x=30,
            y=50,
            genome=self.genome,
            alive=False,
        )
        self.world.organisms = [dead_organism]
        self.world.food = []

        self.world.remove_dead_organisms()

        self.assertEqual([], self.world.organisms, "Organism should be removed")
        self.assertEqual(dead_organism.x, self.world.corpses[0].x,
                         "Corpse should be at the same coordinate position of the removed dead organism")
        self.assertEqual(dead_organism.y, self.world.corpses[0].y,
                         "Corpse should be at the same coordinate position of the removed dead organism")
        self.assertEqual(dead_organism.genome.size, self.world.corpses[0].genome.size,
                         "Corpse should be the same size as the organism")

    def test_corpse_age_progresses_and_removes_with_time(self):
        dt = 15

        self.world.corpses = [Corpse(100, 100, self.genome)]

        self.world.update(dt)
        self.assertEqual(dt, self.world.corpses[0].age, "Age should progress on update")
        self.world.update(CORPSE_REMOVAL_DT)
        self.assertEqual([], self.world.corpses, "Corpses should be removed")


if __name__ == "__main__":
    unittest.main()
