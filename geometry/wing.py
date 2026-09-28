import numpy as np

class Wing:

    def __init__(self,chord=1.0):

        self.chord = chord

    def generate(self):

        x = np.linspace(0,1,100)

        thickness = (
            0.12/0.2
            *(
            0.2969*np.sqrt(x)
            -0.126*x
            -0.3516*x**2
            +0.2843*x**3
            -0.1015*x**4
            )
        )

        upper = thickness
        lower = -thickness

        return x,upper,lower