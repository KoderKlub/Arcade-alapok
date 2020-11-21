import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # A batch ami egy ShapeElementList objektum
        self.batch = arcade.ShapeElementList()

        # Ellipses - Ellipszisek
        ellipse1 = arcade.create_ellipse_filled(440, 360, 50, 50, arcade.color.ROSE)
        ellipse2 = arcade.create_ellipse_outline(640, 360, 50, 80, arcade.color.RED)
        ellipse3 = arcade.create_ellipse_filled_with_colors(840, 360, 50, 80, arcade.color.RED, arcade.color.BLUE, 45)

        # Triangle - Háromszög
        triangle = arcade.create_polygon([[0, 0], [100, 0], [50, 100]], arcade.color.BLUE)
        # Rectangle - Téglalap
        rect = arcade.create_rectangle_filled(100, 360, 100, 150, arcade.color.GREEN)
        # Invisible Rectangle 1 pixel - Láthatalan 1 pixel átmérőjű négyzet
        invisible_rect = arcade.create_rectangle_filled(0, 0, 1, 1, arcade.color.BLACK)

        # Itt adjuk hozzá a batch-oz a geometriai alakzatokat
        self.batch.append(ellipse1)
        self.batch.append(ellipse2)
        self.batch.append(ellipse3)
        self.batch.append(triangle)
        self.batch.append(rect)

        # Ezt mindig utoljára adjuk a batch-hoz, amíg a hibát ki nem javítják az Arcade fejlesztői.
        self.batch.append(invisible_rect)

    def on_draw(self):
        arcade.start_render()
        self.batch.draw()


win = GameWindow(1280, 720, "Game Window")
arcade.run()
