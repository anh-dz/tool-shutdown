print("Tool hẹn giờ tắt máy")
import os
h,m,s = int(input("Nhập giờ: ")), int(input("Nhập phút: ")), int(input("Nhập giây: "))
s = s+h*60*60+m*60
while True:
	t = input("Chọn chế độ (shutdown = s, restart = r): ")
	if t == 's' or t == 'r': break

print("Bắt đầu hẹn giờ")
os.system(f"shutdown -{t} -t {s}")
print("Gõ lệnh 'shutdown -a' để hủy tắt máy")