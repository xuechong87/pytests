'''
Created on 2013-6-3
list tests
@author: xuechong
'''

def test():
    listSearch()
    return

def listSearch():
    '''search in list'''
    print(listSearch.__doc__)
    list_ = ['a','b','c','d','e','a']
    print str(list_.index("a"))
    try:
        print str(list_.index("x"))
    except:
        print('exception when not found\r\nand this still happens in py3.x')
    else:
        print('some thing is really wrong')
        
    list_.remove("c")#remove a obj
    try:
        list_.remove("c")
    except:
        print('will throw ex when no such obj in the list')
        
def listOp():
    li_ = list(range(0,9))
    print (li_)
    li_= [ele*2+ele/3 for ele in li_]
    print li_
    return

if __name__=="__main__":
    print (__doc__)
    test()
    print(str(listOp()))
    
    
    