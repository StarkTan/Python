import re


s = 'hello World!'
# re.I 忽略大小写
regex = re.compile("hello world!", re.I)
print(regex.match(s).group())
# (?i)前缀忽略大小写
regex = re.compile("(?#注释)(?i)hello world!")
print(regex.match(s).group())


s = '''first line
second line
third line'''
#  多行模式
regex_start = re.compile("^\w+")
print(regex_start.findall(s))

regex_start_m = re.compile("^\w+", re.M)
print(regex_start_m.findall(s))

regex_end = re.compile("\w+$")
print(regex_end.findall(s))

regex_end = re.compile("\w+$", re.M)
print(regex_end.findall(s))

# DOTALL 模式
regex = re.compile(".+")
print(regex.findall(s))

regex_dotall = re.compile(".+", re.S)
print(regex_dotall.findall(s))

# 冗余模式 下面两个正则表示式没有区别
email_regex = re.compile("[\w+\.]+@[a-zA-Z\d]+\.(com|cn)")

email_regex = re.compile("""[\w+\.]+  # 匹配@符前的部分
                            @  # @符
                            [a-zA-Z\d]+  # 邮箱类别
                            \.(com|cn)   # 邮箱后缀  """, re.X)
