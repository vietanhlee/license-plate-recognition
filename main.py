import cv2
from OcrPlate import OcrPlate

path_plate = 'model/best_plate.pt'
path_ocr = 'model/best_ocr.pt'

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
    # Chuyển về ảnh RGB vì model được huấn luyện đọc ảnh bằng rgb
    cap_rgb = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)

    Dectect = OcrPlate(path_model_detect_plate= path_plate, path_model_ocr= path_ocr, imgage_input= cap_rgb)
    # Lấy ra img cuối cùng sau khi đã vẽ các box và đánh nhãn các biển số
    img_out = Dectect.image_output
    # Chuyển về BRG để cv2 hiển thị lên màn 
    img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)
    # Ghi ra màn
    cv2.imshow('test code', img_out)
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()