import os
from cau_hinh import OUTPUT_DIR
from tien_ich import print_section_header

def export_results(df, analysis_results):
    print_section_header("PHẦN 7: LƯU FILE")

    # 1. Lưu DataFrame đã xử lý
    cols_save = ["Datetime","Gio","Thang","Nam","Thu",
                 "Global_active_power","Global_reactive_power",
                 "Voltage","Global_intensity",
                 "Sub_metering_1","Sub_metering_2","Sub_metering_3",
                 "Tong_sub_metering","GAP_minmax","Muc_tieu_thu"]
    
    processed_path = os.path.join(OUTPUT_DIR, "du_lieu_da_xu_ly.csv")
    df[cols_save].to_csv(processed_path, index=False, encoding="utf-8-sig")
    print(f"\n[1] ✅ Lưu: {os.path.basename(processed_path)}")

    # 2. Lưu bảng thống kê theo tháng
    agg_path = os.path.join(OUTPUT_DIR, "thong_ke_theo_thang.csv")
    analysis_results['agg_thang'].to_csv(agg_path, encoding="utf-8-sig")
    print(f"[2] ✅ Lưu: {os.path.basename(agg_path)}")

    # 3. Lưu pivot table
    pivot_path = os.path.join(OUTPUT_DIR, "pivot_gio_thang.csv")
    analysis_results['pivot'].to_csv(pivot_path, encoding="utf-8-sig")
    print(f"[3] ✅ Lưu: {os.path.basename(pivot_path)}")

if __name__ == "__main__":
    pass
