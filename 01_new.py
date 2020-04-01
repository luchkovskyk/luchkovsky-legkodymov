# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1000, 1000)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_figure(start_point, side_count, angle, length):
    current_point = start_point
    angle_step = 360 / side_count
    step = angle_step

    for side in range(side_count - 1):  # TODO Используйте range для "расчёта текущего угла, укажите минимальный,
        # максимальнй углы и шаг. Также учтите в максимальном угле как угол проворота фигуры, так и то, что нам надо
        # рисовать на одну грань меньше
        current_point = sd.vector(current_point, angle + step, length, sd.COLOR_YELLOW, 1)
        step += angle_step

    sd.line(current_point, start_point)


def draw_triangle(start_point, angle=0, length=100):
    side = 3
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_square(start_point, angle=0, length=100):
    side = 4
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_pentagon(start_point, angle=0, length=100):
    side = 5
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_hexagon(start_point, angle=0, length=100):
    side = 6
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


point = sd.get_point(600, 600)
draw_triangle(start_point=point, angle=20, length=100)

point = sd.get_point(600, 600)
draw_square(start_point=point, angle=20, length=100)

point = sd.get_point(600, 600)
draw_pentagon(start_point=point, angle=20, length=100)

point = sd.get_point(600, 600)
draw_hexagon(start_point=point, angle=20, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()