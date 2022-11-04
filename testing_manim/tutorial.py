from math import radians
from manim import *
from manim import Scene


class Test(Scene):
    def construct(self):

        circle = Circle(radius=2.5, color=RED)

        self.play(Create(circle))


class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=RED, fill_color=BLUE_B, fill_opacity=0.4,
                    )

        self.play(Create(sq), run_time=5)
        self.wait(2)


class NameSquare(Scene):
    def construct(self):

        name = Tex("kamal").to_edge(UL, buff=0.5)
        sq = Square(side_length=2, fill_color=GOLD,
                    fill_opacity=1).shift(LEFT*4)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq))
        self.play(Create(tri))

        self.play(name.animate.to_edge(UR), run_time=2)

        self.play(sq.animate.scale(3), tri.animate.to_edge(DL), run_time=3)

        self.wait(2)


class Arrow(Scene):
    def construct(self):

        rect = Rectangle(color=YELLOW, height=2, width=3).to_edge(UR)

        circle = Circle().to_edge(DL)

        arrow = always_redraw(lambda: Line(
            start=rect.get_bottom(), end=circle.get_top(), buff=0.2).add_tip())

        self.play(Create(VGroup(rect, arrow, circle)))
        self.play(rect.animate.to_edge(UL),
                  circle.animate.scale(0.5), run_time=3)
        self.wait(2)


class Updater(Scene):
    def construct(self):
        num = MathTex('ln(2)')
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=RED, fill_opacity=0.5, fill_color=BLUE_D, buff=1))
        name = always_redraw(lambda: Tex(
            "kamal", color=GREEN).next_to(box, DOWN, buff=0.5))

        self.play(Create(VGroup(num, box, name)))

        self.play(num.animate.shift(RIGHT*5), run_time=2)

        self.wait(2)


class ValueTrackers(Scene):
    def construct(self):
        
        k = ValueTracker(10.3)
        
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
        
        self.play(FadeIn(num))

        self.wait(1)

        self.play(k.animate.set_value(0), run_time=4, rate_func=linear)
        self.wait(1)

# # %%manim -v WARNING --disable_caching -qm -r400,400 Example1
# from manim import *
# from PIL import Image
# import numpy as np
# import requests
# from pathlib import Path


# class EmojiImageMobject(ImageMobject):
#     def __init__(self, emoji, **kwargs):
#         emoji_code = '-'.join(f'{ord(c):x}' for c in emoji)
#         emoji_code = emoji_code.upper()  # <-  needed for openmojis
#         url = f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/618x618/{emoji_code}.png'
#         im = Image.open(requests.get(url, stream=True).raw)
#         emoji_img = np.array(im.convert('RGBA'))
#         ImageMobject.__init__(self, emoji_img, **kwargs)


# class Example1(Scene):
#     def construct(self):
#         self.camera.background_color = YELLOW_A
#         em = EmojiImageMobject('🤼').scale(.8)
#         # when using OpenEmoji, please give credits e.g. like this:
#         # 'All emojis designed by OpenMoji – the open-source emoji and icon project. License: CC BY-SA 4.0'
#         t = Text('OpenMoji').scale(2.5)
#         Group(em, t).arrange(DOWN).scale(1.5)
#         self.add(em, t)
