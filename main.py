import os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys
from PyQt5 import QtWidgets, QtGui
import requests





class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.map()

        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('карта')
        self.pix = QLabel(self)
        self.pix.setPixmap(QPixmap('map.png'))
        self.pix.move(0, 0)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.x -= 1
            self.map()
            self.map_update()
        elif event.key() == Qt.Key_Down:
            self.x += 1
            self.map()
            print('down', self.x)
            self.map_update()

    def map_update(self):
        self.pix.setPixmap(QPixmap('map.png'))
        self.pix.move(0, 0)

    def map(self):

        toponym_longitude, toponym_lattitude = '37.530887', '55.703118'
        delta = "0.005"
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "l": "map",
            'z': f'{self.x}'
        }
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        # ... и выполняем запрос
        response = requests.get(map_api_server, params=map_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())