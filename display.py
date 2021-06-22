import sdl2
import sdl2.ext


class Display:
    def __init__(self, size, position=None):
        sdl2.ext.init()
        self.size = size
        self.position = position
        self.window = sdl2.ext.Window("SLAM", size=size, position=position)
        self.window.show()

    def poll(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)

    def paint(self, image):
        surface = sdl2.ext.pixels3d(self.window.get_surface())
        surface[:, :, 0:3] = image.swapaxes(0, 1)
        self.window.refresh()