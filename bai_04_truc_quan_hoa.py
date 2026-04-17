import matplotlib.pyplot as plt
import os
import numpy as np
from cau_hinh import OUTPUT_DIR, COLORS
from tien_ich import print_section_header

def create_visualizations(df, analysis_results):
    print_section_header("PHẦN 6: BIỂU ĐỒ")
    
    plt.style.use("seaborn-v0_8-whitegrid")
    tb_theo_gio = analysis_results['tb_theo_gio']
    pivot = analysis_results['pivot']

    # ── Biểu đồ 1: Line – Công suất TB theo giờ
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(tb_theo_gio.index, tb_theo_gio.values,
            color=COLORS[0], linewidth=2.5, marker="o", markersize=5)
    ax.set_title("Biểu đồ đường – Công suất TB theo giờ trong ngày", fontsize=13, fontweight="bold")
    ax.set_xlabel("Giờ")
    ax.set_ylabel("Công suất TB (kW)")
    ax.legend(["Global Active Power"], loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "01_line_cong_suat_theo_gio.png"), dpi=120)
    plt.close()
    print("[1] ✅ Lưu: 01_Công suất TB theo giờ.png")

    # ── Biểu đồ 2: Bar – Công suất TB theo tháng
    tb_thang = df.groupby("Thang")["Global_active_power"].mean()
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(tb_thang.index, tb_thang.values, color=COLORS, edgecolor="white")
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f"{bar.get_height():.2f}", ha="center", va="bottom", fontsize=9)
    ax.set_title("Biểu đồ cột – Công suất TB theo tháng", fontsize=13, fontweight="bold")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Công suất TB (kW)")
    ax.set_xticks(tb_thang.index)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "02_bar_cong_suat_theo_thang.png"), dpi=120)
    plt.close()
    print("[2] ✅ Lưu: 02_Công suất TB theo tháng.png")

    # ── Biểu đồ 3: Barh – Mức tiêu thụ
    muc_count = df["Muc_tieu_thu"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(muc_count.index, muc_count.values, color=COLORS[:len(muc_count)], edgecolor="white")
    ax.set_title("Biểu đồ cột ngang – Phân bố mức tiêu thụ điện", fontsize=13, fontweight="bold")
    ax.set_xlabel("Số bản ghi")
    ax.set_ylabel("Mức tiêu thụ")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "03_barh_muc_tieu_thu.png"), dpi=120)
    plt.close()
    print("[3] ✅ Lưu: 03_Phân bố mức tiêu thụ điện.png")

    # ── Biểu đồ 4: Histogram – Phân phối công suất
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(df["Global_active_power"], bins=60, color=COLORS[0],
            edgecolor="white", alpha=0.85)
    mean_val = df["Global_active_power"].mean()
    ax.axvline(mean_val, color="red", linestyle="--", linewidth=1.8, 
                label=f"Trung bình = {mean_val:.2f}")
    ax.set_title("Histogram – Phân phối công suất tiêu thụ", fontsize=13, fontweight="bold")
    ax.set_xlabel("Công suất (kW)")
    ax.set_ylabel("Tần suất")
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "04_histogram_phan_phoi.png"), dpi=120)
    plt.close()
    print("[4] ✅ Lưu: 04_Phân phối công suất tiêu thụ.png")

    # ── Biểu đồ 5: Scatter – Công suất vs Điện áp
    sample = df.sample(min(3000, len(df)), random_state=42)
    fig, ax = plt.subplots(figsize=(8, 5))
    sc = ax.scatter(sample["Voltage"], sample["Global_active_power"],
                    c=sample["Gio"], cmap="viridis", alpha=0.6, s=15)
    plt.colorbar(sc, ax=ax, label="Giờ trong ngày")
    ax.set_title("Scatter – Điện áp vs Công suất (màu = giờ)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Điện áp (V)")
    ax.set_ylabel("Công suất (kW)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "05_scatter_voltage_power.png"), dpi=120)
    plt.close()
    print("[5] ✅ Lưu: 05_Điện áp vs Công suất (màu = giờ).png")

    # ── Biểu đồ 6: Subplot – Tổng hợp 4 chỉ số
    fig, axes = plt.subplots(2, 2, figsize=(13, 8))
    fig.suptitle("Tổng hợp chỉ số theo giờ trong ngày", fontsize=14, fontweight="bold")

    metrics = [
        ("Global_active_power",    "Công suất tác dụng (kW)",    COLORS[0]),
        ("Global_reactive_power",  "Công suất phản kháng (kW)",  COLORS[1]),
        ("Voltage",                "Điện áp (V)",                 COLORS[2]),
        ("Global_intensity",       "Cường độ (A)",                COLORS[3]),
    ]
    for ax, (col, label, color) in zip(axes.flat, metrics):
        tb = df.groupby("Gio")[col].mean()
        ax.plot(tb.index, tb.values, color=color, linewidth=2, marker="o", markersize=4)
        ax.set_title(label, fontsize=11)
        ax.set_xlabel("Giờ")
        ax.set_ylabel(label)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "06_subplot_4_chi_so.png"), dpi=120)
    plt.close()
    print("[6] ✅ Lưu: 06_Tổng hợp chỉ số theo giờ trong ngày.png")

    # ── Biểu đồ 7: Heatmap Pivot – Giờ × Tháng
    fig, ax = plt.subplots(figsize=(12, 7))
    pivot_vals = pivot.values
    im = ax.imshow(pivot_vals, cmap="YlOrRd", aspect="auto")
    plt.colorbar(im, ax=ax, label="Công suất TB (kW)")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([f"T{m}" for m in pivot.columns])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels([f"{h}h" for h in pivot.index])
    ax.set_title("Heatmap – Công suất TB theo Giờ × Tháng", fontsize=13, fontweight="bold")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Giờ")
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot_vals[i, j]
            if not np.isnan(val):
                ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                        fontsize=6.5, color="black")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "07_heatmap_gio_thang.png"), dpi=120)
    plt.close()
    print("[7] ✅ Lưu: 07_Công suất TB theo Giờ × Tháng.png")

if __name__ == "__main__":
    from bai_02_xu_ly_du_lieu import load_data, clean_data, engineering_data
    from bai_03_phan_tich import perform_analysis
    from cau_hinh import OUTPUT_DIR
    import os

    # Đảm bảo thư mục lưu ảnh tồn tại
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Tải và tiền xử lý dữ liệu
    df = load_data()
    df = clean_data(df)
    df = engineering_data(df)
    
    # Phân tích dữ liệu
    analysis_results = perform_analysis(df)
    
    # Vẽ biểu đồ
    create_visualizations(df, analysis_results)
