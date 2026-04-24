# 📊 Phân Tích Tiêu Thụ Điện Gia Dụng

Dự án phân tích dữ liệu tiêu thụ điện gia dụng theo thời gian với các kỹ thuật xử lý dữ liệu, phân tích, trực quan hóa và dự báo.

## 🎯 Mục Đích

- Làm sạch và chuẩn bị dữ liệu tiêu thụ điện
- Khám phá các mô hình tiêu thụ và xu hướng
- Trực quan hóa dữ liệu bằng biểu đồ đa dạng
- Xây dựng mô hình dự báo tiêu thụ điện tương lai
- Tạo báo cáo phân tích chi tiết

## 📁 Cấu Trúc Dự Án

```
phantichdien/
├── main.py                              # Script chính - chạy toàn bộ pipeline
├── cau_hinh.py                          # Cấu hình, hằng số
├── tien_ich.py                          # Hàm tiện ích dùng chung
│
├── bai_01_numpy.py                      # Xử lý dữ liệu với NumPy
├── bai_02_xu_ly_du_lieu.py              # Làm sạch & chuẩn bị dữ liệu
├── bai_03_phan_tich.py                  # Phân tích thống kê
├── bai_04_truc_quan_hoa.py              # Tạo biểu đồ trực quan hóa
├── bai_05_xuat_du_lieu.py               # Xuất kết quả
├── bai_06_mo_hinh.py                    # Xây dựng mô hình dự báo
│
├── household_power_consumption.txt      # Dataset gốc
├── linkdataset.txt                      # Link tải dataset
├── output/                              # Thư mục lưu kết quả
│
└── README.md                            # Tài liệu này
```

## 📋 Mô Tả Chi Tiết Các Module

### **cau_hinh.py**
Chứa các hằng số cấu hình:
- Đường dẫn file dữ liệu
- Tham số xử lý dữ liệu
- Cấu hình biểu đồ (kích thước, màu sắc, fonts)
- Thông số mô hình machine learning

```python
# Ví dụ
DATA_FILE = 'household_power_consumption.txt'
OUTPUT_DIR = 'output'
FIGURE_DPI = 150
MODEL_TEST_SIZE = 0.2
```

### **tien_ich.py**
Hàm tiện ích dùng chung:
- Hàm load/save dữ liệu
- Hàm làm sạch dữ liệu
- Hàm đánh giá mô hình
- Hàm tạo biểu đồ

### **bai_01_numpy.py**
Xử lý dữ liệu cơ bản với NumPy:
- Load dữ liệu từ file text
- Chuyển đổi kiểu dữ liệu
- Xử lý giá trị missing
- Tính toán thống kê cơ bản

### **bai_02_xu_ly_du_lieu.py**
Làm sạch & chuẩn bị dữ liệu chi tiết:
- Kiểm tra & xử lý null values
- Loại bỏ duplicates
- Chuyển đổi timestamp
- Tạo features mới
- Chuẩn hóa dữ liệu

### **bai_03_phan_tich.py**
Phân tích thống kê:
- Thống kê mô tả (mean, std, min, max)
- Tương quan (correlation analysis)
- Phân tích xu hướng theo mùa
- Phân tích theo giờ, ngày, tháng

### **bai_04_truc_quan_hoa.py**
Tạo biểu đồ và trực quan hóa:
- Line chart: Doanh thụ theo thời gian
- Bar chart: Tiêu thụ theo giờ/ngày/tháng
- Heatmap: Mô hình mùa vụ
- Box plot: Phân phối dữ liệu
- Scatter plot: Tương quan giữa biến

### **bai_05_xuat_du_lieu.py**
Xuất kết quả:
- Lưu dữ liệu đã xử lý thành CSV
- Xuất báo cáo thống kê
- Lưu biểu đồ dạng PNG/PDF
- Tạo bảng tóm tắt

### **bai_06_mo_hinh.py**
Xây dựng mô hình dự báo:
- Linear Regression
- Random Forest
- Time Series (ARIMA/SARIMA)
- LSTM Neural Network
- So sánh hiệu suất mô hình
- Dự báo tương lai

### **main.py**
Script chính - Orchestration:
```
1. Load & chuẩn bị dữ liệu (bai_02)
2. Phân tích thống kê (bai_03)
3. Trực quan hóa (bai_04)
4. Xây dựng mô hình (bai_06)
5. Xuất kết quả (bai_05)
6. Tạo báo cáo
```

## 🚀 Cách Chạy

### 1. **Chạy toàn bộ pipeline**
```bash
python main.py
```

### 2. **Chạy từng bước riêng lẻ**
```bash
# Bước 1: NumPy processing
python bai_01_numpy.py

# Bước 2: Xử lý dữ liệu
python bai_02_xu_ly_du_lieu.py

# Bước 3: Phân tích
python bai_03_phan_tich.py

# Bước 4: Trực quan hóa
python bai_04_truc_quan_hoa.py

# Bước 5: Xuất dữ liệu
python bai_05_xuat_du_lieu.py

# Bước 6: Mô hình & Dự báo
python bai_06_mo_hinh.py
```

### 3. **Import hàm từ module**
```python
from tien_ich import load_data, clean_data
from bai_02_xu_ly_du_lieu import prepare_dataset
from bai_06_mo_hinh import train_model, forecast

# Sử dụng các hàm
df = load_data('household_power_consumption.txt')
df_clean = clean_data(df)
```

## 📊 Input & Output

### Input
- `household_power_consumption.txt` - Dataset tiêu thụ điện gốc
  - Định dạng: Text file, semicolon-separated
  - Cột: Date, Time, Global_active_power, Global_reactive_power, Voltage, Global_intensity, Sub_metering_1/2/3
  - Kích thước: ~2.1M dòng dữ liệu

### Output (trong thư mục `output/`)
- `data_cleaned.csv` - Dữ liệu đã làm sạch
- `statistics.csv` - Thống kê mô tả
- `correlation.csv` - Ma trận tương quan
- `figure_timeseries.png` - Biểu đồ chuỗi thời gian
- `figure_hourly_pattern.png` - Mô hình theo giờ
- `figure_seasonal.png` - Phân tích mùa vụ
- `figure_correlation.png` - Heatmap tương quan
- `forecast_results.csv` - Kết quả dự báo
- `model_evaluation.csv` - Đánh giá mô hình
- `report.txt` - Báo cáo tóm tắt

## 📦 Yêu Cầu & Cài Đặt

### Dependencies
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
statsmodels>=0.13.0  # Cho ARIMA/SARIMA
tensorflow>=2.6.0    # Cho LSTM (optional)
```

### Cài đặt
```bash
# Cách 1: Cài từng package
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels

# Cách 2: Cài từ requirements.txt (nếu có)
pip install -r requirements.txt
```

## 📈 Kỹ Thuật Sử Dụng

### Data Processing
- Handling Missing Values (forward fill, interpolation)
- Outlier Detection & Handling
- Feature Engineering (lag features, rolling averages)
- Data Normalization/Standardization

### Analysis Methods
- Descriptive Statistics
- Correlation Analysis
- Time Series Decomposition
- Seasonal Pattern Detection
- Trend Analysis

### Visualization Techniques
- Time Series Plot
- Heatmap (seasonal patterns)
- Box Plot (distribution)
- Scatter Plot (relationships)
- Histogram (frequency distribution)

### Machine Learning Models
- **Linear Regression** - Baseline model
- **Random Forest** - Non-linear patterns
- **ARIMA/SARIMA** - Time series forecasting
- **LSTM** - Deep learning for sequences (optional)

### Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- R² Score

## 💡 Tips & Best Practices

1. **Lưu cấu hình** - Chỉnh sửa `cau_hinh.py` để thay đổi tham số
2. **Xem logs** - Các script sẽ in thông tin tiến trình
3. **Kiểm tra output** - Xem folder `output/` để kiểm tra kết quả
4. **Tái sử dụng code** - Các hàm trong `tien_ich.py` có thể dùng riêng lẻ
5. **Mở rộng** - Dễ dàng thêm mô hình hoặc phương pháp phân tích mới


## 📝 Ghi Chú

- Dataset gốc từ UCI Machine Learning Repository
- Link: Xem trong file `linkdataset.txt`
- Dữ liệu từ năm 2006-2010
- Được cập nhật thường xuyên
