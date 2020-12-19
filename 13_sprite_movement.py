import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.ship1 = arcade.Sprite("my-sprites/playerShip_green.png", center_x=640, center_y=360)

        self.speed = 300
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        self.ship1.draw()

    # Valahányszor egy billentyűt lenyomunk, ez a metódus fog meghívódni.
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            # self.ship1.change_x = -self.speed
            self.left = True
        if symbol == arcade.key.RIGHT:
            # self.ship1.change_x = self.speed
            self.right = True
        if symbol == arcade.key.UP:
            # self.ship1.change_y = self.speed
            self.up = True
        if symbol == arcade.key.DOWN:
            # self.ship1.change_y = -self.speed
            self.down = True

    # Valahányszor egy billentyűt elengedünk, ez a metódus fog meghívódni.

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False

    # def on_key_release(self, symbol: int, modifiers: int):
    #     if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
    #         # self.ship1.change_x = 0
    #     if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
    #         # self.ship1.change_y = 0

    def on_update(self, delta_time: float):
        # self.ship1.update()
        if self.left:
            self.ship1.center_x += -self.speed * delta_time
        if self.right:
            self.ship1.center_x += self.speed * delta_time
        if self.up:
            self.ship1.center_y += self.speed * delta_time
        if self.down:
            self.ship1.center_y += -self.speed * delta_time


win = GameWindow(1280, 720, "Game Window")
arcade.run()
