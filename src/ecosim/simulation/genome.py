from dataclasses import dataclass
import random


@dataclass
class Genome:
    size: float
    speed: float
    vision: float
    metabolism: float

    @classmethod
    def random(cls):
        return cls(
            size=random.uniform(0.5, 1.5),
            speed=random.uniform(0.5, 1.5),
            vision=random.uniform(50, 150),
            metabolism=random.uniform(0.5, 1.5)
        )

    def mutated_copy(self):
        return Genome(
            size=self._mutate(self.size),
            speed=self._mutate(self.speed),
            vision=self._mutate(self.vision),
            metabolism=self._mutate(self.metabolism),
        )

    @staticmethod
    def _mutate(value):
        return value * random.uniform(0.95, 1.05)
