import numpy as np
from tien_ich import print_section_header

def run_numpy_demo():
    print_section_header("PHẦN 1: NUMPY")

    # 1. Tạo mảng 1D, 2D, 3D
    arr_1d = np.array([4.216, 5.360, 5.374, 5.388, 3.666])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("\n[1] Mảng 1D:", arr_1d)
    print("    Mảng 2D:\n", arr_2d)
    print("    Mảng 3D shape:", arr_3d.shape)

    # 2. Tạo ma trận toàn 0, toàn 1, ma trận đơn vị
    zeros = np.zeros((3, 3))
    ones = np.ones((3, 3))
    identity = np.eye(3)
    print("\n[2] Ma trận toàn 0:\n", zeros)
    print("    Ma trận toàn 1:\n", ones)
    print("    Ma trận đơn vị:\n", identity)

    # 3. Tạo dãy số từ A→B bước C
    day_so = np.arange(0, 24, 0.5)   # giờ trong ngày, bước 0.5h
    print("\n[3] Dãy giờ trong ngày (0 → 24, bước 0.5):", day_so[:8], "...")

    # 4. Tạo ma trận random (mô phỏng mức điện tiêu thụ)
    np.random.seed(42)
    random_power = np.random.uniform(1.0, 6.0, (5, 7))   # 5 tuần x 7 ngày
    print("\n[4] Ma trận random mức điện (5 tuần x 7 ngày):\n", np.round(random_power, 2))

    # 5. Shape, ndim, dtype
    print("\n[5] random_power → shape:", random_power.shape,
          "| ndim:", random_power.ndim, "| dtype:", random_power.dtype)

    # 6. Tổng, trung bình, max, min, std
    print("\n[6] Thống kê ma trận random:")
    print(f"    Tổng   : {random_power.sum():.2f}")
    print(f"    TB     : {random_power.mean():.2f}")
    print(f"    Max    : {random_power.max():.2f}")
    print(f"    Min    : {random_power.min():.2f}")
    print(f"    Std    : {random_power.std():.2f}")

    # 7. Theo hàng (axis=1) / cột (axis=0)
    print("\n[7] Trung bình theo từng tuần (axis=1):", np.round(random_power.mean(axis=1), 2))
    print("    Trung bình theo từng ngày (axis=0) :", np.round(random_power.mean(axis=0), 2))

    # 8. Lấy dòng, cột, phần tử cụ thể
    print("\n[8] Dòng 0:", random_power[0])
    print("    Cột 0  :", random_power[:, 0])
    print("    Phần tử [2,3]:", round(random_power[2, 3], 2))

    # 9. Lọc phần tử thỏa điều kiện
    cao = random_power[random_power > 4.5]
    print("\n[9] Các giá trị điện > 4.5 kW:", np.round(cao, 2))

    # 10. Tìm vị trí phần tử (np.where)
    vi_tri = np.where(random_power > 5.0)
    print("\n[10] Vị trí (hàng, cột) có điện > 5.0 kW:", list(zip(vi_tri[0], vi_tri[1])))

    # 11. Tìm tuần tiêu thụ điện cao nhất (argmax)
    tong_tuan = random_power.sum(axis=1)
    print("\n[11] Tổng điện mỗi tuần:", np.round(tong_tuan, 2))
    print("     Tuần tiêu thụ cao nhất: Tuần", np.argmax(tong_tuan) + 1)

    # 12. Chuẩn hóa Z-score
    z_score = (random_power - random_power.mean()) / random_power.std()
    print("\n[12] Z-score (5 giá trị đầu):", np.round(z_score.flatten()[:5], 4))

if __name__ == "__main__":
    run_numpy_demo()
