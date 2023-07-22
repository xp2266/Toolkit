# -*- coding: utf-8 -*-
import os
import re

# 列出当前目录下的所有文件
for filename in os.listdir('.'):
    # 使用更精确的正则表达式匹配集数
    match = re.search(r'(第)(\d+)(集)', filename)
    if match:
        # 格式化集数为4位数字
        new_num = '{:04d}'.format(int(match.group(2)))
        # 使用一个临时标记替换旧的集数
        temp_filename = re.sub(r'(第)(\d+)(集)', r'\1TEMP\3', filename, count=1)
        # 生成新的文件名，替换临时标记为新的集数
        new_filename = temp_filename.replace('TEMP', new_num)
        # print(new_num, temp_filename, new_filename)
        try:
            # 在控制台打印旧的和新的文件名
            print(f'Renaming "{filename}" to "{new_filename}"')
            # 在硬盘上重命名文件
            os.rename(filename, new_filename)
        except Exception as e:
            print(f"Failed to rename '{filename}' to '{new_filename}'. Error: {str(e)}")
