import numpy as np
from object import Object, vertex_data_dtype
from OpenGL.GL import *
from PIL import Image
from chunkk import Chunk

TEXTURE_ATLAS_PATH = 'assets/texture_atlas.png'

CHUNK_NUMBER = 5

class World(Object):

    def __init__(self):
        super().__init__()

        self.chunks = {}

        self.__create_chunks__(CHUNK_NUMBER)

    def __create_chunks__(self, chunk_number):
        for x in range(-chunk_number, chunk_number):
            for z in range(-chunk_number, chunk_number):
                self.chunks[(x, z)] = Chunk((x, z))

    def load(self, program):
        self.__load_texture_file__(TEXTURE_ATLAS_PATH)

        for chunk in self.chunks.values():
            chunk.load(program)

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        for chunk in self.chunks.values():
            chunk.draw()

        glBindTexture(GL_TEXTURE_2D, 0)