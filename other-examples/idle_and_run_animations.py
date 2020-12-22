import arcade

FACE_RIGHT = 1
FACE_LEFT = 2


# Custom Animated Sprite class with two animations.
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.idle_left_textures = []
        self.idle_right_textures = []
        self.run_left_textures = []
        self.run_right_textures = []

        # 6 idle frames, flipped horizontally
        for i in range(6):
            texture = arcade.load_texture("../my-sprites/Idle.png", x=i*184, y=0, width=184, height=137, flipped_horizontally=True)
            self.idle_left_textures.append(texture)

        # 6 idle frames
        for i in range(6):
            texture = arcade.load_texture("../my-sprites/Idle.png", x=i*184, y=0, width=184, height=137)
            self.idle_right_textures.append(texture)

        # 8 running frames, flipped horizontally
        for i in range(8):
            texture = arcade.load_texture("../my-sprites/Run.png", x=i*184, y=0, width=184, height=137, flipped_horizontally=True)
            self.run_left_textures.append(texture)

        # 8 running frames
        for i in range(8):
            texture = arcade.load_texture("../my-sprites/Run.png", x=i*184, y=0, width=184, height=137)
            self.run_right_textures.append(texture)

        self.center_x = 640
        self.center_y = 360

        self.cur_texture_index = 0
        self.state = FACE_RIGHT
        self.frame_timer = 0

    def update_animation(self, delta_time: float = 1/60):
        texture_list = []

        if self.change_x > 0:
            self.state = FACE_RIGHT
            texture_list = self.run_right_textures
        elif self.change_x < 0:
            self.state = FACE_LEFT
            texture_list = self.run_left_textures

        if self.change_x == 0:
            if self.state == FACE_LEFT:
                texture_list = self.idle_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.idle_right_textures

        # update the textures every 3rd frame
        self.frame_timer += 1
        if self.frame_timer > 3:
            self.frame_timer = 0
            self.cur_texture_index += 1

        if self.cur_texture_index >= len(texture_list):
            self.cur_texture_index = 0

        self.texture = texture_list[self.cur_texture_index]


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.player = Player()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player.change_x = -10
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = 10

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0


win = GameWindow(1280, 720, "Game Window")
arcade.run()
