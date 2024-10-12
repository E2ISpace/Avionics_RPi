import sys
import serial
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

# uic.loadUiType은 두 개의 값을 반환하므로 튜플을 풀어줍니다.


form_class, base_class = uic.loadUiType("/home/E2I/E2I_WorkSpace/Avionics_RPI/RPI_GUI/MainUI.ui")

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    
    def ResetStart(self):
        self.textEdit.append("RESET")
        ResetCode = "RESET"

        if self.serial_port.is_open:
            self.serial_port.write(ResetCode.encode())
            print(f"Sent message: {ResetCode}")
        else:
            print("Serial port is not open")

# QApplication 인스턴스 생성 시 sys.argv를 사용합니다.
app = QApplication(sys.argv)

# 윈도우 클래스 인스턴스를 생성하고 표시합니다.
main_window = WindowClass()
main_window.show()

# 이벤트 루프 실행
app.exec_()
