# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from scipy.special import eval_legendre
import numpy as np
import matplotlib.pyplot as plt
from eval import evaluate
from solver import solve, smart_solve
from ipywidgets import Text, IntSlider, FloatText, TwoByTwoLayout, Layout, Output


# %%
expression_text = Text('cos(x)', description='Выражение: ',
                       layout=Layout(width='auto', height='auto'))
degree_slider = IntSlider(2, 1, 100, 1, description="Степень: ", layout=Layout(
    width='auto', height='auto'))
left_limit = FloatText(-1, description='Начало:',
                       layout=Layout(width='auto', height='auto'))
right_limit = FloatText(value=1, description='Конец:',
                        layout=Layout(width='auto', height='auto'))


# %%
TwoByTwoLayout(top_left=expression_text,
               top_right=degree_slider,
               bottom_left=left_limit,
               bottom_right=right_limit)


# %%
o = Output()
o


# %%
def recalculate(_=None):
    o.clear_output()
    with o:
        try:
            x = np.linspace(left_limit.value, right_limit.value, int(
                (np.abs(left_limit.value - right_limit.value) + 1) * 1000))
            y = [evaluate(expression_text.value, {'x': _x}) for _x in x]
            def get_y(x): return evaluate(expression_text.value, {'x': x})
            yp, cs = solve(x, y, degree_slider.value)
            yp_smart = smart_solve(
                (left_limit.value, right_limit.value), get_y, degree_slider.value)
            print(cs)
            plt.plot(x, y)
            plt.plot(x, yp)
            plt.plot(x, yp_smart)
            plt.show()
        except AttributeError:
            print('Не удалось распознать выражение')


recalculate()


# %%
expression_text.observe(recalculate, names='value')
degree_slider.observe(recalculate, names='value')
left_limit.observe(recalculate, names='value')
right_limit.observe(recalculate, names='value')


# %%


# %%
eval_legendre(1, 3)


# %%
