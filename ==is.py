'''
is和==这两种运算符区别之前，
在 Python 中一切都是对象，包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。

is 同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同，是否为同一个实例对象，是否指向同一个内存地址
== 比较操作符，用来比较判断两个对象的value(值)是否相等。默认会调用对象的__eq__()方法。 
'''

'''
在 Python 的交互解释器中，把可能频繁使用的整数对象规定在范围 [-5, 256] 之间，当它们创建好后就会被缓存下来。但凡是需要再用到它们时，就会从缓存中取，而不是重新创建对象。
'''
# TODO 发现pycharm vscode都不能正常输出 is 的正确结果
a = -5
b = -5
print(id(a))
print(id(b))
print(a is b)

a = -6
b = -6
print(id(a))
print(id(b))
print(a is b)

a = 25787456
b = a
print(id(a))
print(id(b))
print(a is b)

a = (1, 2, 3)
b = (1, 2, 3)
print(id(a))
print(id(b))
print(a is b)

print("python中可变对象")
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)

# a = {'cheese': 1, 'zh': 2}
# b = {'cheese': 1, 'zh': 2}
# print(id(a))
# print(id(b))
# print(a is b)

# a = set([1, 2, 3])
# b = set([1, 2, 3])
# print(id(a))
# print(id(b))
# print(a is b)
# # python集合是可变且无序的数据类型
# a.add(100)
# print(a)
