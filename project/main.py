import sys

from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QWidget, QDialog, QColorDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from Qdraw_main_design import Ui_MainWindow
from Create_Window import Ui_Dialog
from PyQt5 import Qt
from PyQt5.Qt import QRect
from create_widget import wdg_create_list
from instruments import *


class User:
    def __init__(self):
        self.choose_instrument = None
        self.choose_color = Qt.QColor(0, 0, 0)
        self.choose_extra_color = Qt.QColor(255, 255, 255)
        self.coords = 0, 0
        self.old_coords = 0, 0


class Qdrow(QWidget, Ui_MainWindow):
    """
        По сути, вся основная работа проводится здесь.
        Главный скриптер приложения
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Qdrow 0.9")
        self.setWindowIcon(QIcon("ico2.jpg"))

        self.Flag = False
        self.pos_checked = False

        # начальная картинка
        image = Image.new("RGB", (1280, 720), (255, 255, 255))
        image.save("bufer.jpg")
        self.pixmap = QPixmap("bufer.jpg")
        self.picture.setPixmap(self.pixmap)
        self.scrollArea.setWidget(self.picture)

        # Создание юзера
        self.User = User()
        self.pos_old = (0, 0)

        #  настройки
        self.text_settings_color = QColor(255, 255, 255)
        self.text_settings_font = "MS Shell Dlg 2"

        # настройка для скролов
        self.scroll_x_bar = 0
        self.scroll_y_bar = 0

        # Создание инструментов
        self.Eraser = Eraser()
        self.Pen = Pen()
        self.Fill = Fill()
        self.Pencil = Pencil()
        self.Gradient = Gradient()
        self.Line = Line()
        self.Highlight = Rectangle()
        self.Text = Text()
        self.Pipette = Pipette()

        # Прикрепляем картиночки к каждой кнопке
        self.btn_pencil.setStyleSheet("image : url(pencil.png)")
        self.btn_pen.setStyleSheet("image : url(pen.png)")
        self.btn_eraser.setStyleSheet("image : url(eraser.png)")
        self.btn_line.setStyleSheet("image : url(line.png)")
        self.btn_highklight.setStyleSheet("image : url(highlight)")
        self.btn_gradient.setStyleSheet("image: url(gradient.png)")
        self.btn_fill.setStyleSheet("image: url(fill.png)")
        self.btn_text.setStyleSheet("image: url(text.png)")
        self.btn_pipette.setStyleSheet("image:url(pipette.png)")
        self.btn_rotate.setStyleSheet("image:url(rotate.png)")

        # изначальный цвет палитры
        self.btn_main_color.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btn_extra_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_amenotejikara.setStyleSheet("image : url(zamena.png)")

        self.make_all_Engilsh()

        self.hide_all_wdg()

        self.set_value_for_sliders()

        self.wdg_pencil.show()

        self.Init_UI()

    def Init_UI(self):

        # кнопки цвета
        self.btn_main_color.clicked.connect(self.choose_color)
        self.btn_extra_color.clicked.connect(self.choose_color)
        self.btn_amenotejikara.clicked.connect(self.replace_color)

        # инструменты
        self.btn_file.clicked.connect(self.show_features)
        self.btn_settings.clicked.connect(self.show_features)
        self.btn_eraser.clicked.connect(self.show_features)
        self.btn_pen.clicked.connect(self.show_features)
        self.btn_fill.clicked.connect(self.show_features)
        self.btn_pencil.clicked.connect(self.show_features)
        self.btn_gradient.clicked.connect(self.show_features)
        self.btn_line.clicked.connect(self.show_features)
        self.btn_highklight.clicked.connect(self.show_features)
        self.btn_text.clicked.connect(self.show_features)
        self.btn_rotate.clicked.connect(self.rotate_picture)
        self.btn_pipette.clicked.connect(self.show_features)
        self.btn_choose_color_title.clicked.connect(self.choose_color)
        self.btn_choose_color_text.clicked.connect(self.choose_color)

        # освновные кнопки
        self.btn_close_file.clicked.connect(self.show_features)
        self.btn_save_file.clicked.connect(self.save_file)
        self.btn_open_file.clicked.connect(self.open_file)

        self.btn_close_setting.clicked.connect(self.hide_all_wdg)

        self.btn_preview.clicked.connect(self.preview)

        self.slide_size_text.valueChanged[int].connect(self.change_value_slider)
        self.slide_size_pencil.valueChanged[int].connect(self.change_value_slider)
        self.slide_size_eraser.valueChanged[int].connect(self.change_value_slider)

        self.scrollArea.horizontalScrollBar().valueChanged[int].connect(self.change_value_slider)
        self.scrollArea.verticalScrollBar().valueChanged[int].connect(self.change_value_slider)

        self.font_box_text.activated[str].connect(self.edit_font)
        self.font_text_setting.activated[str].connect(self.edit_font_setting)

        self.choose_horisontal.toggled.connect(self.change_rotation)
        self.choose_vertical.toggled.connect(self.change_rotation)
        self.choose_english.toggled.connect(self.change_language)
        self.choose_russian.toggled.connect(self.change_language)

    def change_rotation(self):
        choose = self.sender()
        if choose is self.choose_horisontal:
            self.Gradient.rotation = "Horizontal"
        if choose is self.choose_vertical:
            self.Gradient.rotation = "Vertical"

    def change_language(self):
        choose = self.sender()
        if choose is self.choose_english:
            self.make_all_Engilsh()
        if choose is self.choose_russian:
            self.make_all_Russian()

    def edit_font_setting(self, font):
        font = QFont(font, 12)
        self.btn_file.setFont(font)
        self.btn_new_file.setFont(font)
        self.btn_save_file.setFont(font)
        self.btn_new_file.setFont(font)
        self.btn_close_file.setFont(font)
        self.btn_settings.setFont(font)
        self.btn_preview.setFont(font)
        self.btn_reference.setFont(font)
        self.label_size_text.setFont(font)
        self.label_font_text.setFont(font)
        self.label_size_eraser.setFont(font)
        self.label_text_color.setFont(font)
        self.label_size_pencil.setFont(font)
        self.label_text_setting.setFont(font)
        self.label_choose_lang.setFont(font)
        self.label_choose_title.setFont(font)
        self.btn_close_setting.setFont(font)
        self.label_font_text_setting.setFont(font)
        self.choose_english.setFont(font)
        self.choose_russian.setFont(font)
        self.choose_vertical.setFont(font)
        self.choose_horisontal.setFont(font)
        self.groop_choose_lang.setFont(font)
        self.gr_direction_gradient.setFont(font)
        self.label_text_text.setFont(font)

    def edit_font(self, font):
        self.Text.font = font

    def preview(self):
        self.pixmap.save("bufer.jpg")
        prew = Image.open("bufer.jpg")
        prew.show()

    def change_color_text(self, color):
        """Не работает"""
        edit_color = "color{}: ".format(color.name())
        self.btn_new_file.setStyleSheet("color{}: ".format(color.name()))
        self.label_choose_title.setStyleSheet(edit_color)
        self.label_choose_lang.setStyleSheet(edit_color)
        """
        self.btn_save_file.setText("Save")
        self.btn_new_file.setText("New")
        self.btn_close_file.setText("Close")
        self.btn_settings.setText("Settings")
        self.btn_preview.setText("Prewiew")
        self.btn_reference.setText("References")
        self.label_size_text.setText("Size")
        self.label_font_text.setText("Font")
        self.label_size_eraser.setText("Size")
        self.label_tex_font.setText("Font")
        self.label_text_color.setText("Color")
        self.label_size_pencil.setText("Size")
        self.label_text_setting.setText("Text")
        
        
        """

    def choose_color(self):
        color = QColorDialog.getColor()
        self.sender().setStyleSheet("background-color: {}".format(color.name()))
        if self.sender() == self.btn_main_color:
            self.User.choose_color = color
        elif self.sender() == self.btn_extra_color:
            self.User.choose_extra_color = color
        elif self.sender() == self.btn_choose_color_text:
            self.change_color_text(color)
        elif self.sender() == self.btn_choose_color_title:
            self.setStyleSheet("background-color: {}".format(color.name()))

    def replace_color(self):
        self.User.choose_extra_color, self.User.choose_color = self.User.choose_color, self.User.choose_extra_color
        self.btn_extra_color.setStyleSheet("background-color: {}".format(self.User.choose_extra_color.name()))
        self.btn_main_color.setStyleSheet("background-color: {}".format(self.User.choose_color.name()))

    def open_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
        if fname == "":
            return
        self.pixmap = QPixmap(fname)
        self.picture.setPixmap(self.pixmap)
        self.scrollArea.setWidget(self.picture)
        self.scroll_x_bar = 0
        self.scroll_y_bar = 0

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "File PNG(*.png);;File JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file_path == "":
            return
        self.pixmap.save(file_path)

    def hide_all_wdg(self):
        self.User.choose_instrument = None
        self.wdg_file.hide()
        self.wdg_settings.hide()
        self.wdg_line.hide()
        self.wdg_text.hide()
        self.wdg_gradient.hide()
        self.wdg_eraser.hide()
        self.wdg_highklight.hide()
        self.wdg_pencil.hide()

    def dialog_create(self):
        parameters = wdg_create_list()

        parameters.show()

        parameters.exec()

    def make_all_Engilsh(self):
        self.btn_file.setText("File")
        self.btn_new_file.setText("Open")
        self.btn_save_file.setText("Save")
        self.btn_new_file.setText("New")
        self.btn_close_file.setText("Close")
        self.btn_settings.setText("Settings")
        self.btn_preview.setText("Prewiew")
        self.btn_reference.setText("References")
        self.label_size_text.setText("Size")
        self.label_font_text.setText("Font")
        self.label_text_text.setText("Text")
        self.label_size_eraser.setText("Size")
        self.label_text_color.setText("Color")
        self.label_size_pencil.setText("Size")
        self.label_text_setting.setText("Text")
        self.label_choose_lang.setText("Language:")
        self.label_choose_title.setText("Color Title:")
        self.btn_close_setting.setText("Close")
        self.label_font_text_setting.setText("Font")
        self.choose_english.setText("English")
        self.choose_russian.setText("Russian")
        self.choose_vertical.setText("Vertical")
        self.choose_horisontal.setText("Horizontal")
        self.gr_direction_gradient.setTitle("Direction")

    def make_all_Russian(self):
        self.btn_file.setText("Файл")
        self.btn_new_file.setText("Открыть")
        self.btn_save_file.setText("Сохранить")
        self.btn_new_file.setText("Новый файл")
        self.btn_close_file.setText("Закрыть")
        self.btn_settings.setText("Настройки")
        self.btn_preview.setText("Предпросмотр")
        self.btn_reference.setText("Справка")
        self.label_size_text.setText("Размер")
        self.label_font_text.setText("Шрифт")
        self.label_size_eraser.setText("Размер")
        self.label_text_color.setText("Цвет")
        self.label_size_pencil.setText("Размер")
        self.label_text_setting.setText("Текст")
        self.label_choose_lang.setText("Язык:")
        self.label_choose_title.setText("Цветовая тема:")
        self.label_font_text_setting.setText("Шрифт")
        self.label_text_text.setText("Текст")
        self.btn_close_setting.setText("Закрыть")
        self.choose_english.setText("Английский")
        self.choose_russian.setText("Русский")
        self.choose_vertical.setText("Вертикально")
        self.choose_horisontal.setText("Горизонтально")
        self.gr_direction_gradient.setTitle("Направление")

    def set_value_for_sliders(self):
        """ установливает значения для крутилок инструментов"""
        # карандаш размер
        self.slide_size_pencil.setMinimum(1)
        self.slide_size_pencil.setMaximum(50)
        self.slide_size_pencil.setValue(5)
        # текст размер
        self.slide_size_text.setMinimum(2)
        self.slide_size_text.setMaximum(70)
        self.slide_size_text.setValue(5)
        # ластик размер
        self.slide_size_eraser.setMinimum(1)
        self.slide_size_eraser.setMaximum(100)
        self.slide_size_eraser.setValue(10)

    def change_value_slider(self, value):
        send = self.sender()
        if send == self.slide_size_text:
            self.Text.size = value
        if send == self.slide_size_eraser:
            self.Eraser.size = value
        if send == self.slide_size_pencil:
            self.Pencil.size = value
        if send == self.scrollArea.horizontalScrollBar():
            self.scroll_x_bar = value
        if send == self.scrollArea.verticalScrollBar():
            self.scroll_y_bar = value

    def show_features(self):
        tool = self.sender()
        self.hide_all_wdg()
        if tool == self.btn_file:
            self.wdg_file.show()
        if tool == self.btn_settings:
            self.wdg_settings.show()
        if tool == self.btn_text:
            self.wdg_text.show()
            self.User.choose_instrument = self.Text
        if tool == self.btn_eraser:
            self.wdg_eraser.show()
            self.User.choose_instrument = self.Eraser
        if tool == self.btn_highklight:
            self.wdg_highklight.show()
            self.User.choose_instrument = self.Highlight
        if tool == self.btn_line:
            self.User.choose_instrument = self.Line
        if tool == self.btn_pencil:
            self.wdg_pencil.show()
            self.User.choose_instrument = self.Pencil
        if tool == self.btn_pen:
            self.User.choose_instrument = self.Pen
        if tool == self.btn_fill:
            self.User.choose_instrument = self.Fill
        if tool == self.btn_gradient:
            self.User.choose_instrument = self.Gradient
            self.wdg_gradient.show()
        if tool == self.btn_pipette:
            self.User.choose_instrument = self.Pipette

    def mouseMoveEvent(self, event):
        def calculate_pos():
            return event.pos().x() - 110 + self.scroll_x_bar, \
                   event.pos().y() - 70 + self.scroll_y_bar

        if self.User.choose_instrument in (self.Pen, self.Eraser,
                                           self.Pencil):
            self.pos_old = self.User.coords
            self.User.coords = calculate_pos()
            self.Flag = True

        self.picture.setPixmap(self.pixmap)

    def mousePressEvent(self, event):
        def calculate_pos():
            return event.pos().x() - 110 + self.scroll_x_bar, \
                   event.pos().y() - 70 + self.scroll_y_bar

        tool = self.User.choose_instrument
        if tool:
            self.Flag = True

        if tool in (self.Pen, self.Eraser, self.Pencil):
            self.User.coords = calculate_pos()
            self.pos_checked = True

        elif tool is self.Line:
            if self.Line.first_pos_checked:
                self.Line.second_pos = calculate_pos()
                self.Line.second_pos_checked = True
            else:
                self.Line.first_pos = calculate_pos()
                self.Line.first_pos_checked = True
        elif tool is self.Highlight:
            if self.Highlight.first_pos_checked:
                self.Highlight.pos_second = calculate_pos()
                self.Highlight.second_pos_checked = True
            else:
                self.Highlight.pos_first = calculate_pos()
                self.Highlight.first_pos_checked = True
        elif tool is self.Pipette:
            self.Pipette.pos = calculate_pos()
        elif tool is self.Gradient:
            if self.Gradient.first_pos_checked:
                self.Gradient.second_pos = calculate_pos()
                self.Gradient.second_pos_checked = True
            else:
                self.Gradient.first_pos = calculate_pos()
                self.Gradient.first_pos_checked = True
        if tool is self.Text:
            self.Flag = True
            self.Text.pos = self.Text.first_pos = calculate_pos()

    def paintEvent(self, event) -> None:
        if self.Flag:
            tool = self.User.choose_instrument
            qp = QPainter()
            qp.begin(self.pixmap)
            if tool is self.Pen:
                self.drow_pixel(qp)
            if tool is self.Eraser:
                self.erasing(qp)
            if tool is self.Line:
                if self.Line.second_pos_checked and self.Line.first_pos_checked:
                    self.drow_line(qp)
                    self.Line.second_pos_checked = False
                    self.Line.first_pos_checked = False
                elif self.Line.first_pos_checked:
                    self.drow_first_dot(qp)
            if tool is self.Fill:
                self.fill(qp)
            if tool is self.Highlight:
                if self.Highlight.second_pos_checked:
                    self.frame(qp)
                    self.Highlight.first_pos_checked = False
                    self.Highlight.second_pos_checked = False
            if tool is self.Pipette:
                self.pippete()
            if tool is self.Pencil:
                self.draw_pencil(qp)
            if tool is self.Gradient:
                if self.Gradient.second_pos_checked:
                    self.gradient(qp)
                    self.Gradient.first_pos_checked = False
                    self.Gradient.second_pos_checked = False
                if self.Gradient.first_pos_checked:
                    self.drow_first_dot(qp)
            if tool is self.Text:
                self.text_draw(qp)

            qp.end()
            self.Flag = False
            self.pos_checked = False

    def drow_line(self, qp):
        qp.setPen(self.User.choose_color)
        x_old, y_old = self.Line.first_pos[0], self.Line.first_pos[1]
        x, y = self.Line.second_pos[0], self.Line.second_pos[1]
        qp.drawLine(x_old, y_old, x, y)

    def drow_first_dot(self, qp):
        qp.setPen(self.User.choose_color)
        if self.User.choose_instrument is self.Line:
            x, y = self.Line.first_pos
        if self.User.choose_instrument is self.Gradient:
            x, y = self.Gradient.first_pos
        qp.drawPoint(x, y)

    def drow_pixel(self, qp):
        qp.setPen(self.User.choose_color)
        x_old, y_old = self.pos_old
        x, y = self.User.coords
        if self.pos_checked:
            qp.drawPoint(x, y)
        else:
            qp.drawLine(x_old, y_old, x, y)

    def erasing(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        x, y = self.User.coords
        width = self.Eraser.size
        qp.fillRect(QRect(x, y, width, width), qp.brush())

    def draw_pencil(self, qp):
        qp.setBrush(self.User.choose_color)
        x, y = self.User.coords
        width = self.Pencil.size
        qp.fillRect(QRect(x, y, width, width), qp.brush())

    def fill(self, qp):
        x, y = self.pixmap.width(), self.pixmap.height()
        qp.setBrush(self.User.choose_color)
        qp.fillRect(QRect(0, 0, x, y), qp.brush())

    def gradient(self, qp):
        x1, y1 = self.Gradient.first_pos
        x2, y2 = self.Gradient.second_pos
        r1, g1, b1, a1 = self.User.choose_color.getRgb()
        r2, g2, b2, a2 = self.User.choose_extra_color.getRgb()
        delta_r = r1 - r2
        delta_g = g1 - g2
        delta_b = b1 - b2
        r_new, g_new, b_new = float(r2), float(g2), float(b2)
        step = 1

        if self.Gradient.rotation == "Vertical":
            delta_y = abs(y2 - y1)
            step_r = round(delta_r / delta_y, 2)
            step_g = round(delta_g / delta_y, 2)
            step_b = round(delta_b / delta_y, 2)
            if y1 > y2:
                step = -1
            for line_y in range(y1, y2, step):
                r_new += step_r
                g_new += step_g
                b_new += step_b
                qp.setPen(QColor(int(r_new), int(g_new), int(b_new)))
                qp.drawLine(x1, line_y, x2, line_y)

        else:
            delta_x = abs(x2 - x1)
            step_r = round(delta_r / delta_x, 2)
            step_g = round(delta_g / delta_x, 2)
            step_b = round(delta_b / delta_x, 2)
            if x1 > x2:
                step = -1
            for line_x in range(x1, x2, step):
                r_new += step_r
                g_new += step_g
                b_new += step_b
                qp.setPen(QColor(int(r_new), int(g_new), int(b_new)))
                qp.drawLine(line_x, y1, line_x, y2)

    def frame(self, qp):
        qp.setBrush(self.User.choose_color)
        x, y = self.Highlight.pos_first
        x_2, y_2 = self.Highlight.pos_second
        if x > x_2:
            x, x_2 = x_2, x
        if y_2 < y:
            y, y_2 = y_2, y
        qp.drawRect(x, y, abs(x - x_2), abs(y - y_2))

    def pippete(self):
        self.pixmap.save("bufer.jpg")
        req = Image.open("bufer.jpg")
        pixels = req.load()
        x, y = self.Pipette.pos
        r, g, b = pixels[x, y]
        color = QColor(r, g, b)
        self.User.choose_color = color
        self.btn_main_color.setStyleSheet("background-color: {}".format(color.name()))
        req.save("bufer.jpg")

    def text_draw(self, qp):
        x, y = self.Text.pos
        qp.setPen(self.User.choose_color)
        qp.setFont(QFont(self.Text.font, self.Text.size))
        qp.drawText(x, y, self.lineEdit_text_text.text())

    def rotate_picture(self):
        self.pixmap.save("bufer.jpg")
        image = Image.open("bufer.jpg")
        image = image.transpose(Image.ROTATE_270)
        image.save("bufer.jpg")
        self.pixmap = QPixmap("bufer.jpg")
        self.picture.setPixmap(self.pixmap)
        self.scrollArea.setWidget(self.picture)
        self.scroll_x_bar = 0
        self.scroll_y_bar = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Work = Qdrow()
    Work.show()
    sys.exit(app.exec())
