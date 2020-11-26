import arcade
import random

# Háttérben lévő csillagok színe.
bg_star_color = arcade.make_transparent_color(arcade.color.WHITE, 95)
# Előtérben lévő csillagok színei.
fg_star_colors = [arcade.color.WHITE, arcade.color.BABY_BLUE, arcade.color.AQUA, arcade.color.BUFF, arcade.color.ALIZARIN_CRIMSON]


# Ez a függvény hozza létre a csillagokat, és hozzádja őket a ShapeElementList-hez (batch).
def create_starfield(shape_list, color=bg_star_color, random_color=False):
    for i in range(200): # 200 darab csillag
        x = random.randint(0, 1280) # csillag x pozíciója 0-1280 között
        y = random.randint(0, 720) # csillag y pozíciója 0-720 között
        w = random.randint(1, 3) # csillag széllessége 1-3 pixel között
        h = random.randint(1, 3) # csillag magassága 1-3 pixel között
        if random_color: # Ha a random_color True,
            color = random.choice(fg_star_colors) # akkor véletlenszerűen kiválasztunk egy színt a fg_star_colors-ból
        star = arcade.create_rectangle_filled(x, y, w, h, color) # minden csillag egy kicsi négyszög lesz
        shape_list.append(star) # Itt adjuk hozzá a ShapeElementList-hez az új csillagot.


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # Az első csillagmező, előtérben.
        self.fg_stars1 = arcade.ShapeElementList()
        create_starfield(self.fg_stars1, random_color=True)

        # Az második csillagmező, előtérben.
        self.fg_stars2 = arcade.ShapeElementList()
        self.fg_stars2.center_y = 720 # Ezt az ablak tetejére helyezzük.
        create_starfield(self.fg_stars2, random_color=True)

        # Az első csillagmező, háttérben.
        self.bg_stars1 = arcade.ShapeElementList()
        create_starfield(self.bg_stars1)

        # Az második csillagmező, háttérben.
        self.bg_stars2 = arcade.ShapeElementList()
        self.bg_stars2.center_y = 720 # Ezt az ablak tetejére helyezzük.
        create_starfield(self.bg_stars2)

        # Előtérben lévő csillagok mozgási sebessége.
        self.fg_star_speed = 100
        # Háttérben lévő csillagok mozgási sebessége.
        self.bg_star_speed = 60

    def on_draw(self):
        arcade.start_render()

        # Csillag batch-ok megrajzolása.
        self.fg_stars1.draw()
        self.fg_stars2.draw()
        self.bg_stars1.draw()
        self.bg_stars2.draw()

        # Háromszög - űrhajó :)
        arcade.draw_triangle_filled(640, 20, 640 + 100, 20, 640 + 50, 100 + 20, arcade.color.BABY_BLUE)

    # Ez a metódus mozgatja a csillagokat. Ezt hívjuk meg az on_update metódusban.
    def move_stars(self, dt):
        # Minden frame-ben levonunk az előtérben lévő csillagmező y pozíziójából, 100 * dt értéket.
        self.fg_stars1.center_y -= self.fg_star_speed * dt
        self.fg_stars2.center_y -= self.fg_star_speed * dt

        # Minden frame-ben levonunk a háttérben lévő csillagmező y pozíziójából, 60 * dt értéket.
        self.bg_stars1.center_y -= self.bg_star_speed * dt
        self.bg_stars2.center_y -= self.bg_star_speed * dt

        # Ha bármelyik csillagmező y pozíciója kisseb mint -720, akkor a 720-as pozícióba (ablak teteje) helyezzük.
        if self.fg_stars1.center_y < -720:
            self.fg_stars1.center_y = 720
        if self.fg_stars2.center_y < -720:
            self.fg_stars2.center_y = 720
        if self.bg_stars1.center_y < -720:
            self.bg_stars1.center_y = 720
        if self.bg_stars2.center_y < -720:
            self.bg_stars2.center_y = 720

    def on_update(self, delta_time: float):
        # Itt már csak a move_star metódust hívjuk minden másodpercben hatvanszor.
        self.move_stars(delta_time)


win = GameWindow(1280, 720, "Starfield")
arcade.run()
