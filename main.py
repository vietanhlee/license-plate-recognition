from ultralytics import YOLO
import cv2
import pytesseract
import numpy as np
from OcrOutput import OcrOutput

model_license = YOLO('best (1).pt')
model_ocr = YOLO('best ocr.pt')

lbs = model_ocr.names

cam = cv2.VideoCapture(r"test.MOV")

if not cam.isOpened():
    print('không thể mở cam')
    exit()

while True:
    check, cap = cam.read()
    cap = cv2.resize(cap, (800, 600))

    if(check == False):
        print('Không đọc được ảnh')
        break   

    cap_rgb = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
    license_plate = model_license.predict(source= cap_rgb, conf = 0.8, verbose = False)
    
    box = license_plate[0].boxes.xyxy

    for x, y, x1, y1 in box:
        x, y, x1, y1 = map(int, [x, y, x1, y1])

        img_plate = cap_rgb[y :y1, x:x1]

        res_ocr = model_ocr.predict(verbose = False, source= img_plate, conf = 0.6)

        digits = 'UNKNOW'
        len_digits = len(res_ocr[0].boxes.cls)

        if (len_digits >=7 and len_digits <= 10) and min(res_ocr[0].boxes.conf) > 0.7:
            cls = res_ocr[0].boxes.cls
            cls = cls.reshape(-1, 1)
            cls = np.array(cls)

            xy_center = res_ocr[0].boxes.xywh[:, :2]
            xy_center = np.array(xy_center)

            data = np.hstack([xy_center, cls])

            digits = OcrOutput(data= data, labels_encoder= lbs)
            print(digits)
        
        cv2.putText(cap, str(digits), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.rectangle(cap, (x, y), (x1, y1), (0, 255, 0), 2)
        
        
        im = res_ocr[0].plot()

    cv2.imshow('app', cap)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break