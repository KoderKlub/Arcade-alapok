import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()
        self.background_color = (25, 25, 25, 255)

        self.player1 = arcade.Sprite("my-sprites/playerShip_green.png", center_x=640, center_y=360)
        self.player2 = arcade.Sprite("my-sprites/playerShip_green.png", center_x=940, center_y=200)
        self.enemy1 = arcade.Sprite("my-sprites/playerShip_orange.png", center_x=440, center_y=160)
        self.enemy2 = arcade.Sprite("my-sprites/playerShip2_orange.png", center_x=240, center_y=360)
        self.enemy3 = arcade.Sprite("my-sprites/playerShip3_orange.png", center_x=840, center_y=560)

        # batch rendering with SpriteList
        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(self.enemy1)
        self.enemy_list.append(self.enemy2)
        self.enemy_list.append(self.enemy3)

        self.speed = 300
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.draw_hit_boxes = False

    def on_draw(self):
        arcade.start_render()
        self.player1.draw()
        self.player2.draw()
        self.enemy_list.draw()

        if self.draw_hit_boxes:
            # draw hit boxes, only for debugging
            self.player1.draw_hit_box(arcade.color.YELLOW)
            self.player2.draw_hit_box(arcade.color.YELLOW)
            self.enemy_list.draw_hit_boxes(arcade.color.YELLOW)

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
        if symbol == arcade.key.SPACE:
            self.draw_hit_boxes = not self.draw_hit_boxes

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
            self.player1.center_x += -self.speed * delta_time
        if self.right:
            self.player1.center_x += self.speed * delta_time
        if self.up:
            self.player1.center_y += self.speed * delta_time
        if self.down:
            self.player1.center_y += -self.speed * delta_time

        hit = arcade.check_for_collision_with_list(self.player1, self.enemy_list)
        if hit:
            self.player1.color = (255, 0, 0, 255)
        else:
            self.player1.color = (255, 255, 255, 255)

        if arcade.check_for_collision(self.player1, self.player2):
            self.player1.color = (0, 255, 0, 255)




win = GameWindow(1280, 720, "Game Window")
arcade.run()
