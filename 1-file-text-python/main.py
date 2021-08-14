# mở file

with open("file.txt", encoding='utf-8') as f:
    # f.write("Bùi Văn Trí")
    data = f.read()
    print(data)