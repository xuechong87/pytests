'''
Created on 2013-2-7
布尔上下文环境中的数值
@author: xuechong
'''

def something_is_true(anything):
    if(anything):
        print(str(anything) + "is true")
    else:
        print(str(anything) + "is false")
    return

def tupleTest():
    '''元组在bool上下文的值'''
    print(tupleTest.__doc__)
    print("空元组为" )
    something_is_true(())
    print("至少有一个元素的元组为")
    something_is_true((True,))
    return
if __name__ == '__main__':
    print(__doc__)
    test = something_is_true
    test(1)
    test(0)#0为假
    test(0.0)
    test(0.0000000001)#非0浮点为真
    test('asdasd')
    test(None)#None 为假
    tupleTest()