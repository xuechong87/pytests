'''
Created on 2013-7-23

@author: xuechong
'''

import os
import re


def execute(path,origin,replacement,regexp="^\S*.txt$"):
    path = os.path.abspath(path)
    mat = lambda x : re.compile(regexp).match(x.replace(' ','').lower())
    for _path in os.listdir(path):
        _path = str(_path)
        absPath = path  + os.path.sep + _path
        
        if mat(_path):
            replaceStr(absPath,origin,replacement)
            
        if os.path.isdir(absPath):
            execute(absPath,regexp)
        
def replaceStr(filePath,origin,replacement):
    file_ = os.open(filePath, "r+",-1,"utf-8")
    file_.seek(origin)
    file_.write(replacement)
    file_.flush()
    file_.close()
    
if __name__ == '__main__':
#    help(os.open)
#    dest_path = str(input("folder"))
#    regexp = "^\S*." + str(input("filetype")) + "$"
#    origin = str(input("origin"))
#    replace = str(input("replacemnt"))
#    execute(path=dest_path,
#            regexp=regexp,
#            origin=origin,
#            replacement=replace)
    file_ = open("F:/tests/asdasd.txt","r+",-1,"utf-8")
    file_.write(re.sub('cccd', 'python', file_.read()))
    file_.flush()
    file_.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass