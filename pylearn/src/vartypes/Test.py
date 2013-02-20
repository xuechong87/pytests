'''
Created on 2013-2-7
内置数据类型
@author: xuechong
'''

def booleanTest():
    '''bool 可以当做数值对待,但在py3中不推荐这样使用'''
    i = True + True
    print("boolean test1:" + str(i)) 


def integerAndFloat():
    #浮点型精确到小数点后15位'''
    print("1 is int:" + str(isinstance(1, int)))
    print(type(10/5))
    #用/进行运算,不管输入和结果是什么类型,返回的结果总是float型'''
    print(type(3/5))
    #int()函数会直接截取整数位,而不是"floor"'''
    i = int(2.5)
    print("i="+i.__str__())
    #py3只有一种整数类型py2则分int和long'''
    print(type(999999999999999999999999999999999999))
    
    
if __name__ == "__main__":
    print(__doc__)
    booleanTest()
    integerAndFloat()