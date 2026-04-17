import pandas as pd
from tien_ich import print_section_header

def perform_analysis(df):
    print_section_header("PHẦN 5: PHÂN TÍCH")

    results = {}

    # 1. Trung bình theo nhóm (groupby giờ)
    results['tb_theo_gio'] = df.groupby("Gio")["Global_active_power"].mean().round(3)
    print("\n[1] Trung bình công suất theo giờ:\n", results['tb_theo_gio'])

    # 2. Đếm số lượng theo nhóm
    so_luong_muc = df.groupby("Muc_tieu_thu")["Global_active_power"].count()
    print("\n[2] Số bản ghi theo mức tiêu thụ:\n", so_luong_muc)

    # 3. Tìm max theo nhóm (theo tháng)
    print("\n[3] Công suất max theo tháng:")
    print(df.groupby("Thang")["Global_active_power"].max().round(3))

    # 4. Nhiều hàm cùng lúc (agg)
    results['agg_thang'] = df.groupby("Thang")["Global_active_power"].agg(
        ["mean", "max", "min", "std", "count"]
    ).round(3)
    print("\n[4] Tổng hợp đa hàm theo tháng:\n", results['agg_thang'])

    # 5. Top 3 ngày tiêu thụ điện cao nhất
    print("\n[5] Top 3 ngày tiêu thụ điện cao nhất:")
    print(df.groupby("Ngay")["Global_active_power"].mean().nlargest(3))

    # 6. Pivot table (giờ x tháng → trung bình công suất)
    results['pivot'] = df.pivot_table(
        values="Global_active_power",
        index="Gio",
        columns="Thang",
        aggfunc="mean"
    ).round(2)
    print("\n[6] Pivot table (Giờ × Tháng) created.")

    # 7. Phát hiện giá trị bất thường (IQR)
    Q1 = df["Global_active_power"].quantile(0.25)
    Q3 = df["Global_active_power"].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df["Global_active_power"] < Q1 - 1.5 * IQR) |
                  (df["Global_active_power"] > Q3 + 1.5 * IQR)]
    print(f"\n[7] Phát hiện outlier (IQR): {len(outliers)} bản ghi bất thường")

    return results

if __name__ == "__main__":
    from bai_02_xu_ly_du_lieu import load_data, clean_data, engineering_data
    
    # Tải và tiền xử lý dữ liệu trước khi phân tích
    df = load_data()
    df = clean_data(df)
    df = engineering_data(df)
    
    # Thực hiện phân tích
    perform_analysis(df)
