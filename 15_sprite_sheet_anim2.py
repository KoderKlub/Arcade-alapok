import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.player = arcade.AnimatedWalkingSprite()
        self.player.stand_left_textures.append(arcade.load_texture("my-sprites/top-down.png", x=0, y=64, width=64, height=64))
        self.player.stand_right_textures.append(arcade.load_texture("my-sprites/top-down.png", x=0, y=128, width=64, height=64))

        for i in range(4):
            texture = arcade.load_texture("my-sprites/top-down.png", x=i*64, y=0, width=64, height=64)
            self.player.walk_down_textures.append(texture)

        for i in range(4):
            texture = arcade.load_texture("my-sprites/top-down.png", x=i*64, y=64, width=64, height=64)
            self.player.walk_left_textures.append(texture)

        for i in range(4):
            texture = arcade.load_texture("my-sprites/top-down.png", x=i*64, y=128, width=64, height=64)
            self.player.walk_right_textures.append(texture)

        for i in range(4):
            texture = arcade.load_texture("my-sprites/top-down.png", x=i*64, y=192, width=64, height=64)
            self.player.walk_up_textures.append(texture)

        self.player.center_x = 640
        self.player.center_y = 360

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.player.change_y = 2
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -2
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -2
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = 2

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()


win = GameWindow(1280, 720, "Game Window")
arcade.run()
