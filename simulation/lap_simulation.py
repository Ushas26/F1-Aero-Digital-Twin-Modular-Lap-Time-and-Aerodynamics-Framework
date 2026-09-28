import numpy as np

class LapSimulator:

    def run(
        self,
        track,
        drag,
        downforce
    ):

        lap_time = 0

        for seg in track:

            if seg[0] == "straight":

                lap_time += seg[1]/80

            else:

                radius = seg[2]

                speed = np.sqrt(
                    (
                    downforce+8000
                    )
                    *radius
                    /798
                )

                lap_time += seg[1]/speed

        return lap_time