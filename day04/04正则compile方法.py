import re
str_123 = '"https://m.douban./26930056/", "year": "2018"'
a = re.compile("\d")  #先对正则表达式编码，并储存
print(a)  #re.compile('\\d')
b = a.findall(str_123)  #这里的方法，只需传入需正则的字符串就可以
print(b)  #['2', '6', '9', '3', '0', '0', '5', '6', '2', '0', '1', '8']

ret = re.findall(r"hg(.*)bcd","hg\n94ssbcd",re.DOTALL)  #re.DOTALL作用使.匹配包括换行\n在内的所有字符
print(ret) #['\n94ss']     (.....)  提取匹配括号内的表达式，也表示一个组



#!/usr/bin/python
import re
string = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', string)

print (matchObj.group())  #Cats are smarter than dogs
print (matchObj.group(1))  #Cats
print (matchObj.group(2))   #smarter
print ( matchObj.groups())  #('Cats', 'smarter')
"""
正则表达式：r'(.*) are (.*?) .*'
解析:
    首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。
    但是这个字符串里没有反斜杠，所以这个 r 可有可无。
    
     (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
     (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
     后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
    matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
    
    matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
    
    matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的

    因为只有匹配结果中只有两组，所以如果填 3 时会报错。

"""