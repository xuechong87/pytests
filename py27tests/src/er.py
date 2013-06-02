'''
Created on 2013-6-2

@author: xuechong
'''

    
def dictionaryTest():
    '''
    dictionary tests
    '''
    dictionary = {"server":"mpilgrim","database":"master"}
    print dictionary["server"]
    print dictionary["database"]
    dictionary["uid"]="sa"#add 
    
    print dictionary["uid"]
    dictionary["Uid"]="sss"#case sensitive
    print dictionary["Uid"]
    
    print dictionary
    del dictionary["Uid"]#delete
    print dictionary
        
    dictionary.clear()
    print dictionary
        
if __name__=="__main__":
    print dictionaryTest.__doc__
    dictionaryTest()
    
    
    
    
    