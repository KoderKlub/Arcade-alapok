import arcade

# win = arcade.Window(1280, 720, "Ablak")
# arcade.run()


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 100)


win = GameWindow(1280, 720, "Game Window")
arcade.run()