import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        map = arcade.read_tmx("my-maps/platfomer-map.tmx")
        self.talaj = arcade.tilemap.process_layer(map, "talaj")
        self.egyeb = arcade.tilemap.process_layer(map, "egyeb")


    def on_draw(self):
        arcade.start_render()
        self.talaj.draw()
        self.egyeb.draw()

    def on_update(self, delta_time: float):
        pass


win = GameWindow(1280, 720, "Game Window")
arcade.run()