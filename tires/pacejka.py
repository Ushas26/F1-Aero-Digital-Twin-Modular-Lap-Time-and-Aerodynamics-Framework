import numpy as np

class Pacejka:

    def __init__(self,B,C,D):

        self.B = B

        self.C = C

        self.D = D

    def lateral_force(self,slip):

        return (
            self.D
            *np.sin(
                self.C
                *np.arctan(
                    self.B*slip
                )
            )
        )