'''
乱序字符串是指一个字符串知识另一字符串的重新排序
前提：字符串有26个小写字母字符集合组成，长度相同
比如： python  typhon   head   deah
目的：
    写一个布尔函数（返回布尔值的函数）
    solutions1('abcd','dbca')

'''

#穷举法：排除。原因：如果字符串过长，20个长度

#检查  第一个字符串是不是出现在第二个字符串中 


def solutions1(s1,s2):
    a_lsit = list(s2)
    
    
    pos1 = 0
    flag = True

    while flag and pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        
        
        if found:
            a_lsit[pos2] = None
            pos1 = pos1 +1 
        else:
            flag = True
    
    return flag


print(solutions1('abcd','dbca'))
print(solutions1('abcd','defa'))








