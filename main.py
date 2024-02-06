import os
import sys
from PyQt5 import QtWidgets, QtGui
import PyQt5
import requests

map_request = "http://static-maps.yandex.ru/1.x/?ll=30.530887,20.703118&spn=100,5.2&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame





import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class WordTrick(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('карта')
        self.lbl = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap('map.png')
        self.lbl.setPixmap(self.pix)
        self.lbl.move(100, 200)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())