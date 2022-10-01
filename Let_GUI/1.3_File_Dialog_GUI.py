from PyQt5.QtWidgets import *
import sys


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button = QPushButton('파일 열기')
        self.button.clicked.connect(self.button_click)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button)

        self.setLayout(self.hbox_layout)

    def button_click(self):
        path, _ = QFileDialog.getOpenFileName(self, '파일을 선택하세요.', '.', 'All files(*.*)')
        if path == '':
            print('취소')

        else:
            print('파일 경로',path)


def exception_hook(except_type, value, traceback):
    print(except_type,value,traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())