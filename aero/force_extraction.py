import numpy as np

def extract_forces(pressure,area):

    drag = np.sum(
        pressure*area*0.1
    )

    downforce = np.sum(
        pressure*area*0.5
    )

    return drag,downforce