'''
Created on 2013-6-3

@author: xuechong
'''
def objtests():
    obj_a = "obja";
    obj_b = obj_a
    obj_b.upper()
    print obj_b
    diff(obj_a,obj_b)
    obj_b = "obj_b"
    diff(obj_a,obj_b)
    return

def diff(a,b):
    print "diff"
    print(id(a))# For CPython, id(x) is the memory address where x is stored.
    print(id(b))
    print a is b
    
    
if __name__=="__main__":
    objtests()