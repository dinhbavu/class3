def xep_loai(x):
    """
    Xếp loại mức tiêu thụ điện dựa trên công suất Global_active_power.
    """
    if x >= 5:
        return "Rất cao"
    elif x >= 3:
        return "Cao"
    elif x >= 1:
        return "Trung bình"
    else:
        return "Thấp"

def print_section_header(title):
    """
    In tiêu đề cho mỗi phần phân tích.
    """
    print("\n" + "═" * 60)
    print(f"  {title}")
    print("═" * 60)
