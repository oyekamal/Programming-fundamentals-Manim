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
        programming = Tex('In Programming')
        condition.set_color_by_tex('if else', YELLOW)

        # self.camera.background_color = GREEN_A
        key = EmojiSVGMobject('🔑').scale(0.5)
        door1 = EmojiSVGMobject('🚪').scale(1.2).move_to(LEFT*3)
        door2 = EmojiSVGMobject('🚪').scale(1.2)
        door3 = EmojiSVGMobject('🚪').scale(1.2).move_to(RIGHT*3)

        cloth1 = EmojiSVGMobject('👚').scale(0.5).move_to(LEFT*3 + DOWN*2)
        cloth2 = EmojiSVGMobject('🥻').scale(0.5).move_to(DOWN*2)
        cloth3 = EmojiSVGMobject('👗').scale(0.5).move_to(RIGHT*3 + DOWN*2)

        abc = Tex('A', 'B', 'C')
        abc[0].move_to(LEFT*3)
        abc[2].move_to(RIGHT*3)
        B = Text('B').move_to(DOWN*2)
        box1 = always_redraw(lambda: SurroundingRectangle(
            abc[0], color=BLUE, fill_opacity=0.2, fill_color=BLUE_D, buff=1))

        box2 = always_redraw(lambda: SurroundingRectangle(
            abc[1], color=YELLOW, fill_opacity=0.2, fill_color=BLUE_D, buff=1))

        box3 = always_redraw(lambda: SurroundingRectangle(
            abc[2], color=GREEN, fill_opacity=0.2, fill_color=BLUE_D, buff=1))

        condition1 = always_redraw(lambda: Tex(
            "if A==B ", color=BLUE).next_to(box1, UP, buff=0.5))

        condition2 = always_redraw(lambda: Tex(
            "if B==B ", color=YELLOW).next_to(box2, UP, buff=0.5))

        condition3 = always_redraw(lambda: Tex(
            "if C==B ", color=GREEN).next_to(box3, UP, buff=0.5))

        code = '''print('found B')'''
        rendered_code = Code(code=code, tab_width=4, background="window", style='one-dark',
                             language="Python", font="Monospace")

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

        self.play(FadeOut(VGroup(cloth2, cloth1, cloth3), shift=DOWN))
        self.play(Uncreate(door2))
        self.play(FadeIn(programming))
        self.play(FadeOut(programming))
        self.play(Create(VGroup(
            abc[0], box1, abc[1], box2, abc[2], box3, B, condition1, condition2, condition3)))

        self.play(B.animate.move_to(DOWN*2 + LEFT*3))
        self.play(Indicate(VGroup(B, condition1), color=RED))
        self.play(B.animate.move_to(DOWN*2))
        self.play(Indicate(VGroup(B, condition2), color=GREEN))
        self.play(
            Uncreate(VGroup(abc[0], box1, abc[2], box3, B, condition1, condition3)))
        self.play(abc[1].animate.move_to(LEFT*4))
        self.play(FadeIn(rendered_code, target_position=box2.get_center()))
        self.wait()
