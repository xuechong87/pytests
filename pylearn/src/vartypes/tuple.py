'''
Created on 2013-3-27
元组
@author: xuechong
'''

def setData():
    '''使用元组可以一次给多个变量赋值'''
    print(setData.__doc__)
    v = ('a',2,True)
    (x,y,z) = v
    print(x)
    print(y)
    print(z)
    return
def useRange():
    '''可使用内建range()函数快速赋值'''
    (a,b,c) = range(3)
    print(a)
    print(b)
    print(c)
    return

if __name__ == "__main__":
    print(__doc__)
    setData()
    useRange()
