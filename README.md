# Chương trình nhận diện biển số xe

## Sơ qua về dự án:
- Dùng dataset về nhận diện biển số của các loại xe của Việt Nam sau đó train model nhận diện biển số. [Tải tại đây](https://drive.google.com/drive/folders/1Ofqqey7Yqcas_uQSeUc2E8aB1ZTe_S6K?usp=drive_link)

- Dùng dataset về nhận diện các chữ cái xuất hiện ở biển xe sau đó train model nhận diện ra các chữ cái. [Tải tại đây](https://drive.google.com/drive/folders/1fOh2m80gi0309jYNByFMj2AL0098_w0Q?usp=drive_link)

- Kết hợp hai model trên lại với nhau và dùng một số xử lý logic về khoảng cách các tâm của bounding box với nhau mà cho ra được biển số đó có những kí tự gì, và sắp xếp chúng để thành biển số hoàn chỉnh

## Chạy code
- B1: clone dự án về và chạy lệnh sau trên terminal tại chính folder mà đã clone:
    ```bash
        pip install -r 'requirements.txt'
    ```
- B2: tại file main.py nhấn run để chạy demo theo video có sẵn hoặc nếu muốn nhận diện theo real time bằng camera chính thì có thể thay dòng:
    ```python
    cam = cv2.VideoCapture(r"test.MOV")
    ```
    thành :
    ```python
    cam = cv2.VideoCapture(0)
    ```
## Chạy thử 
![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/1%20line.png)
<p style="text-align: center;">Nhận diện với biển 1 dòng</p>

![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/2%20line.png)
<p style="text-align: center;">Nhận diện với biển 2 dòng</p>

## Dự án vẫn đang tích hợp triển khai trên PyQt5 :__: