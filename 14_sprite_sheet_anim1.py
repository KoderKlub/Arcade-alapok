import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # Girl animation
        self.girl = arcade.AnimatedTimeBasedSprite("my-sprites/girl.png", image_x=0, image_y=0,
                                                   image_width=256, image_height=256)

        # loading the frames using a for loop
        for i in range(6):
            texture = arcade.load_texture("my-sprites/girl.png", x=i*256, y=0, width=256, height=256)
            self.girl.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=80, texture=texture))

        # girl position
        self.girl.center_x = 240
        self.girl.center_y = 360

        # --------------------------------------------------------------------------------------------

        # Cat animation
        self.cat = arcade.AnimatedTimeBasedSprite("my-sprites/cat.png", image_x=0, image_y=0,
                                                  image_width=512, image_height=256)

        # loading the frames individually
        # frame 1
        texture = arcade.load_texture("my-sprites/cat.png", x=0, y=0, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=50, texture=texture))

        # frame 2
        texture = arcade.load_texture("my-sprites/cat.png", x=512, y=0, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=1, duration=50, texture=texture))

        # frame 3
        texture = arcade.load_texture("my-sprites/cat.png", x=0, y=256, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=2, duration=50, texture=texture))

        # frame 4
        texture = arcade.load_texture("my-sprites/cat.png", x=512, y=256, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=3, duration=50, texture=texture))

        # frame 5
        texture = arcade.load_texture("my-sprites/cat.png", x=0, y=512, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=4, duration=50, texture=texture))

        # frame 6
        texture = arcade.load_texture("my-sprites/cat.png", x=512, y=512, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=5, duration=50, texture=texture))

        # frame 7
        texture = arcade.load_texture("my-sprites/cat.png", x=0, y=768, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=6, duration=50, texture=texture))

        # frame 8
        texture = arcade.load_texture("my-sprites/cat.png", x=512, y=768, width=512, height=256)
        self.cat.frames.append(arcade.AnimationKeyframe(tile_id=7, duration=50, texture=texture))

        # cat position
        self.cat.center_x = 640
        self.cat.center_y = 360

    def on_draw(self):
        arcade.start_render()
        self.girl.draw()
        self.cat.draw()

    def on_update(self, delta_time: float):
        self.girl.update_animation()
        self.cat.update_animation()


win = GameWindow(1280, 720, "Game Window")
arcade.run()
