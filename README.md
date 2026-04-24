# 📊 Phân Tích Dữ Liệu về Giá Tiền Điện - Tiêu Thụ Điện

**Đề tài 13**: Phân tích dữ liệu về giá tiền điện - tiêu thu điện gia dụng

Dự án phân tích dữ liệu tiêu thụ điện gia dụng theo thời gian với các kỹ thuật xử lý dữ liệu, phân tích, trực quan hóa và dự báo nhằm tìm hiểu mô hình tiêu thụ, ảnh hưởng của giá điện và dự báo tiêu thụ trong tương lai.

## 🎯 Mục Đích

- **Xử lý dữ liệu**: Làm sạch, chuẩn bị và kiểm tra chất lượng dữ liệu tiêu thụ điện
- **Phân tích giá điện**: Phân tích ảnh hưởng của giá tiền điện lên mức tiêu thụ
- **Khám phá mô hình**: Tìm hiểu các mô hình tiêu thụ (theo giờ, ngày, tháng, mùa)
- **Trực quan hóa**: Tạo biểu đồ minh họa các xu hướng và mối quan hệ
- **Dự báo**: Xây dựng mô hình dự báo tiêu thụ điện tương lai
- **Báo cáo**: Tạo báo cáo phân tích chi tiết và khuyến nghị

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
- Load dữ liệu từ file text (semicolon-separated)
- Chuyển đổi kiểu dữ liệu (int, float, datetime)
- Xử lý giá trị missing và anomalies
- Tính toán thống kê cơ bản
- Chuẩn bị dữ liệu cho bước tiếp theo

### **bai_02_xu_ly_du_lieu.py**
Làm sạch & chuẩn bị dữ liệu chi tiết:
- Kiểm tra & xử lý null values
- Loại bỏ duplicates
- Chuyển đổi timestamp
- Tạo features mới
- Chuẩn hóa dữ liệu

### **bai_03_phan_tich.py**
Phân tích thống kê chi tiết:
- Thống kê mô tả (mean, std, min, max, median)
- Tương quan (correlation analysis) giữa tiêu thụ và giá điện
- Phân tích xu hướng theo mùa và theo thời gian
- Phân tích theo giờ, ngày, tuần, tháng
- Ảnh hưởng của giá tiền điện lên mức tiêu thụ
- Thời kỳ cao điểm và thấp điểm tiêu thụ

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
1. Load & chuẩn bị dữ liệu (bai_01, bai_02)
2. Phân tích thống kê & giá điện (bai_03)
3. Trực quan hóa dữ liệu (bai_04)
4. Xây dựng mô hình dự báo (bai_06)
5. Xuất kết quả & báo cáo (bai_05)
6. Tạo báo cáo phân tích cuối cùng
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
- `household_power_consumption.txt` - Dataset tiêu thụ điện gia dụng
  - Định dạng: Text file, semicolon-separated
  - Cột: 
    - Ngày tháng, Thời gian
    - Công suất hoạt động (Global_active_power)
    - Công suất phản kháng (Global_reactive_power)
    - Điện áp (Voltage)
    - Cường độ dòng (Global_intensity)
    - Tiêu thụ từng khoảng (Sub_metering_1/2/3)
  - Kích thước: ~2.1M dòng dữ liệu
  - Thời gian: Từ tháng 12/2006 đến tháng 11/2010

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
- **Linear Regression** - Phân tích ảnh hưởng giá điện lên tiêu thụ
- **Random Forest** - Xác định các yếu tố ảnh hưởng chính
- **ARIMA/SARIMA** - Dự báo chuỗi thời gian tiêu thụ điện
- **LSTM** - Mô hình neural network cho chuỗi thời gian (optional)
- **Regression with Price** - Mô hình dự báo xem xét giá điện

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
- Dữ liệu từ năm 2006-2010 (4 năm tiêu thụ điện thực tế)
- Bao gồm 3 khoảng tiêu thụ (sub-metering) cho các phòng/thiết bị khác nhau
- **Đề tài 13**: Phân tích dữ liệu về giá tiền điện - tiêu thu điện

## 🔍 Ví Dụ Sử Dụng

### Ví dụ 1: Load và làm sạch dữ liệu
```python
from bai_02_xu_ly_du_lieu import load_and_prepare_data

df = load_and_prepare_data('household_power_consumption.txt')
print(df.head())
print(df.describe())
```

### Ví dụ 2: Phân tích tiêu thụ theo giờ
```python
from bai_03_phan_tich import analyze_by_hour

hourly_stats = analyze_by_hour(df)
print(hourly_stats)
```

### Ví dụ 3: Phân tích ảnh hưởng giá điện lên tiêu thụ
```python
from bai_03_phan_tich import analyze_price_impact

# Tính tương quan giữa giá điện và tiêu thụ
correlation = analyze_price_impact(df)
print(f"Tương quan giá-tiêu thụ: {correlation:.3f}")
```

### Ví dụ 4: Dự báo tiêu thụ 30 ngày tới
```python
from bai_06_mo_hinh import train_and_forecast

forecast = train_and_forecast(df, days=30)
print(forecast)
```

## 👨‍💻 Tác Giả

Dự án phân tích dữ liệu tiêu thụ điện gia dụng - Đề tài 13

## 📄 Giấy Phép

MIT License

---

**Cập nhật lần cuối**: 2024
**Phiên bản**: 1.0
**Python**: 3.7+
