import numpy as np

class OcrOutput():
    '''Input is array 2D dimensions included fisrt collums is x_center, second is y_center and thirt is lable encoder'''
    def __init__(self, data: np.array, labels_encoder: dict):
        self.data = data.copy()
        self.labels_encoder = labels_encoder
        self.out_ocr = None

        delta = np.max(self.data[:, 1]) - np.min(self.data[:, 1])
        
        if(delta > 20):
            y_mean = np.mean(self.data[:, 1])
            
            line1 = data[data[:, 1] < y_mean]
            line2 = data[data[:, 1] >= y_mean]

            line1 = line1[line1[:, 0].argsort()]
            line2 = line2[line2[:, 0].argsort()]

            self.out_ocr = ''.join([self.labels_encoder[item] for item in line1[:,-1]])
            self.out_ocr += '-' + ''.join([self.labels_encoder[item] for item in line2[:,-1]])
        else:
            self.data = self.data[self.data[:, 0].argsort()]
            self.out_ocr = ''.join([self.labels_encoder[item] for item in self.data[:,-1]])
            self.out_ocr = self.out_ocr[:3] + '-' + self.out_ocr[3:]

    def __str__(self):
        return self.out_ocr



