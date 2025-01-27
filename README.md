# Chương trình nhận diện biển số xe

## Sơ qua về dự án:
- Dùng dataset về nhận diện biển số của các loại xe của Việt Nam: sau đó train model nhận diện biển số
- Dùng dataset về nhận diện các chữ cái xuất hiện ở biển xe: sau đó train model nhận diện ra các chữ cái
- Kết hợp hai model trên lại với nhau và dùng một số xử lý logic về khoảng cách các tâm của bounding box với nhau mà cho ra được biển số đó có những kí tự gì

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
## Dự án vẫn đang tích hợp triển khai trên PyQt5 :__: