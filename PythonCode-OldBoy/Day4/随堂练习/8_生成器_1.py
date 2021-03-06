# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 为什么要使用生成器？

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 生成器跟列表的区别？
#
# 只有在调用时才会生成相应的数据，调用到哪一步就产生哪一步的数据

# 生成器取具体的值得时候，只记得当前的位置，不能往回退，不能跳着走
# 只有一个__next__方法，在Python2.7里面是next()

n = (x * x for x in range(10))
print(n) # 并没有生成数据，只是指向了一个内存地址

print(n.__next__()) # 取第一个值
print(n.__next__()) # 取第二个值
#n[10] # 无法打印结果，因为还没有生成列表
# 用循环一次性取其他值
for i in n:
    print(i)