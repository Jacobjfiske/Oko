import unittest

from src.ecosim.simulation.genome import Genome
from src.ecosim.simulation.organism import Organism


class TestOrganism(unittest.TestCase):

    def test_organism_dies_when_energy_reaches_zero(self):
        genome = Genome(
            size=1,
            speed=1,
            vision=100,
            metabolism=1,
        )
        organism = Organism(
            x=100,
            y=100,
            genome=genome,
            energy=1,
        )

        organism.update(dt=1)

        self.assertTrue(organism.alive)


if __name__ == "__main__":
    unittest.main()
