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

class PipeTop  (Animation):
    def __init__(self, ):
        super().__init__(filename="pixil-frame-0 (17).png",scale=2)
    def movement(self, width, height):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_x = -3
        self.angle = 180

class PipeBottom (Animation):
    def __init__(self, ):
        super().__init__(filename="pixil-frame-0 (17).png", scale=2)

    def movement(self, width, height):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_x = -3
class Bird (Animation):
    def __init__(self, ):
        super().__init__(filename="pixil-frame-0 (16).png",scale=5)
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
        self.pipes  =arcade.SpriteList()
        for p in range(6):
            bottom_pipe = PipeBottom()
            bottom_pipe.center_x = 350 * p + SCREEN_WIDTH
            bottom_pipe.center_y = 300

            top_pipe = PipeTop()
            top_pipe.center_x = 350 * p + SCREEN_WIDTH
            top_pipe.center_y = SCREEN_HEIGHT - 300

            self.pipes.append(bottom_pipe)
            self.pipes.append(top_pipe)
        for pipe in self.pipes:
            pipe.movement(self.width, self.height)
        """ Game reset """
        self.game_reset()

    def game_reset(self):
        self.game_status = True
        #self.player_point = 0
        self.bird.center_x = self.width / 2
        self.bird.center_y = self.height / 2
        self.bird.change_y = 0
        #self.dino_jumping.in_jump_momentum = False

        for i, pipe in enumerate(self.pipes):
            if i % 2 == 0:  # нижняя труба
                pipe.center_x = 350 * (i // 2) + SCREEN_WIDTH
                pipe.center_y = 300
            else:  # верхняя труба
                pipe.center_x = 350 * (i // 2) + SCREEN_WIDTH
                pipe.center_y = SCREEN_HEIGHT - 300
            pipe.change_x = -3


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.bird.change_y = JUMP
        if symbol == arcade.key.R:
            self.game_reset()

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.background_picture)
        self.bird.draw()
        self.pipes.draw()
        self.bird.draw_hit_box((255, 0, 0), 3)
        self.pipes.draw_hit_boxes((255, 0, 0), 3)

    def on_update(self, delta_time):
        if not self.game_status:
            return


        if arcade.check_for_collision_with_list(self.bird, self.pipes):
            self.game_status = False

            return


        self.bird.movement(self.width, self.height)


        for pipe in self.pipes:
            pipe.movement(self.width, self.height)


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

"""
Нарисовать что-то (по желанию)
Сделать так, чтобы трубы двигались точно также, как и кактус (логика точно такая же)
+ тупо доделать проект до конца, постараться без гпт
"""