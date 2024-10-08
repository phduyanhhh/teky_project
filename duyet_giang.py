number_student = int(input("Số học sinh của lớp: "))
gioi = kha = trung_binh = 0
for i in range(1, number_student+1):
    print("----------")
    name = str(input(f"Nhập tên học sinh thứ {i}: "))
    toan = float(input("- Nhập điểm toán: "))
    ly = float(input("- Nhập điểm lý: "))
    hoa = float(input("- Nhập điểm hóa: "))
    diem_trung_binh = (toan + ly + hoa) / 3
    print(f"Điểm trung bình của {name} là: {diem_trung_binh}")
    if (diem_trung_binh >= 8):
        gioi += 1
        print(f"{name} xuất sắc thật")
    elif (diem_trung_binh >= 5.5):
        kha += 1
        print(f"{name} làm tốt lắm")
    else:
        trung_binh += 1
        print(f"{name} cố lênn")
print("----------")
print(f"Có {gioi} học sinh giỏi")
print(f"Có {kha} học sinh khá")
print(f"Có {trung_binh} học sinh trung bình")







