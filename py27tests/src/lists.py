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
        print('exception when not found\r\n and this still happens in py3.x')
    

if __name__=="__main__":
    print (__doc__)
    test()