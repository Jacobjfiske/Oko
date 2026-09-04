from dataclasses import dataclass
from src.ecosim.simulation.genome import Genome


@dataclass
class Corpse:
    x: float
    y: float
    genome: Genome
