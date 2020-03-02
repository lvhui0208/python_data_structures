def list1():
    lsit1 = []
    for i in range(1000):
        list1 = list1 + [i]


#append方式
def test2():
    list1 = []
    for i in range(1000):
        list1.append(i)

def test3():
    list1 = [i  for i in range(1000)]:




def test4():
    list1 = list(range(1000))


import timeit

t1 = timeit.Timer('test1()','form_main_import test1')
paint(t1.timeit(number = 1000))

