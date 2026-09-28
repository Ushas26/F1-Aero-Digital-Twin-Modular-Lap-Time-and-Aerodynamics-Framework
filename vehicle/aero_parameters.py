from dataclasses import dataclass

@dataclass
class AeroParameters:

    frontal_area: float = 1.5

    cd: float = 0.90

    cl: float = -3.5