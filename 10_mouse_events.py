import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()
        self.background_color = (25, 25, 25, 255)

        self.set_mouse_visible(False)

        # zöld kör x pozíciója
        self.green_circle_x = 640
        # zöld kör y pozíciója
        self.green_circle_y = 360

        # kék kör x pozíciója
        self.blue_circle_x = 100
        # kék kör y pozíciója
        self.blue_circle_y = 250

        # piros körvonal x pozíciója
        self.red_circle_x = 350
        # piros körvonal y pozíciója
        self.red_circle_y = 150

    # Ebben a metódusban rajzoljuk meg az alakzatokat.
    def on_draw(self):
        arcade.start_render()

        # zöld kör
        arcade.draw_ellipse_filled(self.green_circle_x, self.green_circle_y, 80, 80, arcade.color.GREEN)
        arcade.draw_ellipse_outline(self.green_circle_x, self.green_circle_y, 80, 80, arcade.color.YELLOW, 2)
        arcade.draw_text(f"green x: {self.green_circle_x:.2f} - green y: {self.green_circle_y:.2f}",
                         10, 720 - 20, arcade.color.GREEN, 16)

        # kék kör
        arcade.draw_ellipse_filled(self.blue_circle_x, self.blue_circle_y, 80, 80, arcade.color.BLUE)
        arcade.draw_ellipse_outline(self.blue_circle_x, self.blue_circle_y, 80, 80, arcade.color.YELLOW, 2)
        arcade.draw_text(f"blue x: {self.blue_circle_x:.2f} - blue y: {self.blue_circle_y:.2f}",
                         10, 720 - 40, arcade.color.BABY_BLUE, 16)

        # piros körvonal
        arcade.draw_ellipse_outline(self.red_circle_x, self.red_circle_y, 80, 80, arcade.color.RED, 2)
        arcade.draw_text(f"red x: {self.red_circle_x:.2f} - red y: {self.red_circle_y:.2f}",
                         10, 720 - 60, arcade.color.RED, 16)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.green_circle_x = x
            self.green_circle_y = y
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.blue_circle_x = x
            self.blue_circle_y = y

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.red_circle_x = x
        self.red_circle_y = y

    def on_mouse_enter(self, x, y):
        print(x, y)

    def on_mouse_leave(self, x, y):
        print(x, y)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        print(scroll_y)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        pass


win = GameWindow(1280, 720, "Game Window")
arcade.run()
