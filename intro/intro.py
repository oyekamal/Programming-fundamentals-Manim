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


class Intro1(Scene):
    def construct(self):

        start = Text("Start Coding", gradient=(RED, GREEN, BLUE)).scale(2)
        t2gindices = Text(
            'Programming',
            t2g={
                'Programming': (BLUE, GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'Coding',
            t2g={
                'Coding': (GREEN, YELLOW),
            },
        ).next_to(t2gindices, RIGHT)

        theory_concept = Tex("Theory ", " Pure Coding Concepts").scale(1.5)

        theory_concept[1].set_color(YELLOW)
        theory_concept[0].set_color(BLUE)
        concept_box = SurroundingRectangle(
            theory_concept[1], corner_radius=0.1)

        cross = Cross(
            mobject=theory_concept[0], stroke_color=RED, stroke_width=6)

        pi = MathTex(r"\mathbb{A}").scale(7)
        pi.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=YELLOW, fill_opacity=0.4).shift(LEFT)
        square = Square(color=BLUE_D, fill_opacity=0.6).shift(UP)
        rectangle = Rectangle(fill_opacity=0.2).set_color(YELLOW)
        python = Text("Python", gradient=(RED, YELLOW, BLUE)).scale(2)

        list_of_content = Tex(
            # '$\\bullet$ Display Text on screen \\\\',
            '$\\bullet$ Variable \\\\',
            '$\\bullet$ Condition \\\\',
            '$\\bullet$ Loop \\\\',
            '$\\bullet$ Function \\\\',
            '$\\bullet$ List \\\\',
            '$\\bullet$ Dictionary \\\\',
        )

        list_of_content[0].set_color(YELLOW)
        list_of_content[1].set_color(BLUE)
        list_of_content[2].set_color(GREEN)
        list_of_content[3].set_color(GOLD)
        list_of_content[4].set_color(GRAY)
        list_of_content[5].set_color(WHITE)

        self.play(Create(VGroup(t2gindices, t2gwords), run_time=3))

        self.play(Wiggle(t2gindices), run_time=2)
        self.play(Wiggle(t2gwords), run_time=2)

        self.wait(3)

        self.play(FadeOut(VGroup(t2gindices, t2gwords)), run_time=4)

        shapes = VGroup(pi, circle, square)
        self.play(SpiralIn(shapes), run_time=2)

        self.wait(3)

        self.play(Transform(square, rectangle), circle.animate.set_fill(
            BLUE_D).scale(2.5), pi.animate.rotate(PI), run_time=2)
        self.wait(1)

        self.play(Uncreate(VGroup(pi, circle)),
                  FadeOut(VGroup(rectangle, square)))
        self.wait(1)

        self.play(Write(theory_concept[0]), FadeIn(cross), run_time=1)

        self.wait(2)

        self.play(ReplacementTransform(
            theory_concept[0], theory_concept[1]), FadeOut(cross))
        # self.wait(1)
        self.play(Create(concept_box))
        self.play((Indicate(concept_box)))
        self.wait(1)
        self.play(ReplacementTransform(
            theory_concept[1], python), FadeOut(concept_box))
        self.wait(4)
        self.play(FadeOut(python))
        self.wait()
        self.play(Write(list_of_content), run_time=6)
        self.wait(4)
        self.play(ReplacementTransform(list_of_content, start), run_time=3)
        self.wait(5)


# urdu time aedd