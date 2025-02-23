import io

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog
#  Импорт template окна "Настройки"
from templates import settings_form


#  Класс настроек вывода изображения
class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.filename = None
        f = io.StringIO(settings_form)
        uic.loadUi(f, self)

        self.select.clicked.connect(self.change_the_image)
        self.set_default.clicked.connect(self.set_image_by_default)

    #  Установка собственной директории с изображением
    def change_the_image(self):
        self.filename = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]

        try:
            image_name_from_file = open('programfiles/name_of_the_image.txt', mode='w')
            image_name_from_file.write(self.filename)

        except Exception as e:
            print(e)
            print('Не удалось подключится к файлу')

        else:
            image_name_from_file.close()

        self.hide()

    #  Установка директории с изображением по умолчанию
    def set_image_by_default(self):
        try:
            image_name_from_file = open('programfiles/name_of_the_image.txt', mode='w')
            image_name_from_file.write('programfiles/happy_image.jpg')

        except Exception as e:
            print(e)
            print('Не удалось подключится к файлу')

        else:
            image_name_from_file.close()

        self.hide()
