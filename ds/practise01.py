'''
问题描述：使用函数，求前n个整数的和 
'''
import time

def sumOfN(n):
    start_time = time.time()
    sum = 0
    for i in range(n+1):
        sum = sum + i
    end_time = time.time()
    return sum,end_time-start_time
# print(sumOfN(10000))

for i in range(2):
    print('计算结果是%d需要%10.7f秒'%sumOfN(10000000))


#高斯函数

def sumOfN2(n):
    return (n*(n+1))/2


start_time = time.time()
print(sumOfN2(100000000000))
end_time = time.time()
print(end_time-start_time)





# def foo(lala):
#     a = 0
#     for b in range(1,lala+1):
#         c = b 
#         a = a + c
#     return a
# print(foo(10))
