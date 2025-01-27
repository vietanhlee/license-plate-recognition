import cv2
from OcrPlate import OcrPlate

path_plate = 'best_plate.pt'
path_ocr = 'best_ocr.pt'
cam = cv2.VideoCapture(r"test.MOV")

if not cam.isOpened():
    print('không thể mở cam')
    exit()

while True:
    check, cap = cam.read()
    # cap = cv2.imread(r"C:\Users\levie\OneDrive\Documents\data set bien so\images\train\xemay68.jpg")
    cap = cv2.resize(cap, (800, 600))

    if(check == False):
        print('Không đọc được ảnh')
        break   

    cap_rgb = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)

    Dectect = OcrPlate(path_model_detect_plate= path_plate, path_model_ocr= path_ocr, imgage_input= cap_rgb)
    img_out = Dectect.image_output
    img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)

    cv2.imshow('app', img_out)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break