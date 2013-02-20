'''
Created on 2013-2-7

@author: xuechong
'''

def function1():
    '''return str : function1'''
    return 'function1'

def docStrTest():
    print(function1.__doc__)

if __name__ == '__main__':
    docStrTest()