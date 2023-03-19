from manimlib import *
from typing import Any
import numpy as np


class PresentationScene(Scene):
    current_subtitle = Text('')

    def subtitle(self, string, mode: Any = Text):
        self.play(FadeOut(self.current_subtitle), run_time=0.5)
        self.current_subtitle = mode(string, font='Times New Roman', font_size=40).to_corner(DOWN)
        self.play(ShowCreation(self.current_subtitle), run_time=2)

class S2Simplex(PresentationScene):
    def construct(self) -> None:
        # self.subtitle(r'Intuitively, we can use points, lines, surfaces')
        # self.wait()
        # self.subtitle(r'and some higher dimensional chunks')
        # self.wait()
        # self.subtitle(r'to build diverse topological objects.')
        # self.wait()
        # self.subtitle(r'We can generalize these bricks to arbitrary dimensions.')
        tex1 = Tex(r'\Delta^n:=\{(x_0,\dots,x_n)\in[0,1]^{n+1}:x_0+\dots+x_n=1\}', color=BLUE)
        self.wait()
        self.subtitle(r'Particularly, if n = 0, this is a point')
        self.play(ReplacementTransform(tex1, tex2 := Tex(r'\Delta^n:=\{x_0\in[0,1]^n:x_0=1\}', color=BLUE)))
        self.wait(0.5)
        self.play(ReplacementTransform(tex2, tex2_2 := Tex(r'\Delta^n:=\{1\}', color=BLUE)))
        self.wait()
        self.play(FadeOut(tex2_2))
        self.subtitle(r'If n = 1, then this will be a line segment.')
        # self.play(FadeIn())

class Scene3ExampleTorus(PresentationScene):
    def construct(self) -> None:
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6
        )
        self.subtitle(r'Hello everyone!')
        self.wait()
        self.subtitle(r'Today, we are going to talk about simplicial homology.')
        self.wait()
        self.play(FadeIn(torus1 := Torus(r1=2, r2=1, color=BLUE_E)))
        self.subtitle(r'As what you see, this is a torus.')
        self.play(Rotate(torus1, 225 * DEGREES, axis=UR, run_time=2))
        self.play(Rotate(torus1, 360 * DEGREES, axis=DR, run_time=2, about_point=ORIGIN))
        self.wait()
        self.subtitle(r'We could start from a point')
        self.wait()
        self.subtitle(r'cut the torus along a longitudinal circle and a meridional circle.')
        self.play(ShowCreation(circ1 := Circle(color=BLUE, radius=3).rotate(45 * DEGREES, axis=UR)))
        self.play(ShowCreation(circ2 := Circle(color=BLUE).shift(2 * LEFT)
                               .rotate(90 * DEGREES, axis=RIGHT)
                               .rotate(45 * DEGREES, axis=UR, about_point=ORIGIN)
                               ))
        self.play(FadeOut(torus1))
        self.subtitle(r'Then the torus surface can be unfolded into a square.')
        self.wait()
        self.play(ReplacementTransform(VGroup(circ1, circ2),
                                       rect1 := Square(4, color=BLUE)))
        self.play(FadeIn(arr_rect1 := VGroup(
            arr1 := Arrow(np.array([-2, -2, 0]), np.array([-2, 0, 0]), buff=0, color=BLUE),
            arr2 := Arrow(np.array([2, -2, 0]), np.array([2, 0, 0]), buff=0, color=BLUE),
            arr3 := Arrow(np.array([-2, -2, 0]), np.array([0, -2, 0]), buff=0, color=BLUE),
            arr4 := Arrow(np.array([-2, 2, 0]), np.array([0, 2, 0]), buff=0, color=BLUE),
        )))
        self.add(
            e_01 := Line(np.array([-2, -2, 0]), np.array([-2, 2, 0]), color=BLUE),
            e_02 := Line(np.array([-2, -2, 0]), np.array([2, -2, 0]), color=BLUE),
            e_13 := Line(np.array([-2, 2, 0]), np.array([2, 2, 0]), color=BLUE),
            e_23 := Line(np.array([2, -2, 0]), np.array([2, 2, 0]), color=BLUE),
        )
        self.subtitle(r'Note that the four points are identity')
        self.wait()
        self.subtitle(r'but it is good to assign them an order.')
        self.play(FadeIn(VGroup(
            v0 := Dot(np.array([-2, -2, 0])),
            v1 := Dot(np.array([-2, 2, 0])),
            v2 := Dot(np.array([2, -2, 0])),
            v3 := Dot(np.array([2, 2, 0])),
        )))
        self.play(ShowCreation(label_v := VGroup(
            Tex('v_0').next_to(v0, direction=LEFT),
            Tex('v_1').next_to(v1, direction=LEFT),
            Tex('v_2').next_to(v2),
            Tex('v_3').next_to(v3),
        )))
        self.play(ShowCreation(label_e := VGroup(
            Tex('a').next_to(Point(np.array([0, 2, 0])), direction=UP),
            Tex('a').next_to(Point(np.array([0, -2, 0])), direction=DOWN),
            Tex('b').next_to(Point(np.array([2, 0, 0])), direction=RIGHT),
            Tex('b').next_to(Point(np.array([-2, 0, 0])), direction=LEFT),
        )))
        self.subtitle(r'To show how it can be made up of simplices,')
        self.wait()
        self.subtitle(r'we can cut the square on the diagonal.')
        self.play(ShowCreation(e_c := Line(np.array([-2, -2, 0]), np.array([2, 2, 0]), color=BLUE)))
        self.play(FadeIn(arr_e_c := Arrow(np.array([-2, -2, 0]), np.array([0, 0, 0]), buff=0, color=BLUE)))
        self.play(ShowCreation(label_e_c := Tex('c').move_to(np.array([0, 0.3, 0]))))
        self.play(
            FadeIn(f_A := Polygon(np.array([2, 2, 0]), np.array([-2, 2, 0]), np.array([-2, -2, 0]),
                                  color=BLUE).set_fill(YELLOW, opacity=0.5)),
            FadeIn(f_B := Polygon(np.array([2, 2, 0]), np.array([2, -2, 0]), np.array([-2, -2, 0]),
                                  color=BLUE).set_fill(RED, opacity=0.5))
        )
        self.subtitle(r'Note that the edges always')
        self.wait()
        self.subtitle(r'go from a smaller vertex to a greater vertex.')
        self.wait()
        self.subtitle(r'Then it forms two triangles,')
        self.wait()
        self.subtitle(r'as known as, 2-dimensional Delta-simplices.')
        self.play(ShowCreation(label_f := VGroup(
            Tex('A').move_to(Point(np.array([-1, 1, 0]))),
            Tex('B').move_to(Point(np.array([1, -1, 0]))),
        )))
        self.subtitle(r'Now we know the torus is a 2-dimensional Delta-complex.')
        self.wait()
        self.subtitle(r'Therefore, we can induce the simplicial homology of torus.')
        self.wait()
        self.subtitle('Let\'s define the chain complexes,')
        self.wait()
        self.subtitle(r'which are the free abelian groups generated by the sets of simplices.')
        self.wait()
        self.subtitle(r'chained by the boundary homomorphisms.')
        diagram1 = VGroup(rect1, v0, v1, v2, v3, arr_rect1,
                          e_01, e_02, e_13, e_23, e_c, arr_e_c, label_e_c,
                          f_A, f_B, label_v, label_e, label_f)
        self.play(diagram1.to_edge, LEFT)
        self.play(ShowCreation(tex_chain := Tex(r'\dots\overset{\partial_4}{\to}'
                                                r'C_3\overset{\partial_3}{\to}'
                                                r'C_2\overset{\partial_2}{\to}'
                                                r'C_1\overset{\partial_1}{\to}'
                                                r'C_0\overset{\partial_0}{\to}0')
                               .next_to(diagram1).to_edge(UP)))
        self.play(ShowCreation(tex2 := Tex(r'C_3=0').next_to(tex_chain, direction=DOWN, aligned_edge=LEFT)))
        self.play(TransformFromCopy(VGroup(f_A, f_B),
                                    tex3 := Tex(r'C_2=\langle A,B\rangle').next_to(tex2, direction=DOWN,
                                                                                   aligned_edge=LEFT)))
        self.play(TransformFromCopy(VGroup(rect1, e_c),
                                    tex4 := Tex(r'C_1=\langle a,b,c\rangle').next_to(tex3, direction=DOWN,
                                                                                     aligned_edge=LEFT)))
        self.play(TransformFromCopy(VGroup(v0, v1, v2, v3),
                                    tex5 := Tex(r'C_0=\langle v\rangle').next_to(tex4, direction=DOWN,
                                                                                 aligned_edge=LEFT)))
        self.subtitle(r'The boundary homomorphisms map a simplex')
        self.wait()
        self.subtitle(r'to the alternative sum of opposite faces for each vertex.')
        tex6 = Tex(r'\partial_2A=', 'a', '-c', '+b').next_to(tex5, direction=DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(tex6[0]))
        self.play(TransformFromCopy(e_13, tex6[1]))
        self.play(TransformFromCopy(e_c, tex6[2]))
        self.play(TransformFromCopy(e_01, tex6[3]))
        tex7 = Tex(r'\partial_2B=', 'b', '-c', '+a').next_to(tex6, direction=DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(tex7[0]))
        self.play(TransformFromCopy(e_23, tex7[1]))
        self.play(TransformFromCopy(e_c, tex7[2]))
        self.play(TransformFromCopy(e_02, tex7[3]))
        self.subtitle(r'Since free abelian groups are also Z-modules,')
        self.wait()
        self.subtitle(r'the homomorphism can be written as a matrix as shown.')
        self.play(ReplacementTransform(VGroup(tex6, tex7),
                                       tex_d2 := Tex(
                                           r'\partial_2=\left[\begin{tabular}{c c}1&1\\1&1\\-1&-1\end{tabular}\right]')
                                       .next_to(tex5, direction=DOWN, buff=0.4, aligned_edge=LEFT)))
        tex_C_i = VGroup(tex2, tex3, tex4, tex5)
        self.play(tex_C_i.to_edge, RIGHT, tex_C_i.scale, 0.6, tex_d2.next_to, tex_chain, DOWN, 0.5, LEFT)
        self.subtitle(r'The kernel will be the null space of the matrix.')
        self.wait()
        self.subtitle(r'We can easily solve it out.')
        self.play(
            ShowCreation(tex_kerd2 := Tex(r'\left[\begin{tabular}{c c}$1$&$1$\\$1$&$1$\\$-1$&$-1$\end{tabular}\right]'
                                          r'\left[\begin{tabular}{c}$x$\\$y$\end{tabular}\right]'
                                          r'=\left[\begin{tabular}{c}$0$\\$0$\\$0$\end{tabular}\right]')
                         .next_to(tex_d2, direction=DOWN, aligned_edge=LEFT, buff=0.6)))
        self.wait()
        self.play(Transform(tex_kerd2, Tex(r'(x+y)\left[\begin{tabular}{c}$1$\\$1$\\$-1$\end{tabular}\right]'
                                           r'=\left[\begin{tabular}{c}$0$\\$0$\\$0$\end{tabular}\right]')
                            .next_to(tex_d2, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        self.wait()
        self.play(Transform(tex_kerd2, Tex(r'x+y=0')
                            .next_to(tex_d2, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        self.wait()
        self.play(Transform(tex_kerd2, Tex(r'\left[\begin{tabular}{c}$x$\\$y$\end{tabular}\right]'
                                           r'=x\left[\begin{tabular}{c}$1$\\$-1$\end{tabular}\right]')
                            .next_to(tex_d2, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        self.wait()
        self.play(Transform(tex_kerd2, Tex(r'\ker\partial_2=', r'\langle A-B\rangle')
                            .next_to(tex_d2, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        self.wait()
        self.subtitle(r'The image will be the column space of the matrix.')
        self.wait()
        self.subtitle(r'Obviously, this is a rank-1 matrix.')
        self.play(ShowCreation(tex_imd2 := Tex(r'\mathrm{im}\partial_2=', r'\langle a+b-c\rangle')
                               .next_to(tex_kerd2, direction=DOWN, aligned_edge=LEFT)))
        self.wait()
        self.play(Uncreate(tex_d2), VGroup(tex_kerd2, tex_imd2).next_to, tex_chain, DOWN, 0.5, LEFT)
        self.subtitle(r'Since all the vertexes are identical,')
        self.wait()
        self.subtitle(r'we know the 1st boundary map sends every edge to v-v=0.')
        self.play(ShowCreation(tex_kerd1 := Tex(r'\mathrm{ker}\partial_1=', r'\langle a,b,c\rangle')
                               .next_to(tex_imd2, direction=DOWN, aligned_edge=LEFT)))
        self.wait()
        self.play(ShowCreation(tex_imd1 := Tex(r'\mathrm{im}\partial_1=', r'0')
                               .next_to(tex_kerd1, direction=DOWN, aligned_edge=LEFT)))
        self.wait()
        self.subtitle(r'Since the codomain is zero, we know del0 is a zero map.')
        self.play(ShowCreation(tex_kerd0 := Tex(r'\mathrm{ker}\partial_0=', r'\langle v\rangle')
                               .next_to(tex_imd1, direction=DOWN, aligned_edge=LEFT)))
        self.wait()
        self.subtitle(r'Now we have all we need to compute the homology groups.')
        self.wait()
        self.subtitle('')
        tex_ker_im = VGroup(tex_kerd2, tex_kerd1, tex_kerd0, tex_imd2, tex_imd1)
        self.play(tex_ker_im.scale, 0.6, tex_ker_im.to_corner, DR)
        tex_h2 = Tex(r'H_2&=\ker\partial_2/\mathrm{im}\partial_3\\&=', r'\langle A-B\rangle', r'/', r'0')\
            .next_to(tex_chain, direction=DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(ShowCreation(tex_h2[0]))
        self.play(ShowCreation(tex_h2[2]))
        self.play(ReplacementTransform(tex_kerd2, tex_h2[1]))
        self.play(ShowCreation(tex_h2[3]))
        self.play(ReplacementTransform(tex_h2, Tex(r'H_2\cong\mathbb{Z}')
                            .next_to(tex_chain, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        tex_h1 = Tex(r'H_1&=\ker\partial_1/\mathrm{im}\partial_2\\&=',
                     r'\langle a,b,c\rangle', r'/', r'\langle a+b-c\rangle',
                     r'\\&=\langle a,b,a+b\rangle \\&=\langle a,b\rangle'
                     ).next_to(tex_h2, direction=DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(ShowCreation(tex_h1[0]))
        self.play(ShowCreation(tex_h1[2]))
        self.play(ReplacementTransform(tex_kerd1, tex_h1[1]))
        self.play(ReplacementTransform(tex_imd2, tex_h1[3]))
        self.play(ShowCreation(tex_h1[4]))
        self.play(ReplacementTransform(tex_h1, Tex(r'H_1\cong\mathbb{Z}\oplus\mathbb{Z}')
                            .next_to(tex_h2, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        tex_h0 = Tex(r'H_0&=\ker\partial_0/\mathrm{im}\partial_1\\&=',
                     r'\langle v\rangle', r'/', r'0'
                     ).next_to(tex_h1, direction=DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(ShowCreation(tex_h0[0]))
        self.play(ShowCreation(tex_h0[2]))
        self.play(ReplacementTransform(tex_kerd0, tex_h0[1]))
        self.play(ReplacementTransform(tex_imd1, tex_h0[3]))
        self.play(ReplacementTransform(tex_h0, Tex(r'H_0\cong\mathbb{Z}')
                                       .next_to(tex_h1, direction=DOWN, aligned_edge=LEFT, buff=0.5)))
        self.subtitle(r'All Done!')
        self.wait(5)

class QuickTest(PresentationScene):
    def construct(self) -> None:
        self.play(ShowCreation(tex_8 := Tex(r'\mathrm{im}\partial_2', r'=', r'\langle a+b-c\rangle')[0]))
        self.play(ShowCreation(tex_8 := Tex(r'\mathrm{im}\partial_2', r'=', r'\langle a+b-c\rangle')[2]))
