'''
Created on 2013-2-25
SET 集合
@author: xuechong
'''
def test1():
    set_1 = set()
    print(set_1)
    set_1 = {1, 2, 3, 4, 5}
    print(set_1)
    print(type(set_1))
    
    #可以由列表转换
    list_a = [1,2,2,4]
    set_a = set(list_a)
    print(list_a)
    print(set_a)
    return


#program start
if __name__=='__main__':
    print(__doc__)
    test1()
