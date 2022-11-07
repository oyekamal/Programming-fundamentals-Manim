from manim import *


# %%manim -v WARNING --disable_caching -qm -r400,400 Example1

from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class EmojiSVGMobject(SVGMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = '-'.join(f'{ord(c):x}' for c in emoji)
        emoji_code = emoji_code.upper()  # <-  needed for openmojis
        url = f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{emoji_code}.svg'
        path_svg = Path.cwd() / f'{emoji_code}.svg'
        urllib.request.urlretrieve(url, path_svg)
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class Condition(Scene):
    def construct(self):
        condition = Tex('Condition ', ' / ', 'if else')
        condition.set_color_by_tex('if else', YELLOW)

        # self.camera.background_color = GREEN_A
        key = EmojiSVGMobject('🔑').scale(0.5)
        door1 = EmojiSVGMobject('🚪').scale(1.2).move_to(LEFT*3)
        door2 = EmojiSVGMobject('🚪').scale(1.2)
        door3 = EmojiSVGMobject('🚪').scale(1.2).move_to(RIGHT*3)

        cloth1 = EmojiSVGMobject('👚').scale(0.5).move_to(LEFT*3 + DOWN*2)
        cloth2 = EmojiSVGMobject('🥻').scale(0.5).move_to(DOWN*2)
        cloth3 = EmojiSVGMobject('👗').scale(0.5).move_to(RIGHT*3 + DOWN*2)
        # t = Text('OpenMoji (SVG)').scale(2)
        # Group(em, t).arrange(DOWN).scale(1.4)

        self.play(Write(condition))
        self.wait()
        self.play(condition.animate.to_edge(UL).scale(0.6))
        self.wait()
        self.play(FadeIn(key, shift=DOWN))
        self.play(Indicate(key))
        self.play(key.animate.to_edge(DL, buff=1.5))
        # self.play(FadeIn(door1, shift=LEFT),FadeIn(door2,shift=UP),FadeIn(door3,shift=RIGHT))
        self.play(Create(VGroup(door1, door2, door3), rate_time=4))
        self.play(FocusOn(door1), FocusOn(door2), FocusOn(door3))
        self.wait()

        curved1 = always_redraw(lambda: CurvedArrow(
            key.get_right(), door1.get_bottom(), color=BLUE_E))

        curved2 = always_redraw(lambda: CurvedArrow(
            key.get_right(), door2.get_bottom(), color=BLUE_E))

        curved3 = always_redraw(lambda: CurvedArrow(
            key.get_right(), door3.get_bottom(), color=BLUE_E))

        self.play(Create(VGroup(curved1, curved2, curved3)))

        self.play(key.animate.move_to(RIGHT*2).move_to(DOWN*2.2))
        self.wait()
        self.play(FadeOut(VGroup(curved1, curved2, curved3)))

        self.play(key.animate.move_to(LEFT*2))
        self.play(Indicate(key, color=RED))
        self.wait()

        self.play(key.animate.move_to(RIGHT))
        self.play(Indicate(key, color=GREEN), FocusOn(door2))

        self.wait()
        self.play(Uncreate(VGroup(door3, door1, key)))
        self.play(FadeIn(cloth1, target_position=door2.get_center()),
                  FadeIn(cloth2, target_position=door2.get_center()),
                  FadeIn(cloth3, target_position=door2.get_center()))
        self.wait()
