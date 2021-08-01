import glfw


class Window:
    def __init__(self, widh:int, heigth:int, title:str):
        # initializing glfw library
        if not glfw.init():
            raise Exception("glfw can not be initialized")

        # creating the window
        self._win = glfw.create_window(widh,heigth, title, None, None)

        # check if window was created
        if not self._win:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        # set window's position
        glfw.set_window_pos(self._win, 400, 200)

        # make the context current
        glfw.make_context_current(self._win)

    def main_loop(self):
        # the main application loop
        while not glfw.window_should_close(self._win):
            glfw.poll_events()

            glfw.swap_buffers(self._win)

        # terminate glfw, free up allocated resources
        glfw.terminate()



