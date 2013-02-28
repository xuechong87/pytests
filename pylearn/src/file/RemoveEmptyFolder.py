'''
Created on 2013-2-28
check the empty folder & remove
@author: xuechong87
'''
import os

def pathNotNull(pathStr):
    return len(os.listdir(pathStr))>0

def remove(pathStr):
    os.removedirs(pathStr)
    return

def execute(pathStr):
    if pathNotNull(pathStr)==False :
        remove(pathStr)
    return

def iterate(pathStr):
    flag = True
    while flag:
        flag = False
        for f in os.listdir(pathStr):
            fPath = pathStr+ "\\" + f
            if os.path.exists(fPath) and os.path.isdir(fPath) and pathNotNull(fPath):
                iterate(fPath)
            else:
                flag = True
                print(fPath)
                remove(fPath)
    return

if __name__=='__main__':
    ''' flag = 'y'
    while(flag!='n'):
        folderPath = input('输入检查路径')
        try:
            execute(folderPath)
        except:
            print('出错了')
        print('finished!')
        flag=input('按n结束')
    '''
    iterate('F:\\test1')
   
   
    
