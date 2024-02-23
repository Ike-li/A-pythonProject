# 打开文件
with open('username_identifier.txt', 'r') as file:
    # 读取文件的所有行
    lines = file.readlines()

# 统计行数
num_lines = len(lines)
print("文件中的条数为:", num_lines)
