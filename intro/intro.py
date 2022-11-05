from manim import *


class Intro(Scene):
    def construct(self):
        ok = Text("OK",  t2c={'O': YELLOW}).scale(2)
        oykamal = Text("oykamal", t2c={'oy': YELLOW}).scale(2)
        lets = Text("lets start")

        message = Tex(
            r"I'm going to teach you the basic concept of ", r"Programming.")
        message[1].set_color(YELLOW)
        message1 = Tex(r"Which are use in lot of ",
                       r"Programming ", r"language.").scale(0.5)
        message1[1].set_color(YELLOW)
        example = Text("For Example.", color=RED)

        theory = Text("Theory", color=GREEN)

        cross = Cross(mobject=theory, stroke_color=RED, stroke_width=6)
        
        see_you = Text("See you in next video", color=GOLD_B)
        
        list_of_content = Tex(
            # '$\\bullet$ Display Text on screen \\\\',
            '$\\bullet$ Variable \\\\',
            '$\\bullet$ Condition \\\\',
            '$\\bullet$ Loop \\\\',
            '$\\bullet$ Function \\\\',
            '$\\bullet$ List \\\\',
            '$\\bullet$ Dictionary \\\\',
        )

        message.next_to(message1, UP)
        ok.next_to(lets, UP)

        self.wait(2)
        # self.play(Write(ok))
        self.play(Write(oykamal), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(oykamal, ok))
        self.play(Write(lets))
        self.play(FadeOut(ok), FadeOut(lets))
        self.wait(2)

        self.play(Write(theory), run_time=2)
        self.wait()

        self.play(Create(cross), run_time=2)

        self.play(FadeOut(theory), FadeOut(cross))

        self.play(Write(message), Write(message1))
        self.wait(3)
        self.play(FadeOut(message), FadeOut(message1))
        self.play(Write(example))
        self.play(example.animate.scale(0.4).to_edge(UL))
        self.wait(1)
        self.play(Write(list_of_content))
        self.wait(2)
        # self.play(FadeOut(list_of_content), FadeIn(see_you))
        self.play(ReplacementTransform(list_of_content, see_you))
        self.wait(2)