'''
Created on 2013-2-7
列表
@author: xuechong
'''
def listIndex():
    '''访问索引'''
    print(listIndex.__doc__)
    list_1 = ['a','b',3]
    for i in list_1:
        print(i)
    #负值索引可以从列表的尾部向前计数访问元素
    print(list_1[-1])#得到3 任何非空列表的最后一个元素的索引都为-1 
    print(list_1[-2])#得到b
    return

def listCut():
    '''列表切片'''
    print(listCut.__doc__)
    list_ = ['a','b',3,4,5,6,7,8]
    x = list_[1:3]#包含起始索引但不包含结束索引
    print(x)
    print(list_[2:-1])
    print(list_[:2])
    print(list_[3:])
    print(list_[:])#复制了一个元素值相同的新列表 但和之前的列表不是一个对象
    return

def listAdd():
    '''向列表中添加元素'''
    print(listAdd.__doc__)
    list_ = [1]
    class Listx:
        def dox(self):#return a copy of the origin list
            return list_[:]
    
    x =list_
    x = x + [2,3]#方法1 这种方法会创建一个新的引用
    print(x)
    print(list_)#原数组不变
    
    x =Listx.dox(None)
    x.append(2)#方法2
    x.append([3,4])#这种操作会把[3,4]作为一个元素追加到列表中
    print(x)
    
    x =Listx.dox(None)
    x.extend([2,3,4])#方法3 只接受列表类型的参数
    try:
        x.extend(5)
    except:
        print('extend方法只接受列表类型的参数')
    print(x)
    
    x = Listx.dox(None)
    x.insert(0, 0)
    print(x)
    
    x.insert(4,4)#不会报错
    print(x)
    try:
        print(x[4])
    except :
        print("但是索引没有增加到4")
    return

def listSearch():
    '''在列表中检索数据'''
    print(listSearch.__doc__)
    list_ = ['a','b','c','d','e','a']
    # TODO
    
    return
#program start
if __name__=='__main__':
    print(__doc__)
    listIndex()
    listCut()
    listAdd()