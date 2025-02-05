from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2
from OcrPlate import OcrPlate

path_plate = 'model/best_plate.pt'
path_ocr = 'model/best_ocr.pt'

class Main(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)

        self.cap = cv2.VideoCapture(r'test.MOV')
        if not self.cap.isOpened():
            print("Không thể mở camera")
            return
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        # frame = cv2.flip(frame, 1)
        if ret:
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_cp = frame.copy()
            # frame = self.convert_qimg(frame)
            a = OcrPlate(path_model_detect_plate= path_plate, path_model_ocr= path_ocr, imgage_input= frame)
            frame_main = self.convert_qimg(cv2.cvtColor(a.image_output, cv2.COLOR_BGR2RGB))
            digits = a.digit_out

            if(digits != 'unknow'):
                xyxy = a.box_xyxy[-1]
                x, y, x1, y1 = map(int, xyxy)
                frame_cut = frame_cp[y:y1, x:x1]
                frame_plate = self.convert_qimg(frame_cut)

                self.label_plate.setPixmap(QPixmap.fromImage(frame_plate).scaled(self.label_plate.size()))
                self.label_digits.setText(f'{str(digits)}')
            else:
                self.label_plate.setText('Không nhận thấy')
                self.label_digits.setText('Không nhận thấy')
            self.label_main.setPixmap(QPixmap.fromImage(frame_main).scaled(self.label_main.size()))
            
        else:
            print("Không đọc được ảnh")
    def closeEvent(self, event):
        if self.cap.isOpened():
            self.cap.release()
        self.timer.stop()
        event.accept()

    def convert_qimg(self, image):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        # Chuyển numpy array về dạng bytes trước khi tạo QImage
        res = QImage(image.tobytes(), w, h, bytes_per_line, QImage.Format_RGB888)
        return res

import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Main(MainWindow)
MainWindow.show()
sys.exit(app.exec_())