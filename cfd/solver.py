import numpy as np

class CFDSolver:

    def __init__(self,nx=100,ny=100):

        self.nx = nx
        self.ny = ny

    def solve(self):

        u = np.ones((self.nx,self.ny))

        v = np.zeros((self.nx,self.ny))

        p = np.zeros((self.nx,self.ny))

        return u,v,p