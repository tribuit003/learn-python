file_object = open('test.txt')

data = file_object.read(-1)
print(data)

file_object.close()

# Chú ý
# Thao tác với file chú ý tới đường dẫn (path)
# help()

# r, r+, w, w+, a, a+

# with (đây là cụm lệnh with-block)

