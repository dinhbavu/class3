| STT | Nhiệm vụ | Trạng thái |
|-----|----------|------------|
| 1 | Thu thập và tìm hiểu bộ dữ liệu | ✅ |
| 2 | Phần 1 – NumPy (mảng, ma trận, thống kê, lọc dữ liệu) | ✅ |
| 3 | Phần 2 – Pandas cơ bản (Series, DataFrame, đọc file) | ✅ |
| 4 | Phần 3 – Làm sạch dữ liệu (null, trùng, ép kiểu, chuỗi) | ✅ |
| 5 | Phần 4 – Feature Engineering (cột mới, chuẩn hóa, phân loại) | ✅ |
| 6 | Phần 5 – Phân tích thống kê (groupby, pivot table, outlier) | ✅ |
| 7 | Phần 6 – Trực quan hóa (7 biểu đồ Matplotlib) | ✅ |
| 8 | Phần 7 – Lưu kết quả CSV | ✅ |


Mô tả code

Phần 1 – NumPy
Tạo mảng 1D/2D/3D, ma trận đặc biệt (zeros, ones, eye), dãy số (`arange`), ma trận ngẫu nhiên. Thực hành thống kê (sum, mean, max, min, std) theo trục, indexing/slicing, lọc boolean, `np.where()`, `argmax()`, chuẩn hóa Z-score.

Phần 2 – Pandas Cơ Bản
Tạo `Series` và `DataFrame` mẫu. Đọc file `.txt` phân cách `;` bằng `pd.read_csv()` với 500,000 dòng. Khám phá dữ liệu qua `head()`, `info()`, `describe()`, lọc và đếm giá trị bằng `value_counts()`.

Phần 3 – Làm Sạch Dữ Liệu
Kiểm tra null (`isnull().sum()`), điền giá trị thiếu bằng trung bình (`fillna`), xóa dòng thiếu (`dropna`), xóa trùng (`drop_duplicates`). Ép kiểu cột ngày giờ sang `datetime`, xử lý chuỗi với `str.strip()`, `str.title()`, `str.upper()`.

Phần 4 – Feature Engineering
Tạo cột `Tong_sub_metering`, trích xuất giờ/ngày/tháng/năm/thứ từ `Datetime`. Chuẩn hóa Min-Max cho `Global_active_power`. Phân loại mức tiêu thụ thành 4 nhóm (Thấp / Trung bình / Cao / Rất cao) bằng `.apply()`.

Phần 5 – Phân Tích Thống Kê
Groupby theo giờ, tháng để tính mean/max/min/std/count. Tìm top 3 ngày tiêu thụ cao nhất (`nlargest`). Tạo pivot table Giờ × Tháng. Phát hiện outlier bằng phương pháp IQR.

Phần 6 – Trực Quan Hóa

| # | Loại biểu đồ | Nội dung |
|---|--------------|----------|
| 1 | Line chart | Công suất TB theo giờ trong ngày |
| 2 | Bar chart | Công suất TB theo tháng |
| 3 | Horizontal bar | Phân bố mức tiêu thụ |
| 4 | Histogram | Phân phối tần suất công suất |
| 5 | Scatter plot | Điện áp vs Công suất (màu = giờ) |
| 6 | Subplot 2×2 | 4 chỉ số điện biến thiên theo giờ |
| 7 | Heatmap | Công suất TB theo Giờ × Tháng |

Phần 7 – Lưu Kết Quả



Bộ Dữ Liệu
https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set?utm_source=chatgpt.com

