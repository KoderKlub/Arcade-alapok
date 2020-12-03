import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # kör x pozíciója
        self.circle_x = 640
        # kör y pozíciója
        self.circle_y = 360

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.speed = 200

    # Ebben a metódusban rajzoljuk meg az alakzatokat.
    def on_draw(self):
        arcade.start_render()
        arcade.draw_ellipse_filled(self.circle_x, self.circle_y, 80, 80, arcade.color.AO)
        arcade.draw_ellipse_outline(self.circle_x, self.circle_y, 80, 80, arcade.color.YELLOW, 2)
        arcade.draw_text(f"x: {self.circle_x:.2f} - y: {self.circle_y:.2f}", 10, 720-20, arcade.color.WHITE, 16)

    # Valahányszor egy billentyűt lenyomunk, ez a metódus fog meghívódni.
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

        # Billentyű kombinációk módosítók használatával.
        if modifiers & arcade.key.MOD_SHIFT and symbol == arcade.key.C:
            print("Shift+C")
        if modifiers & arcade.key.MOD_CTRL and modifiers & arcade.key.MOD_ALT and symbol == arcade.key.C:
            print("CTRL+ALT+C")

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

    def on_update(self, delta_time: float):
        if self.left:
            self.circle_x -= self.speed * delta_time
        if self.right:
            self.circle_x += self.speed * delta_time
        if self.up:
            self.circle_y += self.speed * delta_time
        if self.down:
            self.circle_y -= self.speed * delta_time


win = GameWindow(1280, 720, "Game Window")
arcade.run()
