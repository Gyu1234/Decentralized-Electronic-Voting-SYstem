from PyQt5.QtWidgets import *
import sys


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼1')
        self.button2 = QPushButton('버튼2')

        self.vbox_layout = QHBoxLayout()
        self.vbox_layout.addWidget(self.button1)
        self.vbox_layout.addWidget(self.button2)

        self.setLayout(self.vbox_layout)


def exception_hook(except_type, value, traceback):
    print(except_type,value,traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
