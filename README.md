# Chương trình nhận diện biển số xe

## Sơ qua về code:
- Dùng dataset về nhận diện biển số của các loại xe của Việt Nam sau đó train model nhận diện biển số. [Tải tại đây](https://drive.google.com/drive/folders/1Ofqqey7Yqcas_uQSeUc2E8aB1ZTe_S6K?usp=drive_link)

- Dùng dataset về nhận diện các chữ cái xuất hiện ở biển xe sau đó train model nhận diện ra các chữ cái. [Tải tại đây](https://drive.google.com/drive/folders/1fOh2m80gi0309jYNByFMj2AL0098_w0Q?usp=drive_link)

- Kết hợp hai model trên lại với nhau và dùng một số xử lý logic về khoảng cách các tâm của bounding box với nhau mà cho ra được biển số đó có những kí tự gì, và sắp xếp chúng để thành biển số hoàn chỉnh

> File `OcrPlate.py` chính là class gồm một số công cụ trong đó có chức năng trả về kí tự đọc được trên biển số từ một ảnh được đưa vào
## Chạy code
- **B1**: clone dự án về và chạy lệnh sau trên terminal tại chính folder mà đã clone:
    ```bash
    pip install -r 'requirements.txt'
    ```
- **B2**: tại file `main.py` nhấn run để chạy demo theo video có sẵn hoặc nếu muốn nhận diện theo real time bằng camera chính thì có thể thay dòng:
    ```python
    cam = cv2.VideoCapture(r"test.MOV")
    ```
    thành :
    ```python
    cam = cv2.VideoCapture(0)
    ```
## Kết quả với từng loại biển
Việc phát hiện biển số và các kí tự có trên biển có thể được coi là dễ nhưng việc từ các kí tự đó sắp xếp sao cho đúng trình tự thì là một vấn đề khá phức tạp

![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/display%20github/1%20line.png)

<p align = 'center'>Nhận diện với biển 1 dòng</p>

![anh](https://raw.githubusercontent.com/vietanhlee/license-plate-recognition/refs/heads/main/display%20github/2%20line.png)

<p align = 'center'>Nhận diện với biển 2 dòng</p>

## Tích hợp vào dự án quản lý vé xe phục vụ cho bãi gửi xe trên PyQt5

Link project ở [đây](https://github.com/vietanhlee/parking-ticket-management)

![anh](https://raw.githubusercontent.com/vietanhlee/parking-ticket-management/refs/heads/main/display_github/Screenshot%202025-02-13%20191333.png)

<p align = 'center'>Demo trên Qt5 </p>