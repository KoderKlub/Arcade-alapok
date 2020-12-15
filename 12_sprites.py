import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.ship1 = arcade.Sprite("my-sprites/playerShip_green.png", center_x=640, center_y=360)
        self.ship2 = arcade.Sprite("my-sprites/playerShip_orange.png", center_x=440, center_y=360)
        self.ship3 = arcade.Sprite("my-sprites/playerShip2_orange.png", center_x=240, center_y=360)
        self.ship4 = arcade.Sprite("my-sprites/playerShip3_orange.png", center_x=840, center_y=360)

        # batch rendering with SpriteList
        self.ship_list = arcade.SpriteList()
        self.ship_list.append(self.ship2)
        self.ship_list.append(self.ship3)
        self.ship_list.append(self.ship4)

        self.angle = 0

    def on_draw(self):
        arcade.start_render()
        self.ship1.draw()
        self.ship_list.draw()
        # self.ship2.draw()
        # self.ship3.draw()
        # self.ship4.draw()

    def on_update(self, delta_time: float):
        self.angle += 1
        self.ship1.angle = -self.angle


win = GameWindow(1280, 720, "Game Window")
arcade.run()
