import requests
from PyQt5.QtWidgets import *
import sys
import json

class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.form_layout = QFormLayout()

        self.Q1 = QLineEdit()
        self.Selection1 = QLineEdit()
        self.Selection2 = QLineEdit()
        self.Selection3 = QLineEdit()
        self.button1 = QPushButton('개시')
        self.button2 = QPushButton('초기화')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.form_layout.addRow('질문', self.Q1)
        self.form_layout.addRow('선택지', self.Selection1)
        self.form_layout.addRow('', self.Selection2)
        self.form_layout.addRow('', self.Selection3)
        self.form_layout.addRow('', self.hbox_layout)

        self.setLayout(self.form_layout)


    def button1_click(self):
        headers = {'Content-Type': 'application/json'}

        Q1 = self.Q1.text()
        Selection1 = self.Selection1.text()
        Selection2 = self.Selection2.text()
        Selection3 = self.Selection3.text()

        data = {
            'Q1': Q1,
            'Selections' : [Selection1, Selection2, Selection3]
        }

        res = requests.post(
            'http://127.0.0.1:5000/open',
            data=json.dumps(data),
            headers=headers
        )
        print(res.text)
        self.button1_click()


    def button2_click(self):
        self.Q1.setText('')
        self.Selection1.setText('')
        self.Selection2.setText('')
        self.Selection3.setText('')


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        # self.menu_group_box = QGroupBox('메뉴')
        #
        # self.Vote_button = QPushButton('투표 조회')
        #
        # self.hbox_layout = QHBoxLayout()
        # self.hbox_layout.addWidget(self.Vote_button)
        #
        # self.group_box.setLayout(self.hbox_layout)
        #
        #
        # self.vote_layout = QGridLayout()
        self.vote_layout_layout.addWidget(self.menu_group_box, 0, 0, 1, 2)
        self.setLayout(self.vote_layout)



class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('블록 체인 투표 시스템')

        self.tab1 = Tab1()
        self.tab2 = Tab2()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1, '투표 생성')
        self.tabs.addTab(self.tab2, '투표')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)

        self.setLayout(self.vbox_layout)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
