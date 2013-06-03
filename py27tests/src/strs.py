'''
Created on 2013-6-3
string tests
@author: xuechong
'''

def stringtests():
    print ";".join([str(i) for i in list(range(0,9))])#a non str object can not be 'join'
    
    return


if __name__=="__main__":
    print(__doc__)
    stringtests()