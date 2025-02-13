import cv2
import time
from OcrPlate import OcrPlate

path_plate = 'model/best_plate.pt'
path_ocr = 'model/best_ocr.pt'

ocr_plate = OcrPlate(path_model_detect_plate=path_plate, path_model_ocr=path_ocr)
cam = cv2.VideoCapture(r"test.MOV")

if not cam.isOpened():
    print('không thể mở cam')
    exit()

prev_time = time.time()

while True:
    check, cap = cam.read()
    if not check:
        print('Không đọc được ảnh')
        break  

    cap = cv2.resize(cap, (800, 600))

    ocr_plate.set_data(imgage_input=cap)
    img_out = ocr_plate.image_output

    # Tính FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Hiển thị FPS trên ảnh
    cv2.putText(img_out, f'FPS: {fps:.2f}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2)

    # Ghi ra màn hình
    cv2.imshow('test code', img_out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
