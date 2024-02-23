# 打开原始文件进行读取
with open('all_usernames.txt', 'r') as infile:
    # 创建一个新文件用于写入包含大写字母的行
    with open('uppercase_usernames.txt', 'w') as outfile:
        # 逐行读取原始文件
        for line in infile:
            # 检查当前行是否包含大写字母
            if any(char.isupper() for char in line):
                # 如果包含大写字母，则将该行写入新文件
                outfile.write(line)
