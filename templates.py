main_window_template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1280</width>
    <height>690</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Календарщик</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QFormLayout" name="formLayout">
    <property name="fieldGrowthPolicy">
     <enum>QFormLayout::FieldsStayAtSizeHint</enum>
    </property>
    <property name="rowWrapPolicy">
     <enum>QFormLayout::DontWrapRows</enum>
    </property>
    <property name="labelAlignment">
     <set>Qt::AlignHCenter|Qt::AlignTop</set>
    </property>
    <property name="formAlignment">
     <set>Qt::AlignHCenter|Qt::AlignTop</set>
    </property>
    <property name="horizontalSpacing">
     <number>6</number>
    </property>
    <property name="leftMargin">
     <number>12</number>
    </property>
    <property name="topMargin">
     <number>12</number>
    </property>
    <property name="rightMargin">
     <number>12</number>
    </property>
    <item row="0" column="0" colspan="2">
     <layout class="QHBoxLayout" name="calendar_display" stretch="1,60,60">
      <property name="spacing">
       <number>20</number>
      </property>
      <item>
       <widget class="QCalendarWidget" name="calendar_days_select"/>
      </item>
      <item>
       <layout class="QVBoxLayout" name="calendar_current_day">
        <item>
         <widget class="QLabel" name="label">
          <property name="font">
           <font>
            <family>Verdana</family>
            <pointsize>12</pointsize>
            <weight>75</weight>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>События в выбранный день:</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QTableWidget" name="calendar_events">
          <property name="font">
           <font>
            <pointsize>8</pointsize>
           </font>
          </property>
          <property name="verticalScrollMode">
           <enum>QAbstractItemView::ScrollPerPixel</enum>
          </property>
          <property name="horizontalScrollMode">
           <enum>QAbstractItemView::ScrollPerPixel</enum>
          </property>
          <property name="sortingEnabled">
           <bool>true</bool>
          </property>
          <attribute name="horizontalHeaderStretchLastSection">
           <bool>true</bool>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="delete_all_button">
          <property name="text">
           <string>Удалить ВСЕ события</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="calendar_feed" stretch="0,0">
        <property name="leftMargin">
         <number>0</number>
        </property>
        <item>
         <widget class="QLabel" name="feed_label">
          <property name="font">
           <font>
            <family>Verdana</family>
            <pointsize>12</pointsize>
            <weight>75</weight>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>События в ближайшие 3 дня:</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QTableWidget" name="feed_table">
          <property name="font">
           <font>
            <pointsize>8</pointsize>
           </font>
          </property>
          <property name="verticalScrollMode">
           <enum>QAbstractItemView::ScrollPerPixel</enum>
          </property>
          <property name="horizontalScrollMode">
           <enum>QAbstractItemView::ScrollPerPixel</enum>
          </property>
          <property name="sortingEnabled">
           <bool>true</bool>
          </property>
          <attribute name="horizontalHeaderStretchLastSection">
           <bool>true</bool>
          </attribute>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item row="1" column="0">
     <spacer name="verticalSpacer">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>20</width>
        <height>50</height>
       </size>
      </property>
     </spacer>
    </item>
    <item row="2" column="0" colspan="2">
     <layout class="QHBoxLayout" name="calendar_control" stretch="50,20">
      <property name="spacing">
       <number>40</number>
      </property>
      <property name="sizeConstraint">
       <enum>QLayout::SetDefaultConstraint</enum>
      </property>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_2" stretch="20,25,0,0,10">
        <property name="spacing">
         <number>15</number>
        </property>
        <item>
         <widget class="QLabel" name="add_event_label">
          <property name="font">
           <font>
            <family>Verdana</family>
            <pointsize>14</pointsize>
            <weight>75</weight>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>Добавить событие</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="add_event_lineEdit"/>
        </item>
        <item>
         <widget class="QComboBox" name="marker_select">
          <property name="layoutDirection">
           <enum>Qt::LeftToRight</enum>
          </property>
          <property name="currentText">
           <string>Цель/задача</string>
          </property>
          <item>
           <property name="text">
            <string>Цель/задача</string>
           </property>
          </item>
          <item>
           <property name="text">
            <string>Важная дата</string>
           </property>
          </item>
         </widget>
        </item>
        <item>
         <widget class="QDateTimeEdit" name="select_dateTimeEdit"/>
        </item>
        <item>
         <widget class="QPushButton" name="add_event_button">
          <property name="text">
           <string>Добавить</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout" stretch="50,50">
        <property name="topMargin">
         <number>60</number>
        </property>
        <item>
         <widget class="QLabel" name="calendar_current_label">
          <property name="font">
           <font>
            <family>Verdana</family>
            <pointsize>12</pointsize>
            <weight>75</weight>
            <italic>true</italic>
            <bold>true</bold>
           </font>
          </property>
          <property name="layoutDirection">
           <enum>Qt::LeftToRight</enum>
          </property>
          <property name="text">
           <string>Текущий день:</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="calendar_current_day_label">
          <property name="font">
           <font>
            <family>Verdana</family>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="layoutDirection">
           <enum>Qt::LeftToRight</enum>
          </property>
          <property name="text">
           <string>Не задан</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item row="4" column="0">
     <widget class="QLabel" name="inf_label">
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="text">
       <string>(Чтобы изменить или удалить событие, выберите ряд
 и столбец &quot;Событие&quot; нужного события в таблице)</string>
      </property>
     </widget>
    </item>
    <item row="5" column="0">
     <widget class="QPushButton" name="change_event_button">
      <property name="text">
       <string>Изменить событие</string>
      </property>
     </widget>
    </item>
    <item row="6" column="0">
     <widget class="QPushButton" name="delete_event_button">
      <property name="text">
       <string>Удалить событие</string>
      </property>
     </widget>
    </item>
    <item row="7" column="0">
     <widget class="QLabel" name="image_label">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
    <item row="7" column="1">
     <widget class="QLabel" name="error_label">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1280</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>О программе</string>
    </property>
    <addaction name="action"/>
   </widget>
   <widget class="QMenu" name="menu_2">
    <property name="title">
     <string>Настройки</string>
    </property>
    <addaction name="action_2"/>
    <addaction name="action_CSV"/>
    <addaction name="action_CSV_2"/>
   </widget>
   <addaction name="menu_2"/>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Информация</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Изображения</string>
   </property>
  </action>
  <action name="action_CSV">
   <property name="text">
    <string>Экспорт в CSV файл</string>
   </property>
  </action>
  <action name="action_CSV_2">
   <property name="text">
    <string>Импорт из CSV файла</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

about_template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>798</width>
    <height>337</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>О программе</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>50</y>
     <width>654</width>
     <height>231</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label_3">
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>22</pointsize>
        <weight>75</weight>
        <italic>true</italic>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&quot;Календарщик&quot;</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label">
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>22</pointsize>
        <weight>75</weight>
        <italic>true</italic>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>Автор: Гусевкий Всеволод Витальевич</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_4">
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>20</pointsize>
        <italic>true</italic>
       </font>
      </property>
      <property name="text">
       <string>Фреймворк: PyQt</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_2">
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>20</pointsize>
        <italic>true</italic>
       </font>
      </property>
      <property name="text">
       <string>2024. Лицей Академии Яндекса</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

settings_form = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>483</width>
    <height>301</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Настр. изображения</string>
  </property>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>170</y>
     <width>461</width>
     <height>91</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QPushButton" name="select">
      <property name="text">
       <string>Выбрать изображение</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="set_default">
      <property name="text">
       <string>Установить по умолчанию</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>31</x>
     <y>31</y>
     <width>431</width>
     <height>151</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Verdana</family>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Здесь вы можете установить собственное
изображение, которое будет выводится
в чей-либо день рождения (ТРЕБУЕТСЯ ПЕРЕЗАПУСК)</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

change_form = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>633</width>
    <height>395</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Изменить событие</string>
  </property>
  <widget class="QDateTimeEdit" name="select_dateTimeEdit_w">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>165</y>
     <width>599</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QComboBox" name="marker_select_w">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>130</y>
     <width>599</width>
     <height>20</height>
    </rect>
   </property>
   <property name="layoutDirection">
    <enum>Qt::LeftToRight</enum>
   </property>
   <property name="currentText">
    <string>Цель/задача</string>
   </property>
   <item>
    <property name="text">
     <string>Цель/задача</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>Важная дата</string>
    </property>
   </item>
  </widget>
  <widget class="QLineEdit" name="change_event_lineEdit_w">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>95</y>
     <width>599</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="change_event_label_w">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>57</y>
     <width>599</width>
     <height>23</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Verdana</family>
     <pointsize>14</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="text">
    <string>Изменить событие</string>
   </property>
  </widget>
  <widget class="QPushButton" name="change_event_button_w">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>200</y>
     <width>599</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

export_form = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>391</width>
    <height>285</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Экспорт БД в CSV файл</string>
  </property>
  <widget class="QPushButton" name="directory_select_button">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>30</y>
     <width>251</width>
     <height>91</height>
    </rect>
   </property>
   <property name="text">
    <string>Выбрать директорию для сохранения файла</string>
   </property>
  </widget>
  <widget class="QPushButton" name="export_button">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>150</y>
     <width>251</width>
     <height>81</height>
    </rect>
   </property>
   <property name="text">
    <string>Экспортирвать БД в файл CSV</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

import_form = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>391</width>
    <height>285</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Импорт БД из CSV файла</string>
  </property>
  <widget class="QPushButton" name="import_button">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>150</y>
     <width>251</width>
     <height>81</height>
    </rect>
   </property>
   <property name="text">
    <string>Импортировать БД из CSV файла</string>
   </property>
  </widget>
  <widget class="QPushButton" name="directory_select_button">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>30</y>
     <width>251</width>
     <height>91</height>
    </rect>
   </property>
   <property name="text">
    <string>Выбрать директорию для импорта из файла</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
