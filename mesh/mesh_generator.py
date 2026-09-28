import pyvista as pv

class MeshGenerator:

    def generate(self):

        grid = pv.ImageData(
            dimensions=(100,100,50)
        )

        return grid