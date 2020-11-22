import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.circle_x = 640 # kör x pozíciója
        self.circle_y = 360 # kör y pozíciója
        self.speed_x = 300 # x sebesség
        self.speed_y = 300 # y sebesség

    # Ebben a metódusban rajzoljuk meg az alakzatokat. 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_ellipse_filled(self.circle_x, self.circle_y, 80, 80, arcade.color.AO)
        arcade.draw_ellipse_outline(self.circle_x, self.circle_y, 80, 80, arcade.color.YELLOW, 2)
        arcade.draw_text(f"x: {self.circle_x:.2f} - y: {self.circle_y:.2f}", 10, 720-20, arcade.color.WHITE, 16)

    # Ebben a metódusban frissítjük a változókat.
    def on_update(self, delta_time: float):
        self.circle_x += self.speed_x * delta_time
        self.circle_y += self.speed_y * delta_time

        # Ha a kör x pozíciója nagyobb mint 1280 - 40.
        if self.circle_x > 1280 - 40:
            self.circle_x = 1280 - 40
            self.speed_x *= -1

        # Ha a kör x pozíciója kisseb mint 0 + 40.
        if self.circle_x < 0 + 40:
            self.circle_x = 0 + 40
            self.speed_x *= -1

        # Ha a kör y pozíciója nagyobb mint 720 - 40.
        if self.circle_y > 720 - 40:
            self.circle_y = 720 - 40
            self.speed_y *= -1

        # Ha a kör y pozíciója kisebb mint 0 + 40.
        if self.circle_y < 0 + 40:
            self.circle_y = 0 + 40
            self.speed_y *= -1


win = GameWindow(1280, 720, "Game Window")
arcade.run()
