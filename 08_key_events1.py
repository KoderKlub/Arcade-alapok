import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # kör x pozíciója
        self.circle_x = 640
        # kör y pozíciója
        self.circle_y = 360

    # Ebben a metódusban rajzoljuk meg az alakzatokat.
    def on_draw(self):
        arcade.start_render()
        arcade.draw_ellipse_filled(self.circle_x, self.circle_y, 80, 80, arcade.color.AO)
        arcade.draw_ellipse_outline(self.circle_x, self.circle_y, 80, 80, arcade.color.YELLOW, 2)
        arcade.draw_text(f"x: {self.circle_x:.2f} - y: {self.circle_y:.2f}", 10, 720-20, arcade.color.WHITE, 16)

    # Valahányszor egy billentyűt lenyomunk, ez a metódus fog meghívódni.
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.circle_x -= 10
        if symbol == arcade.key.RIGHT:
            self.circle_x += 10
        if symbol == arcade.key.UP:
            self.circle_y += 10
        if symbol == arcade.key.DOWN:
            self.circle_y -= 10

    # Valahányszor egy billentyűt elengedünk, ez a metódus fog meghívódni.
    def on_key_release(self, symbol: int, modifiers: int):
        print("Elengedes!")


win = GameWindow(1280, 720, "Game Window")
arcade.run()
