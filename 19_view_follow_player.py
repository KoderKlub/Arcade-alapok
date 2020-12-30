import arcade

# Physics
MOVEMENT_SPEED = 12
JUMP_SPEED = 50
GRAVITY = 5

# Window sizes
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_HALF_WIDTH = WINDOW_WIDTH / 2

# Map sizes
TILE_WIDTH = 70
MAP_WIDTH = 31 * TILE_WIDTH
MAP_HEIGHT = 10 * TILE_WIDTH


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        map = arcade.read_tmx("my-maps/platfomer-map.tmx")
        self.talaj = arcade.tilemap.process_layer(map, "talaj", use_spatial_hash=True)
        self.egyeb = arcade.tilemap.process_layer(map, "egyeb", use_spatial_hash=True)

        self.player = arcade.Sprite("my-sprites/greene.png", center_x=100, center_y=300)

        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.talaj, gravity_constant=GRAVITY)

    def on_draw(self):
        arcade.start_render()
        self.talaj.draw()
        self.egyeb.draw()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.physics.update()

        if WINDOW_HALF_WIDTH < self.player.center_x < MAP_WIDTH - TILE_WIDTH - WINDOW_HALF_WIDTH:
            change_view = True
        else:
            change_view = False

        if change_view:  # left, right, bottom, top
            arcade.set_viewport(self.player.center_x - WINDOW_HALF_WIDTH,
                                self.player.center_x + WINDOW_HALF_WIDTH, 0, WINDOW_HEIGHT)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        if symbol == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        if symbol == arcade.key.UP:
            if self.physics.can_jump():
                self.player.change_y = JUMP_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0


win = GameWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "Game Window")
arcade.run()