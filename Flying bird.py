import arcade
from pyglet.image import Animation

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750
SCREEN_TITLE = ""
GRAVITY=0.5
JUMP=10

class Animation(arcade.Sprite):
    time=0
    i=0
    def update_animation(self, delta_time: float = 1 / 60):
        self.time+=delta_time
        print(delta_time)
        if self.time>=0.2:
            self.time=0
            if len(self.textures)-1==self.i:
                self.i=0
            else:
                self.i+=1
            self.set_texture(self.i)

class Pipe  (Animation):
    def __init__(self, ):
        super().__init__(filename="183-1831473_flappy-bird-pipe-png-flappy-bird-pipe-transparent.png",scale=0.5)
    def movement(self, width, height):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Bird (Animation):
    def __init__(self, ):
        super().__init__(filename="загрузка (1).png",scale=0.5)
    def movement(self,width,height):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_y -= GRAVITY
        if self.top>SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        if self.bottom < 0:
            self.bottom = 0



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        """ Bird """
        self.bird= Bird()
        self.bird.center_x=self.width/2
        self.bird.center_y =self.width/2
        """ background """
        self.background_picture= arcade.load_texture("загрузка.jpg")
        """ Pipe sprite list  """
        self.pipes =arcade.SpriteList()
        for p in range(6):
            pipe_variable =Pipe()
            pipe_variable.center_x=250*p
            self.pipes.append(pipe_variable)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.bird.change_y = JUMP

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background_picture)
        self.bird.draw()
        self.pipes.draw()

    def on_update(self, delta_time):
        self.bird.movement(self.width,self.height )


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

"""
Нарисовать что-то (по желанию)
Сделать так, чтобы трубы двигались точно также, как и кактус (логика точно такая же)
+ тупо доделать проект до конца, постараться без гпт
"""