from scipy.optimize import differential_evolution

class SetupOptimizer:

    def optimize(
        self,
        objective
    ):

        bounds = [

            (5,20),

            (10,30),

            (20,50)
        ]

        return differential_evolution(
            objective,
            bounds
        )