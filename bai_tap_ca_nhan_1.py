from tkinter import *
window = Tk()
window.title("GUI Python")
# Dòng này nhập toàn bộ nội dung của thư viện tkinter, giúp bạn tạo giao diện người dùng đồ họa (GUI).
# Tạo cửa sổ GUI

def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
# Hàm from_kg() được gọi khi người dùng nhấn nút "Convert". Nó thực hiện các phép tính để chuyển đổi từ kilogram sang gram, pound, và ounce.
# e2_value.get() lấy giá trị từ ô nhập liệu, sau đó chuyển thành kiểu số float.
# Sau đó, khối lượng được nhân với các hằng số tương ứng để tính ra giá trị gram, pound, và ounce.
# t1.delete("1.0",END) xóa mọi dữ liệu hiện có trong Text widget đầu tiên.
# t1.insert(END, gram) chèn kết quả chuyển đổi sang gram vào Text widget đầu tiên.
# Tương tự, giá trị pound và ounce được chèn vào các widget t2 và t3.


e1 = Label(window, text="Nhập số cân nặng (kg):")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
# StringVar() là biến được liên kết với Entry widget để lưu trữ giá trị người dùng nhập vào.
# Entry là ô nhập liệu nơi người dùng sẽ nhập khối lượng tính bằng kilogram.

e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
# Label là các nhãn văn bản hiển thị trên cửa sổ để mô tả các thành phần.
# e1 hiển thị thông báo hướng dẫn người dùng nhập khối lượng tính bằng kilogram.
# e3, e4, và e5 hiển thị các đơn vị chuyển đổi tương ứng là Gram, Pound, và Ounce.


t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
# Text là widget nơi kết quả chuyển đổi sẽ được hiển thị. Mỗi Text có chiều cao 5 dòng và chiều rộng 30 ký tự.

b1 = Button(window, text="Convert", command=from_kg)
# Button tạo ra một nút bấm có nhãn là "Convert". Khi nút này được nhấn, hàm from_kg() sẽ được gọi để thực hiện chuyển đổi đơn vị.

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)
# grid() sắp xếp các widget theo dạng bảng (grid), với các hàng và cột.
# Ví dụ: e1.grid(row=0, column=0) đặt nhãn e1 ở dòng 0 và cột 0.
# Các thành phần khác như Entry, Text, và Button cũng được sắp xếp theo lưới.

window.mainloop()
# mainloop() bắt đầu vòng lặp chính của ứng dụng, giúp cửa sổ GUI hiển thị và tương tác với người dùng.
# Mọi sự kiện như nhấn nút hay nhập liệu sẽ được xử lý trong vòng lặp này.