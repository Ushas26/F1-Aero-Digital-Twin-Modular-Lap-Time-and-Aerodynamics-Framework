from dataclasses import dataclass

@dataclass
class Vehicle:

    mass: float = 798

    wheelbase: float = 3.6

    track_width: float = 2.0

    cg_height: float = 0.30