'''
Created on 2013-2-25
元组:元素是不可变的列表
@author: Administrator
'''
from platform import system
import time
def test1():
    '''
    元组的定义方式与列表相同,对元组切片可以得到新的元组
    与列表主要不同是元组不能修改
    *元组的速度比列表快??0,0
    
    '''
    print(test1.__doc__)
    a_tuple = ('a','b','c','d')
    a_list = ['a','b','c','d']
    
    t1 = time.time()  
    loopTest(a_tuple)
    print("元组" + str(time.time()-t1))    
    t2 = time.time()  
    loopTest(a_list)
    print("列表" + str(time.time()-t2))  
    
    return
def loopTest(collec):
    counts = 10**7
    for i in range(1,counts):
        for j in range(0,len(collec)-1):
            v = collec[j]
    
def test2():
    '''
    *元组和列表可以互相转换
    '''
    print(test2.__doc__)
    a_tuple = ('a','b')
    list1 = list(a_tuple)
    print(list1)
    return

#program start
if __name__=='__main__':
    print(__doc__)
    test1()
    test2()