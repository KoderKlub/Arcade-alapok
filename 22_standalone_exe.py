import arcade


"""
# pyinstaller telepítése
pip install pyinstaller


# futtatható .exe állomány generálása - első verzió
>>>pyinstaller platformer.py --windowed

# második verzió
# hozd létre az assets mappát, és másold bele a my-maps, my-sounds, my-sprites mappákat
>>>pyinstaller platformer.py --add-data "assets;assets" --windowed
"""

# Fizika.
MOVEMENT_SPEED = 12
JUMP_SPEED = 50
GRAVITY = 5

# Ablak méretei.
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_HALF_WIDTH = WINDOW_WIDTH / 2

# Pálya méretei.
TILE_WIDTH = 70
MAP_WIDTH = 31 * TILE_WIDTH
MAP_HEIGHT = 10 * TILE_WIDTH


# Behatárolja a játékos mozgásterét a megadott minimum és a maximum értékek között.
def clamp1(value, _min, _max):
    if value <= _min:
        return _min
    if value >= _max:
        return _max
    return value


# Ugyanaz mint a clamp1 függvény, csak rövidebb.
def clamp2(value, _min, _max):
    return max(min(value, _max), _min)


# Player osztály ami az arcade.Sprite-ból örököl.
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(center_x=100, center_y=300)
        self.textures = []

        self.textures.append(arcade.load_texture("my-sprites/greene.png"))
        self.textures.append(arcade.load_texture("my-sprites/greene.png", flipped_horizontally=True))

        self.texture = self.textures[0]

    def update_texture(self):
        # Mindig csekkoljuk, hogy a change_x nagyobb, vagy épp kisseb mint 0, és ez alapján jelenítjük meg a textúrát.
        if self.change_x > 0:
            self.texture = self.textures[0]
        elif self.change_x < 0:
            self.texture = self.textures[1]


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        map = arcade.read_tmx("my-maps/platfomer-map.tmx")
        self.talaj = arcade.tilemap.process_layer(map, "talaj", use_spatial_hash=True)
        self.egyeb = arcade.tilemap.process_layer(map, "egyeb", use_spatial_hash=True)
        self.targyak = arcade.tilemap.process_layer(map, "targyak", use_spatial_hash=True)

        # Példányosítjuk a Player osztályt.
        self.player = Player()
        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.talaj, gravity_constant=GRAVITY)

        self.collected = 0

        self.sound = arcade.Sound("my-sounds/coin1.wav")
        self.music = arcade.Sound("my-sounds/funkyrobot.mp3")
        self.music.play(volume=0.1)

    def on_draw(self):
        arcade.start_render()
        self.talaj.draw()
        self.egyeb.draw()
        self.targyak.draw()
        self.player.draw()

        arcade.draw_text(f"collected: {self.collected}", arcade.get_viewport()[0] + 10, 680, arcade.color.GOLD, font_size=20)

    def on_update(self, delta_time: float):
        self.physics.update()
        self.player.update_texture()

        # A clamp függvénnyel behatároljuk a player mozgásterét az x tengelyen (min=25, max=2075).
        self.player.center_x = clamp1(self.player.center_x, 25, MAP_WIDTH - TILE_WIDTH - 25)

        if WINDOW_HALF_WIDTH < self.player.center_x < MAP_WIDTH - TILE_WIDTH - WINDOW_HALF_WIDTH:
            change_view = True
        else:
            change_view = False

        if change_view:  # left, right, bottom, top
            arcade.set_viewport(self.player.center_x - WINDOW_HALF_WIDTH,
                                self.player.center_x + WINDOW_HALF_WIDTH, 0, WINDOW_HEIGHT)

        collected = arcade.check_for_collision_with_list(self.player, self.targyak)
        for coll in collected:
            coll.kill()
            self.collected += 1
            self.sound.play(volume=0.2)

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
