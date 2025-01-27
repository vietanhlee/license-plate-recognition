from ultralytics import YOLO
import cv2
import numpy as np

class OcrPlate:
    def __init__(self, path_model_detect_plate, path_model_ocr, imgage_input):
        self.model_license = YOLO(path_model_detect_plate)
        self.model_ocr = YOLO(path_model_ocr)
        self.image_input = imgage_input
        self.image_output = imgage_input
        self.digit_out = []
        self.box_xyxy = None
        self.detect_plate_ocr()

    def detect_plate_ocr(self):
        lbs = self.model_ocr.names
        res_detect_plate = self.model_license.predict(source= self.image_input, conf = 0.8, verbose = False)

        box = res_detect_plate[0].boxes.xyxy
        self.box_xyxy = box

        for x, y, x1, y1 in box:
            x, y, x1, y1 = map(int, [x, y, x1, y1])

            img_plate = self.image_input[y :y1, x:x1]

            res_ocr = self.model_ocr.predict(verbose = False, source= img_plate, conf = 0.6)

            len_digits = len(res_ocr[0].boxes.cls)

            digit = 'unknow'
            if (len_digits >= 7 and len_digits <= 10) and min(res_ocr[0].boxes.conf) > 0.7:
                cls = res_ocr[0].boxes.cls
                cls = cls.reshape(-1, 1)
                cls = np.array(cls)

                xy_center = res_ocr[0].boxes.xywh[:, :2]
                xy_center = np.array(xy_center)

                data = np.hstack([xy_center, cls])
                digit = self.process_ocr(data_center_labe= data, labels_encoder= lbs)
                self.digit_out.append(digit)
            
            cv2.putText(self.image_output, str(digit), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.rectangle(self.image_output, (x, y), (x1, y1), (0, 255, 0), 2)
        
    def process_ocr(self, data_center_labe: np.array, labels_encoder: dict):
        delta = np.max(data_center_labe[:, 1]) - np.min(data_center_labe[:, 1])
        out_ocr = None

        if(delta > 20):
            y_mean = np.mean(data_center_labe[:, 1])
            
            line1 = data_center_labe[data_center_labe[:, 1] < y_mean]
            line2 = data_center_labe[data_center_labe[:, 1] >= y_mean]

            line1 = line1[line1[:, 0].argsort()]
            line2 = line2[line2[:, 0].argsort()]

            out_ocr = ''.join([labels_encoder[item] for item in line1[:,-1]])
            out_ocr += '-' + ''.join([labels_encoder[item] for item in line2[:,-1]])
        else:
            data_center_labe = data_center_labe[data_center_labe[:, 0].argsort()]
            out_ocr = ''.join([labels_encoder[item] for item in data_center_labe[:,-1]])
            out_ocr = out_ocr[:3] + '-' + out_ocr[3:]
        return out_ocr