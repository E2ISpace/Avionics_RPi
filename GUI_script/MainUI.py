import sys
import serial
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

# uic.loadUiType은 두 개의 값을 반환하므로 튜플을 풀어줍니다.
form_class, base_class = uic.loadUiType("/home/E2I/E2I_WorkSpace/Avionics_RPI/RPI_GUI/MainUI.ui")

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 시리얼 포트 초기화 (예외 처리 추가)
        try:
            self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        except serial.SerialException as e:
            self.show_error_message(f"Error opening serial port: {e}")
        
        # 버튼 클릭 시 ResetStart 실행
        self.pushButton.clicked.connect(self.ResetStart)

    def ResetStart(self):
        reset_code = "RESET"

        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(reset_code.encode())
            self.textEdit.append(f"Sent message: {reset_code}")
        else:
            self.show_error_message("Serial port is not open")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

# QApplication 인스턴스 생성 시 sys.argv를 사용합니다.
app = QApplication(sys.argv)

# 윈도우 클래스 인스턴스를 생성하고 표시합니다.
main_window = WindowClass()
main_window.show()

# 이벤트 루프 실행
app.exec_()

