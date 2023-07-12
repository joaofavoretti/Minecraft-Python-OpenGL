import numpy as np
from object import Object, vertex_data_dtype
from OpenGL.GL import *
from PIL import Image
from chunkk import Chunk

TEXTURE_ATLAS_PATH = 'assets/texture_atlas.png'

CHUNK_NUMBER = 1

class World(Object):

    def __init__(self):
        super().__init__()

        self.chunks = {}

        self.__add_chunks__(CHUNK_NUMBER)

    def __load_texture_file__(self, texture_file):
        self.texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        image = Image.open(texture_file)
        image_width = image.size[0]
        image_height = image.size[1]
        image_data = image.tobytes("raw", "RGBA", 0, -1)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    def __add_chunks__(self, chunk_number):
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