# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R = int(float(line.split()[1].lower()))
    """Радиус звезды"""
    star.color = line.split()[2].lower()
    """Цвет звезды"""
    star.m = float(line.split()[3].lower())
    """Масса звезды"""
    star.x = float(line.split()[4].lower())
    """Координата по оси **x**"""
    star.y = float(line.split()[5].lower())
    """Скорость по оси **y**"""
    star.vx = float(line.split()[6].lower())
    """Скорость по оси **x**"""
    star.vy = float(line.split()[7].lower())
    """Скорость по оси **y**"""

    return star.R, star.color, star.m, star.x, star.y, star.vx, star.vy


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = int(float(line.split()[1].lower()))
    """Радиус планеты"""
    planet.color = line.split()[2].lower()
    """Цвет планеты"""
    planet.m = float(line.split()[3].lower())
    """Масса планеты"""
    planet.x = float(line.split()[4].lower())
    """Координата по оси **x**"""
    planet.y = float(line.split()[5].lower())
    """Скорость по оси **y**"""
    planet.vx = float(line.split()[6].lower())
    """Скорость по оси **x**"""
    planet.vy = float(line.split()[7].lower())
    """Скорость по оси **y**"""

    return planet.R, planet.color, planet.m, planet.x, planet.y, planet.vx, planet.vy


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(
                obj.type + ' ' + str(obj.R) + ' ' + obj.color + ' ' + "%.3e" % obj.m + ' ' + "%.3e" % obj.x + ' ' +
                "%.3e" % obj.y + ' ' + "%.3e" % obj.vx + ' ' + "%.3e" % obj.vy + '\n\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
