'''
Created on 2013-3-27
集合
集合是无序的
@author: xuechong
'''
def createSets():
    '''创建方式'''
    #可以从列表中创建集合
    l = [1,2,3,4]
    set1 = set(l)
    print(str(set1))
    return

def addValue():
    '''像集合中添加数据'''
    set_a = set()
    set_a.add('1')
    print(set_a)
    
    set_b = {1,2,3}
    set_b.update({4,5,6})#update函数只接受一个集合作为参数
    print(set_b)
    return

def delteValue():
    '''从集合中删除数据'''
    set_a = {1}
    set_a.discard(1)
    set_a.discard(1)#discard删除一个不存在的值时不会报错
    print(set_a)
    #set_a.remove(1)#remove不存在的值会引发Key Error
    set_a.add(1)
    print(set_a.pop())#pop推出一个值如果集合已经为空的时候会报错
    print(set_a)
    set_a.add(1)
    set_a.clear()#清空等价于set_a = set()
    
    return

if __name__ == "__main__":
    print(__doc__)
    a = {'a','b'}
    print(str(type(a)))
    createSets()
    addValue()
    delteValue()