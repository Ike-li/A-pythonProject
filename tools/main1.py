# 打开文件
file_path = '../username/all_usernames.txt'
output_file_path = '../username/duplicate_usernames_1.txt'

# 用集合记录存在的字符串及其小写形式
existing_strings = set()
existing_lower_strings = set()
ls = []
with open(file_path, 'r') as file:
    for line in file:
        # 移除换行符并获取原始字符串
        original_string = line.strip()

        # 将字符串转换为小写形式
        lower_string = original_string.lower()

        # 检查原始字符串是否存在重复
        if original_string in existing_strings:
            print(f"原始字符串 '{original_string}' 存在重复")
        else:
            existing_strings.add(original_string)

        # 检查小写形式字符串是否存在重复
        if lower_string in existing_lower_strings:
            ls.append(original_string)
            print(f"小写形式字符串 '{lower_string}' 存在重复，对应的原始字符串为: '{original_string}'")
        else:
            existing_lower_strings.add(lower_string)

print(len(ls))
# 将重复的原始字符串写入输出文件
with open(output_file_path, 'w') as output_file:
    for duplicate_string in ls:
        output_file.write(f"{duplicate_string}\n")

print(f"重复的原始字符串已写入文件 '{output_file_path}'")