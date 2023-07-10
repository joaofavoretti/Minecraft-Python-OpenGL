import glfw
from OpenGL.GL import *

class Scene:
    shaders = []

    def __init__ (self, width, height, window_title):
        self.width = width
        self.height = height
        self.window_title = window_title
    
    def __init_window__(self):
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
        glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)

        window = glfw.create_window(self.width, self.height, self.window_title, None, None)
        if not window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")

        glfw.make_context_current(window)

        return window

    def __init_program__(self):
        program = glCreateProgram()

        return program

    def __setup_shader__(self, program, shader_code, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, shader_code)
        glCompileShader(shader)

        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader))

        glAttachShader(program, shader)

        return shader        

    def __build_program__(self, program):
        glLinkProgram(program)

        if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(program))

    def __start_program__(self, program):
        glUseProgram(program)

    def __set_background_color__ (self, window, rgb_color):
        r, g, b = rgb_color
        
        a = 1.0

        glClearColor(r/255, g/255, b/255, a)


    def add_shader(self, shader_code, shader_type):
        self.shaders.append(
            {
                "shader": None,
                "shader_code": shader_code,
                "shader_type": shader_type
            }
        )

    def start(self):
        glfw.init()

        self.window = self.__init_window__()

        self.program = self.__init_program__()

        for shader in self.shaders:
            shader["shader"] = self.__setup_shader__(self.program, shader["shader_code"], shader["shader_type"])

        self.__build_program__(self.program)

        self.__start_program__(self.program)

        color = (173, 216, 230)
        self.__set_background_color__(self.window, color)

        glEnable(GL_DEPTH_TEST)

        glfw.show_window(self.window)

    def run(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glfw.swap_buffers(self.window)

        glfw.terminate()