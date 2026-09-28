import numpy as np

class BicycleModel:

    def corner_speed(
        self,
        radius,
        mass,
        grip
    ):

        return np.sqrt(
            grip*radius/mass
        )