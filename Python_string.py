print("hello world")

#用\进行转义
print("let\'s go")
print("\"hello world\" she said")

#用+号拼接字符串
x="hello,"
y="world"
print(x+y)

#字符串两种输出方式
#str形式：不忽略格式（str是个类）
print(str("hello,\nworld"))
#repr形式：忽略格式及转义字符（repr是个函数）
print(repr("hello,\nworld"))