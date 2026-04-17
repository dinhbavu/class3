import pandas as pd
from cau_hinh import DATA_PATH
from tien_ich import xep_loai, print_section_header

def load_data(nrows=500_000):
    print_section_header("PHẦN 2: PANDAS - ĐỌC DỮ LIỆU")
    print(f"\n[1] Đọc file gốc ({nrows:,} dòng)...")
    df = pd.read_csv(
        DATA_PATH,
        sep=";",
        nrows=nrows,
        na_values=["?"],
        low_memory=False
    )
    print("    ✅ Đọc xong! Shape:", df.shape)
    return df

def clean_data(df):
    print_section_header("PHẦN 3: LÀM SẠCH DỮ LIỆU")
    
    # 1. Kiểm tra dữ liệu thiếu
    print("\n[1] Dữ liệu thiếu theo cột:\n", df.isnull().sum())

    # 2. Điền giá trị thiếu bằng trung bình
    cols_num = ["Global_active_power","Global_reactive_power",
                "Voltage","Global_intensity",
                "Sub_metering_1","Sub_metering_2","Sub_metering_3"]
    for col in cols_num:
        df[col] = df[col].fillna(df[col].mean())
    print("\n[2] ✅ Đã điền giá trị thiếu bằng trung bình")

    # 3. Xóa dòng thiếu (cột Date / Time)
    truoc = len(df)
    df.dropna(subset=["Date", "Time"], inplace=True)
    print(f"\n[3] Xóa dòng thiếu Date/Time: {truoc - len(df)} dòng bị xóa")

    # 4. Kiểm tra & xóa dữ liệu trùng
    truoc = len(df)
    df.drop_duplicates(inplace=True)
    print(f"\n[4] Dữ liệu trùng đã xóa: {truoc - len(df)} dòng")

    # 5. Ép kiểu sang datetime
    df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"],
                                    format="%d/%m/%Y %H:%M:%S")
    print("\n[5] ✅ Cột Datetime:", df["Datetime"].dtype)

    # 6. Chuẩn hóa chuỗi
    df["Date"] = df["Date"].str.strip().str.title()
    print("\n[6] ✅ Đã chuẩn hóa cột Date (strip + title)")

    return df

def engineering_data(df):
    print_section_header("PHẦN 4: FEATURE ENGINEERING")

    # 1. Tạo cột mới
    df["Tong_sub_metering"] = df["Sub_metering_1"] + df["Sub_metering_2"] + df["Sub_metering_3"]
    df["Gio"]   = df["Datetime"].dt.hour
    df["Ngay"]  = df["Datetime"].dt.date
    df["Thang"] = df["Datetime"].dt.month
    df["Nam"]   = df["Datetime"].dt.year
    df["Thu"]   = df["Datetime"].dt.day_name()
    print("\n[1] ✅ Đã tạo cột: Tong_sub_metering, Gio, Ngay, Thang, Nam, Thu")

    # 2. Chuẩn hóa Min-Max
    col = "Global_active_power"
    df["GAP_minmax"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    print("\n[2] ✅ Đã chuẩn hóa Min-Max cho Global_active_power")

    # 3. Xếp loại
    df["Muc_tieu_thu"] = df["Global_active_power"].apply(xep_loai)
    print("\n[3] Phân phối mức tiêu thụ:\n", df["Muc_tieu_thu"].value_counts())

    return df

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    df = engineering_data(df)
    print("\n✅ Hoàn thành xử lý dữ liệu!")
