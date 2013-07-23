'''
Created on 2013-7-23

@author: xuechong
'''

import os
import re

dest_path = "F:/tests";
regexp = "\S*.txt";

def sat(path):
    mat = lambda x : re.compile(regexp).match(x.replace(' ','').lower())
    for _path in os.listdir(path):
        _path = str(_path)
        
        if mat(_path):
            print(_path + "mat")
        else:
            print(_path)
        
            
if __name__ == '__main__':
    sat(dest_path)