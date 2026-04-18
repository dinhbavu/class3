import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import os
from tien_ich import print_section_header

def run_regression_model(df):
    print_section_header("PHẦN 6: MÔ HÌNH HỒI QUY (LINEAR REGRESSION)")
    
    # 1. Chọn đặc trưng (Features) và nhãn (Target)
    # Target: Dự đoán Global_active_power
    features = ['Global_reactive_power', 'Voltage', 'Global_intensity', 
                'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
    target = 'Global_active_power'
    
    # Lọc lại dữ liệu chứa các cột này và dropna
    df_model = df.dropna(subset=features + [target])
    
    X = df_model[features]
    y = df_model[target]
    
    # 2. Chia dữ liệu Train/Test (80% Train, 20% Test)
    print("\n[1] Đang chia dữ liệu Train/Test (80% Huấn luyện, 20% Kiểm thử)...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"    - Tập Huấn luyện (Train): {X_train.shape[0]:,} dòng")
    print(f"    - Tập Kiểm thử (Test)   : {X_test.shape[0]:,} dòng")
    
    # 3. Tạo và huấn luyện mô hình
    print("\n[2] Đang huấn luyện mô hình Linear Regression...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("    ✅ Huấn luyện hoàn tất!")
    
    # 4. Dự đoán trên tập Test
    y_pred = model.predict(X_test)
    
    # 5. Đánh giá mô hình
    print("\n[3] ĐÁNH GIÁ MÔ HÌNH:")
    import numpy as np
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"    - Hệ số xác định (R² Score): {r2:.4f} (Giá trị tối đa là 1.0)")
    print(f"    - Sai số toàn phương trung bình (RMSE): {rmse:.4f}")
    print(f"    - Sai số tuyệt đối trung bình (MAE): {mae:.4f}")
    
    print("\n[4] INSIGHT TỪ MÔ HÌNH (Nhận xét và đề xuất):")
    print(f"    - Nhận xét: Mô hình tuyến tính giải thích được {r2*100:.2f}% sự biến thiên của {target}.")
    print("      Điều này cho thấy có mối quan hệ rất mạnh giữa các thông số phụ (đặc biệt là Global_intensity) và tổng tiêu thụ điện.")
    print("    - Đề xuất: Trong hệ thống đo đạc thực tế, việc trang bị cảm biến đo dòng điện (Intensity) là đủ để xấp xỉ mức tiêu thụ điện năng với độ chuẩn xác cao, giúp tối ưu chi phí lắp đặt đa cảm biến.")

    # 6. Trực quan hóa kết quả (So sánh 100 điểm dữ liệu đầu tiên)
    print("\n[5] Đang vẽ biểu đồ so sánh kết quả thực tế và dự đoán...")
    plt.figure(figsize=(10, 5))
    plt.plot(y_test.values[:100], label='Thực tế (Actual)', marker='o', linestyle='-', alpha=0.7)
    plt.plot(y_pred[:100], label='Dự đoán (Predicted)', marker='x', linestyle='--', alpha=0.7)
    plt.title("Linear Regression: So sánh 100 giá trị Dự đoán và Thực tế vòng đầu tiên")
    plt.xlabel("Mẫu dữ liệu tập Test (Sample/Index)")
    plt.ylabel("Global Active Power (kW)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    if not os.path.exists("output"):
        os.makedirs("output")
    plt.savefig("output/bai06_linear_regression.png", dpi=300, bbox_inches='tight')
    # plt.show() # Tạm thời comment plt.show() để máy không bị đứng khi chạy luồng tự động
    print("    ✅ Đã lưu biểu đồ kết quả mô hình vào: output/bai06_linear_regression.png")
    
    return model, rmse, r2

if __name__ == "__main__":
    from bai_02_xu_ly_du_lieu import load_data, clean_data, engineering_data
    # Nhập thử 20_000 dòng để test model
    df_test = load_data(nrows=20_000)
    df_test = clean_data(df_test)
    df_test = engineering_data(df_test)
    run_regression_model(df_test)
