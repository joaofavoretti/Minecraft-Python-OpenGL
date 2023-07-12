import numpy as np
from object import vertex_data_dtype

TEXTURE_ATLAS_RESOLUTION = 16 / 256

class Block:

    def __init__(self, coord):

        if not isinstance(coord, tuple) or len(coord) != 3:
            raise ValueError("coord must be a tuple with 3 elements")

        self.coord = coord

        if not hasattr(self, 'texture_map'):
            self.texture_map = {
                "top": (1, 0),
                "bottom": (0, 0),
                "front": (2, 0),
                "back": (2, 0),
                "left": (2, 0),
                "right": (2, 0)
            }

        self.__define_vertices__(self.coord, self.texture_map)

    def __define_vertices__(self, coord, texture_map):
        x, y, z = coord

        self.vertices = np.array([
        # Front face
        ((x + 0.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['front'])[0]),
        ((x + 1.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['front'])[1]),
        ((x + 1.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['front'])[2]),
        ((x + 0.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['front'])[3]),

        # Back face
        ((x + 1.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['back'])[1]),
        ((x + 0.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['back'])[0]),
        ((x + 0.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['back'])[3]),
        ((x + 1.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['back'])[2]),

        # Top face
        ((x + 0.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['top'])[0]),
        ((x + 1.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['top'])[1]),
        ((x + 1.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['top'])[2]),
        ((x + 0.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['top'])[3]),

        # Bottom face
        ((x + 0.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['bottom'])[3]),
        ((x + 1.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['bottom'])[2]),
        ((x + 1.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['bottom'])[1]),
        ((x + 0.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['bottom'])[0]),

        # Right face
        ((x + 1.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['right'])[0]),
        ((x + 1.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['right'])[1]),
        ((x + 1.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['right'])[2]),
        ((x + 1.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['right'])[3]),

        # Left face
        ((x + 0.0, y + 0.0, z + 0.0), self.__get_texture_coords__(texture_map['left'])[1]),
        ((x + 0.0, y + 0.0, z + 1.0), self.__get_texture_coords__(texture_map['left'])[0]),
        ((x + 0.0, y + 1.0, z + 1.0), self.__get_texture_coords__(texture_map['left'])[3]),
        ((x + 0.0, y + 1.0, z + 0.0), self.__get_texture_coords__(texture_map['left'])[2]),
    ], dtype=vertex_data_dtype)

    def __get_texture_coords__(self, texture_atlas_coord):
        x, y = texture_atlas_coord
        return np.array([
            (x * TEXTURE_ATLAS_RESOLUTION, y * TEXTURE_ATLAS_RESOLUTION),
            ((x + 1) * TEXTURE_ATLAS_RESOLUTION, y * TEXTURE_ATLAS_RESOLUTION),
            ((x + 1) * TEXTURE_ATLAS_RESOLUTION, (y + 1) * TEXTURE_ATLAS_RESOLUTION),
            (x * TEXTURE_ATLAS_RESOLUTION, (y + 1) * TEXTURE_ATLAS_RESOLUTION)
        ])
    