# Nghiên cứu các mô hình học máy cho bài toán phân loại video

## Giải thích về triển khai các mô hình

### 1. Cấu trúc và triển khai các mô hình
Trong quá trình thực hiện, em đã tổ chức mã nguồn để có thể chạy nhiều mô hình khác nhau trong cùng một file notebook.

#### 1.1 Các mô hình pre-trained cho phân loại video
File `Pre_trained_3D_CNN.ipynb` chứa việc triển khai các mô hình:
- Pre-trained ResNet50
- Pre-trained Inception-ResNet-v2
- Pre-trained InceptionV3

#### 1.2 Các mô hình phân loại ảnh spectrogram
File `Image classification for data spectrogram.ipynb` triển khai các mô hình:
- VGG16
- DenseNet121
- ResNet50
- InceptionV3
- VGG19

#### 1.3 Các mô hình BERT cho phân loại văn bản
File `simpletransformers.ipynb` triển khai các biến thể của BERT:
- BERT
- PhoBERT
- RoBERTa
  
### 1.4 Lý do sử dụng một file cho nhiều mô hình
Việc triển khai nhiều mô hình trong cùng một file notebook mang lại nhiều lợi ích:
#### Hiệu quả trong phát triển và thử nghiệm
- **Tái sử dụng code**: Các hàm tiền xử lý dữ liệu, đánh giá và trực quan hóa có thể được sử dụng chung cho tất cả các mô hình
- **Giảm thiểu lặp code**: Tránh việc phải viết lại các đoạn code giống nhau ở nhiều file khác nhau
- **Quản lý dữ liệu hiệu quả**: Dữ liệu chỉ cần được nạp một lần và có thể sử dụng cho tất cả các mô hình

#### Tối ưu tài nguyên
- **Tiết kiệm bộ nhớ**: Tránh việc phải tải lại dữ liệu nhiều lần cho từng file riêng biệt
- **Quản lý phiên làm việc**: Dễ dàng theo dõi và quản lý quá trình huấn luyện trong một phiên Google Colab

#### Dễ dàng bảo trì và mở rộng
- **Cấu trúc rõ ràng**: Tất cả các thử nghiệm được tổ chức trong một nơi
- **Dễ thêm mô hình mới**: Có thể nhanh chóng thêm và thử nghiệm các mô hình mới
- **Quản lý phiên bản**: Dễ dàng theo dõi và kiểm soát các thay đổi
  
### 2. Điều chỉnh màu sắc Confusion Matrix
#### Lý do điều chỉnh
- Thầy hướng dẫn tiểu luận khuyên em nên đổi màu sắc của confusion matrix để khi in ra dễ đọc hơn ạ.
*Lưu ý: Việc điều chỉnh này chỉ ảnh hưởng đến cách hiển thị kết quả, không ảnh hưởng đến kết quả đánh giá của các mô hình.*
