# 创建一个字典来跟踪已经出现过的行
seen = {}
# 记录重复行数
duplicate_count = 0

# 打开文件并逐行读取
with open('all_usernames.txt', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        # 将每一行都转换为小写形式
        lowercase_line = line.strip().lower()

        # 检查是否已经出现过这一行
        if lowercase_line in seen:
            print(f"重复的行 {lowercase_line} 在行号 {seen[lowercase_line]} 和 {line_num} 中出现")
            duplicate_count += 1
        else:
            # 记录该行出现的行号
            seen[lowercase_line] = line_num

print(f"总共有 {duplicate_count} 行重复")
