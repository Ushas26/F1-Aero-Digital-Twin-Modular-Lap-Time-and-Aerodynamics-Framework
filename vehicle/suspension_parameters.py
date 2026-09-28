from dataclasses import dataclass

@dataclass
class Suspension:

    front_spring_rate: float = 200000

    rear_spring_rate: float = 180000

    front_ride_height: float = 25

    rear_ride_height: float = 40