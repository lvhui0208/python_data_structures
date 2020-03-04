# ??
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]

# append??
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)

# ??????
def test3():
    list1 = [i for i in range(1000)]


def test4():
    list1 = list(range(1000))

from timeit import Timer

t1 = Timer('test1()','from __main__ import test1')
print('contact',t1.timeit(number=1000),'??')
t2 = Timer("test2()", "from __main__ import test2")
print("append",t2.timeit(number=1000), "??")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "??")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "??")