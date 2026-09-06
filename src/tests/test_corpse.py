import unittest

from src.ecosim.simulation.corpse import Corpse
from src.ecosim.simulation.genome import Genome


class CorpseTest(unittest.TestCase):

    def setUp(self):
        self.genome = Genome(
            size=1,
            speed=1,
            vision=100,
            metabolism=1,
        )
        self.corpse = Corpse(100, 100, self.genome)

    def test_corpse_age_advances_with_time(self):
        dt = 2
        self.corpse.update(dt)
        self.assertEqual(dt, self.corpse.age, "Corpse age should progress with time")


