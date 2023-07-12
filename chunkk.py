from block import Block
from OpenGL.GL import *
import numpy as np
from object import vertex_data_dtype

CHUNK_X_SIZE = 16
CHUNK_Y_SIZE = 1
CHUNK_Z_SIZE = 16

class Chunk:
    def __init__(self, coord):
        self.coord = coord
        
        self.blocks = {}

        self.__add_blocks__()

    def __add_blocks__(self):
        for x in range(CHUNK_X_SIZE):
            for y in range(CHUNK_Y_SIZE):
                for z in range(CHUNK_Z_SIZE):
                    block_x = self.coord[0] * CHUNK_X_SIZE + x
                    block_y = y
                    block_z = self.coord[1] * CHUNK_Z_SIZE + z
                    self.blocks[(block_x, block_y, block_z)] = Block((block_x, block_y, block_z))

    def __stack_blocks_vertices__(self, blocks):
        # Copy the first block vertices
        vertices = None

        for block in blocks.values():
            if vertices is None:
                vertices = block.vertices.copy()
                continue
            
            vertices = np.vstack((vertices, block.vertices))

        return vertices

    def load(self, program):
        self.obj_vao = glGenVertexArrays(1)
        glBindVertexArray(self.obj_vao)

        vertices = self.__stack_blocks_vertices__(self.blocks)

        self.obj_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.obj_vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        
        locationPositionAttrib = glGetAttribLocation(program, "aPosition")
        glVertexAttribPointer(locationPositionAttrib, 3, GL_FLOAT, GL_FALSE, vertex_data_dtype.itemsize, ctypes.c_void_p(vertex_data_dtype.fields['position'][1]))
        glEnableVertexAttribArray(0)

        locationTextureAttrib = glGetAttribLocation(program, "aTexCoord")
        glVertexAttribPointer(locationTextureAttrib, 2, GL_FLOAT, GL_FALSE, vertex_data_dtype.itemsize, ctypes.c_void_p(vertex_data_dtype.fields['texture'][1]))
        glEnableVertexAttribArray(1)

        glBindVertexArray(0)

    def draw(self):
        glBindVertexArray(self.obj_vao)
        glDrawArrays(GL_QUADS, 0, len(self.blocks) * 24)
        glBindVertexArray(0)
