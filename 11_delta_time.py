import arcade
import timeit

"""
frissítési rátától függő mozgás
5 * 60 = 300 (pixel per sec)
5 * 30 = 150 (pixel per sec)
5 * 15 =  75 (pixel per sec)

frissítési rátától független mozgás
300 * (1/60) =  5 * 60 = 300 (pixel per sec)
300 * (1/30) = 10 * 30 = 300 (pixel per sec)
300 * (1/15) = 20 * 15 = 300 (pixel per sec)
"""


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1/60)
        self.center_window()
        self.background_color = (25, 25, 25, 255)

        # zöld kör x pozíciója
        self.green_circle_x = 40
        # zöld kör y pozíciója
        self.green_circle_y = 360

        self.speed = 300
        self.start_time = timeit.default_timer()
        self.end_time = None
        self.switch = True

    # Ebben a metódusban rajzoljuk meg az alakzatokat. (frame rate - képkocka ráta)
    def on_draw(self):
        arcade.start_render()

        # zöld kör
        arcade.draw_ellipse_filled(self.green_circle_x, self.green_circle_y, 80, 80, arcade.color.GREEN)
        arcade.draw_text(f"green x: {self.green_circle_x:.2f} - green y: {self.green_circle_y:.2f}",
                         10, 720 - 20, arcade.color.GREEN, 16)

    # Ebben a metódusban mozgatjuk az alakzatokat. (update rate - frissítési ráta)
    def on_update(self, delta_time: float):
        if self.green_circle_x < 1280 - 40:
            self.green_circle_x += self.speed * delta_time
        else:
            if self.switch:
                self.end_time = timeit.default_timer() - self.start_time
                print(self.end_time)
                self.switch = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.green_circle_x = 40


win = GameWindow(1280, 720, "Game Window")
arcade.run()
