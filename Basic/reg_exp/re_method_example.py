import re


s = '''first line
second line
third line'''

print('test compile \n')
regex = re.compile(".+")
print(type(regex))
print(regex.findall(s))
print(regex.search(s).group())

print('test escape \n')
s = ".+\d123"
regex_str = re.escape(".+\d123")
print(regex_str)  # 转义后的字符
print(re.findall(regex_str, s))

print('test findall \n')
s = '''first line
second line
third line'''
regex = re.compile("\w+")
print(regex.findall(s))
print(re.findall("\w+", s))

print('test finditer \n')
print(regex.finditer(s))
for i in regex.finditer(s):
    print(i)

print('test match \n')
regex = re.compile("\w+")
m = regex.match(s)
print(m)
print(m.group())

regex = re.compile("^i\w+")
print(regex.match(s))

print('test search \n')
print(re.match('i\w+', s))
print(re.search('i\w+', s))
print(re.search('i\w+', s).group())

print('test split \n')
s = '''first 111 line
second 222 line
third 333 line'''
print(re.split('\d+', s))
print(re.split('\.+', s, 1))
print(re.split('\d+', s, 1))


print('test sub \n')
s = "the sum of 7 and 9 is [7+9]."
# 基本用法 将目标替换为固定字符串
print(re.sub('\[7\+9\]', '16', s))
# 高级用法 1 使用前面匹配的到的内容 \1 代表 pattern 中捕获到的第一个分组的内容
print(re.sub('\[(7)\+(9)\]', r'\2\1', s))


# 高级用法 2 使用函数型 repl 参数, 处理匹配到的 SRE_Match 对象
def replacement(m):
    p_str = m.group()
    if p_str == '7':
        return '77'
    if p_str == '9':
        return '99'
    return ''


print(re.sub('\d', replacement, s))

