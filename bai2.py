# Nhập thời gian bắt đầu
a0, b0, c0 = map(int, input().split())

# Nhập thời gian kết thúc
a1, b1, c1 = map(int, input().split())

# Tính thời gian bắt đầu và kết thúc tính theo giây từ đầu ngày
start_seconds = a0 * 3600 + b0 * 60 + c0
end_seconds = a1 * 3600 + b1 * 60 + c1

# Tính thời gian chạy chương trình
if end_seconds >= start_seconds:
    elapsed_seconds = end_seconds - start_seconds
else:
    elapsed_seconds = (24 * 3600 - start_seconds) + end_seconds

# In kết quả
print("Thời gian thực hiện chương trình:", elapsed_seconds)
