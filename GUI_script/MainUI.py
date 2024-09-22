import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

# uic.loadUiType은 두 개의 값을 반환하므로 튜플을 풀어줍니다.
form_class, base_class = uic.loadUiType("D:\\EEI\\Avionics_RPi\\RPI_GUI\\MainUI.ui")

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# QApplication 인스턴스 생성 시 sys.argv를 사용합니다.
app = QApplication(sys.argv)

# 윈도우 클래스 인스턴스를 생성하고 표시합니다.
main_window = WindowClass()
main_window.show()

# 이벤트 루프 실행
app.exec_()


