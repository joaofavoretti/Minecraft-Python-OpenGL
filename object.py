import numpy as np

vertex_data_dtype = np.dtype([
    ("position", np.float32, 3),
    ("texture", np.float32, 2)
])

class Object:
    def __init__(self):
        pass

    def load(self):
        raise NotImplementedError("load() not implemented")

    def draw(self, camera):
        raise NotImplementedError("draw() not implemented")
