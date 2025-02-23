import sqlite3
import io
import datetime

#  Импорт компонентов PyQt6
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem, QFileDialog
import pyglet
#  Импорт template'ов
from templates import main_window_template, about_template, change_form, export_form, import_form
#  Импорт настроек из модуля
from settings_file import Settings
#  Импорт модуля работы с базой данных
from database_file import (add_event_to_db, change_event_in_db, delete_event_from_db, export_to_csv, delete_all_from_db,
                           import_from_csv)


# Создание основного класса приложения
class PyCalendar(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_window_template)
        uic.loadUi(f, self)
        #  Блок определения констант
        self.calendar_date_plus_three = None
        self.titles = None
        self.calendar_date = None
        self.pixmap = None
        self.change_form = None
        try:
            self.sound = pyglet.media.load('programfiles\\Sound_11086.mp3', streaming=False)

        except Exception as e:
            print(e)
            print('Не удалось загрузить файл звука')

        #  Определение дня в системе, и следующих двух после него
        date_table = datetime.date.today()
        self.today_date = f'{date_table.strftime("%d.%m.%Y")}'
        date_table_2days = date_table + datetime.timedelta(days=1)
        self.today_date_plus_two = f'{date_table_2days.strftime("%d.%m.%Y")}'
        date_table_3days = date_table + datetime.timedelta(days=2)
        self.today_date_plus_three = f'{date_table_3days.strftime("%d.%m.%Y")}'

        #  Создание QLabel с картинкой, которая появляется, когда в текущий день в системе есть событие с меткой
        #  "Важная дата"
        try:
            image_name_from_file = open('programfiles/name_of_the_image.txt', encoding='utf-8')
            self.ImageName = image_name_from_file.read()
            image_name_from_file.close()
            self.update_img()
            self.image_label.hide()

        except Exception as e:
            print(e)
            print('Не удалось найти файл')
            Settings().set_image_by_default()

        self.important_date_check()

        #  Вывод окон "О программе", "Настройки" и "Экспортировать". Вывод окна "Изменить событие" по нажатию кнопки
        #  "Изменить событие"
        self.about_form = AboutCalendar()
        self.action.triggered.connect(self.about_calendar_show)

        self.settings_form = Settings()
        self.action_2.triggered.connect(self.settings_show)

        self.export_window = CSVExport()
        self.action_CSV.triggered.connect(self.start_csv_export)

        self.import_window = CSVImport()
        self.action_CSV_2.triggered.connect(self.start_csv_import)

        self.change_event_button.clicked.connect(self.change_window_show)
        self.change_event_button.clicked.connect(self.important_date_check)

        #  Вывод в основном окне даты в системе и реагирование на изменение даты в календаре,
        #  вызов соответствующих функций. Реагирование на изменение даты в QDateTimeEdit
        self.calendar_current_day_label.setText(f'{datetime.date.today().strftime("%d.%m.%Y")}')
        self.calendar_date = f'{datetime.date.today().strftime("%d.%m.%Y")}'
        self.calendar_time = f'{self.select_dateTimeEdit.time().hour()}, {self.select_dateTimeEdit.time().minute()}'

        self.select_dateTimeEdit.timeChanged.connect(self.change_time)
        self.select_dateTimeEdit.setDate(self.calendar_days_select.selectedDate())

        self.calendar_days_select.clicked.connect(self.calendar_date_has_changed)
        self.calendar_days_select.clicked.connect(self.current_day_events_table)
        self.calendar_days_select.clicked.connect(self.events_feed_table)
        self.calendar_days_select.clicked.connect(self.important_date_check)

        #  Блок вызова функций для работы с БД
        self.add_event_button.clicked.connect(self.add_an_event)
        self.delete_event_button.clicked.connect(self.delete_an_event)

        #  Вывод информации на таблицы
        self.current_day_events_table()
        self.events_feed_table()
        self.feed_table.setSortingEnabled(True)

        #  Определить выбранный элемент таблицы событий за текущий день
        self.pressedRow = None
        self.pressedCol = None
        self.calendar_events.cellPressed.connect(self.update_cell)

        #  Создание таймера
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.check_time_for_ringtone)
        self.timer.start()

        #  Реакция на нажатие кнопки "Удалить ВСЕ события"
        self.delete_all_button.clicked.connect(self.clear_db)

        self.select_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    #  Методы обновления картинки и выбранной ячейки
    def update_img(self):
        self.pixmap = QPixmap(self.ImageName)
        self.image_label.setPixmap(self.pixmap)

    def update_cell(self, row, col):
        self.pressedRow = row
        self.pressedCol = col
        if col == 1:
            event_time = self.calendar_events.item(row, col + 2).text()
            self.calendar_time = event_time
            event_time = event_time.split(', ')
            event_time = QTime(int(event_time[0]), int(event_time[1]))
            self.select_dateTimeEdit.setTime(event_time)


    #  Вывод окон "О программе", "Настройки" и "Изменить событие", а также "Экспорт в CSV таблицу" и
    #  "Экспорт из CSV таблицы"
    def about_calendar_show(self):
        self.about_form.show()

    def settings_show(self):
        self.settings_form.show()

    def change_window_show(self):
        if self.pressedRow is not None and self.pressedCol is not None and self.pressedCol == 1:
            event_from_table = self.calendar_events.item(self.pressedRow, self.pressedCol).text()
            self.change_form = ChangeAnEvent(self.calendar_days_select.selectedDate(),
                                             event_from_table, self.select_dateTimeEdit.time(),
                                             self.calendar_date, self.calendar_time)
            self.change_form.show()
        else:
            return

    def start_csv_export(self):
        self.export_window.show()

    def start_csv_import(self):
        self.import_window.show()

    # Добавление, удаление событий. Взаимодействие с БД
    def add_an_event(self):
        date = self.calendar_date
        event = self.add_event_lineEdit.text()
        marker = self.marker_select.currentText()
        time = self.calendar_time
        add_event_to_db(date, event, marker, time)

        self.current_day_events_table()
        self.events_feed_table()
        self.important_date_check()

    def delete_an_event(self):
        if self.pressedRow is not None and self.pressedCol is not None:
            event = self.calendar_events.item(self.pressedRow, self.pressedCol).text()
            delete_event_from_db(event, self.calendar_date, self.calendar_time)
            self.current_day_events_table()
            self.events_feed_table()
        else:
            return

    def clear_db(self):
        delete_all_from_db()
        self.current_day_events_table()
        self.events_feed_table()

    #  Проверка, есть ли сегодня (системное время) важные даты. Если да – вывести картинку
    def important_date_check(self):
        try:
            with sqlite3.connect('database/data_base_file.db') as db:
                cursor = db.cursor()
                result = cursor.execute("SELECT * FROM events_table WHERE marker = ? AND date = ?",
                                        ('Важная дата', self.today_date)).fetchall()

                if result:
                    self.image_label.show()
                else:
                    self.image_label.hide()

        except Exception as e:
            print(e)
            print('Не удалось подключится к базе данных')

    #  Метод обновления данных в таблице событий за выбранный в виджете календаря день
    def current_day_events_table(self):
        try:
            with sqlite3.connect('database/data_base_file.db') as db:
                cursor = db.cursor()
                result = cursor.execute("SELECT * FROM events_table WHERE date=?",
                                        (self.calendar_date,)).fetchall()

                self.calendar_events.setRowCount(len(result))

                if not result:
                    self.calendar_events.setColumnCount(1)
                    self.calendar_events.setRowCount(1)
                    headers = ['События']
                    self.calendar_events.setHorizontalHeaderLabels(headers)
                    self.calendar_events.setItem(
                        0, 0, QTableWidgetItem('Не заданы'))
                    self.calendar_events.horizontalHeader().setStretchLastSection(True)
                    self.calendar_events.resizeColumnsToContents()
                    return

                self.calendar_events.setColumnCount(len(result[0]))
                headers = ['Дата', 'Событие', 'Метка', 'Время']
                self.calendar_events.setHorizontalHeaderLabels(headers)
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.calendar_events.setItem(i, j, QTableWidgetItem(str(val)))
                        self.calendar_events.resizeRowsToContents()

        except Exception as e:
            print(e)
            print('Не удалось подключится к базе данных')

    #  Метод обновления данных в таблице ленты событий за промежуток три дня, начиная со дня в системе
    def events_feed_table(self):
        try:
            with sqlite3.connect('database/data_base_file.db') as db:
                cursor = db.cursor()
                result = cursor.execute("SELECT * FROM events_table WHERE date = ? OR date = ? OR date = ?",
                                        (self.today_date, self.today_date_plus_two, self.today_date_plus_three)).fetchall()

                self.feed_table.setRowCount(len(result))

                if not result:
                    self.feed_table.setColumnCount(1)
                    self.feed_table.setRowCount(1)
                    headers = ['События']
                    self.feed_table.setHorizontalHeaderLabels(headers)
                    self.feed_table.setItem(
                        0, 0, QTableWidgetItem('Здесь пока что пусто.'))
                    self.feed_table.horizontalHeader().setStretchLastSection(True)
                    self.feed_table.resizeColumnsToContents()
                    return

                self.feed_table.setColumnCount(len(result[0]))
                headers = ['Дата', 'Событие', 'Метка', 'Время']
                self.feed_table.setHorizontalHeaderLabels(headers)
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.feed_table.setItem(i, j, QTableWidgetItem(str(val)))
                        self.feed_table.resizeRowsToContents()

        except Exception as e:
            print(e)
            print('Не удалось подключится к базе данных')

    #  Реакция календаря на выбор даты, посредством нажатия ЛКМ
    def calendar_date_has_changed(self, date):
        self.calendar_date = f'{date.toString("dd.MM.yyyy")}'
        self.select_dateTimeEdit.setDate(self.calendar_days_select.selectedDate())
        default = QTime(0, 0)
        self.select_dateTimeEdit.setTime(default)

        self.current_day_events_table()
        self.events_feed_table()
        self.important_date_check()

    #  Реакция на изменение времени в QDateTimeEdit
    def change_time(self):
        self.calendar_time = f'{self.select_dateTimeEdit.time().hour()}, {self.select_dateTimeEdit.time().minute()}'

    #  Каждые три секунды приложение смотрит, есть ли событие, со временем, соответствующим времени устройства
    def check_time_for_ringtone(self):
        try:
            with sqlite3.connect('database/data_base_file.db') as db:
                cursor = db.cursor()
                result = cursor.execute("SELECT time FROM events_table WHERE date = ?", (self.today_date,)).fetchall()

                current_time = datetime.datetime.today().strftime('%H:%M')
                for rows in result:
                    for column in rows:
                        hour_min = column.split(', ')
                        event_time = datetime.time(int(hour_min[0]), int(hour_min[1])).strftime('%H:%M')
                        if event_time == current_time:
                            self.sound.play()

                self.timer.start()

        except Exception as e:
            print(e)
            print('Не удалось подключится к базе данных')

#  Создание класса для окна "О программе"
class AboutCalendar(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(about_template)
        uic.loadUi(f, self)


#  Создание класса для окна "Изменить событие"
class ChangeAnEvent(QWidget):
    def __init__(self, date_from_calendar, event_from_calendar, time_from_calendar, calendar_date, calendar_time):
        super().__init__()
        f = io.StringIO(change_form)
        uic.loadUi(f, self)

        self.delta_date = None
        self.delta_event = None
        self.delta_marker = None
        self.delta_time = None
        self.calendar_class = PyCalendar()

        self.event = event_from_calendar

        self.change_event_lineEdit_w.setText(self.event)
        self.select_dateTimeEdit_w.setDate(date_from_calendar)
        self.select_dateTimeEdit_w.setTime(time_from_calendar)

        self.change_event_button_w.clicked.connect(self.load_data_into_db)

    def update_from_calendar(self):
        self.calendar_class.current_day_events_table()

    def load_data_into_db(self):
        self.delta_event = self.change_event_lineEdit_w.text()
        self.delta_marker = self.marker_select_w.currentText()
        self.delta_date = f'{self.select_dateTimeEdit_w.date().toString("dd.MM.yyyy")}'
        self.delta_time = f'{self.select_dateTimeEdit_w.time().hour()}, {self.select_dateTimeEdit_w.time().minute()}'

        change_event_in_db(self.event, self.delta_date, self.delta_event, self.delta_marker, self.delta_time)
        self.update_from_calendar()
        self.hide()


# Создание класса для окна "Экспортировать в CSV"
class CSVExport(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(export_form)
        uic.loadUi(f, self)
        self.directory = None

        self.directory_select_button.clicked.connect(self.directory_select)
        self.export_button.clicked.connect(self.export_to_file)

    def directory_select(self):
        self.directory = QFileDialog.getExistingDirectory(self)

    def export_to_file(self):
        if self.directory != '' and self.directory is not None:
            export_to_csv(self.directory)
            self.hide()
        else:
            return


# Создание класса для окна "Импортировать из CSV"
class CSVImport(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(import_form)
        uic.loadUi(f, self)
        self.file_name = None

        self.directory_select_button.clicked.connect(self.directory_select)
        self.import_button.clicked.connect(self.import_from_file)

    def directory_select(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать таблицу', '', 'Таблица (*.csv)')[0]

    def import_from_file(self):
        if self.file_name != '' and self.file_name is not None:
            import_from_csv(self.file_name)
            self.hide()
        else:
            return
