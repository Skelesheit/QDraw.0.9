class ToolParent:
    """
        Главный родитель всех классов инструментов
        Абстрактный класс
    """


class Figure(ToolParent):
    """
        Создатель фигур, по сути делает обводку фигуры
    """

    def __init__(self):
        super().__init__()


class Pencil(ToolParent):
    """
        Класс карандаш, тупо рисует карандашом
        в несколько пикселей, имеет толщину, цвет ...
        но без размытия как кисть

    """

    def __init__(self):
        super().__init__()
        self.size = 4


class Pen(ToolParent):
    """
        Класс ручка позволяет рисовать попиксельно
    """

    def __init__(self):
        super(Pen, self).__init__()


class Gradient(ToolParent):
    def __init__(self):
        self.first_pos = 0, 0
        self.second_pos = 0, 0
        self.first_pos_checked = False
        self.second_pos_checked = False
        self.rotation = "Horizontal"


class Eraser(ToolParent):
    """
        обычный ластик без размытием и с ним и без
        Возвращает к исходному цвету, в котором
        была картинка при создании
    """

    def __init__(self):
        self.size = 10


class Fill(ToolParent):
    """
        Заполняет все пространство каким-то цветом
        Если есть обводка, то рисует до обводки
        если в замкнутой фигуре, то нарисуется
        только внутри
    """

    def __init__(self):
        pass


class Line(ToolParent):
    """
        Создаёт линию из двух точек.
        Тупо рисует линию. Можно менять Цвет!
        ...
    """

    def __init__(self):
        super().__init__()
        self.first_pos = (0, 0)
        self.first_pos_checked = False
        self.second_pos = (0, 0)
        self.second_pos_checked = False


class Pipette(ToolParent):
    """
        крадет цвет пикселя
    """

    def __init__(self):
        self.pos = 0, 0


class Rectangle(ToolParent):
    """
        Рисует прямоугольник, прикольная вещь, правда?
    """

    def __init__(self):
        self.pos_first = 0, 0
        self.first_pos_checked = False
        self.pos_second = 0, 0
        self.second_pos_checked = False


class Text(ToolParent):
    """
            Создаёт текст в нужном месте
            Будут доступны шрифты и кучу всяких
            свойств для работы с текстом
            в картинке...
    """

    def __init__(self):
        self.size = 2
        self.font = "MS Shell Dlg 2"
        self.pos = 0, 0

