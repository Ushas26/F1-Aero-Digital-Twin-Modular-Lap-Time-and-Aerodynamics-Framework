from dataclasses import dataclass

@dataclass
class TireParameters:

    mu: float = 1.8

    pacejka_B: float = 10

    pacejka_C: float = 1.9

    pacejka_D: float = 1.0