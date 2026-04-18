from bai_01_numpy import run_numpy_demo
from bai_02_xu_ly_du_lieu import load_data, clean_data, engineering_data
from bai_03_phan_tich import perform_analysis
from bai_04_truc_quan_hoa import create_visualizations
from bai_05_xuat_du_lieu import export_results
from bai_06_mo_hinh import run_regression_model

def main():
    print("=" * 60)
    print("  HỆ THỐNG PHÂN TÍCH DỮ LIỆU TIÊU THỤ ĐIỆN")
    print("=" * 60)

    # Phần 1: Numpy Demo (Có thể bỏ qua nếu chỉ muốn chạy phân tích)
    run_numpy_demo()

    # Phần 2-4: Xử lý dữ liệu
    df = load_data(nrows=500_000)
    df = clean_data(df)
    df = engineering_data(df)

    # Phần 5: Phân tích
    analysis_results = perform_analysis(df)

    # Phần 6: Biểu đồ
    create_visualizations(df, analysis_results)

    # Phần 7: Mô hình dự báo Linear Regression
    model, rmse, r2 = run_regression_model(df)

    # Phần 8: Xuất dữ liệu
    export_results(df, analysis_results)

    print("\n" + "=" * 60)
    print("  ✅ HOÀN THÀNH TOÀN BỘ QUY TRÌNH!")
    print("=" * 60)

if __name__ == "__main__":
    main()
