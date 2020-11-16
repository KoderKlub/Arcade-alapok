import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # self.set_location(400, 100)
        self.center_window()

    def on_draw(self):
        arcade.start_render()

        # Circle - Kör
        arcade.draw_circle_filled(240, 360, 30, arcade.color.BLUE)
        arcade.draw_circle_outline(340, 360, 30, arcade.color.BUFF)

        # Ellipse - Ellipszis
        arcade.draw_ellipse_filled(100, 100, 50, 80, arcade.color.AO)
        arcade.draw_ellipse_outline(200, 100, 50, 80, arcade.color.YELLOW)

        # Rectangle - Téglalap
        arcade.draw_rectangle_filled(300, 100, 50, 50, arcade.color.ALIZARIN_CRIMSON)
        arcade.draw_rectangle_outline(400, 100, 50, 150, arcade.color.YANKEES_BLUE, 4)

        # Text - Szöveg
        arcade.draw_text("Kóder Klub", 20, 720-80, arcade.color.AQUA, 24)

        # Arc - Ív
        arcade.draw_arc_filled(640, 720-80, 120, 120, arcade.color.YELLOW_ORANGE, 0, 90)
        arcade.draw_arc_filled(1040, 720-80, 120, 120, arcade.color.YELLOW_ORANGE, 0, 270)

        # Triangle - Háromszög
        arcade.draw_polygon_outline([[0, 0], [50, 0], [25, 50]], arcade.color.AFRICAN_VIOLET)

        # Pentagon - Ötszög
        arcade.draw_polygon_outline([[640, 360],
                                     [640 + 50, 360],
                                     [640 + 75, 360 + 25],
                                     [640 + 25, 360 + 50],
                                     [640 - 25, 360 + 25]], arcade.color.ALLOY_ORANGE)


win = GameWindow(1280, 720, "Game Window")
arcade.run()