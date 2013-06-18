'''
Created on 2013-6-9
read xml
@author: Administrator
'''
from xml.etree import ElementTree

class TextMsg:
    
    ToUserName=''
    FromUserName=''
    CreateTime=0
    MsgType=''
    Content=''
    MsgId=0
    
    def __init__(self,xmlContent):
        '''
        xmlContent the str content of the xml
        '''
        root = ElementTree.fromstring(xmlContent)
        _nodes = root.getiterator("xml")
        for node in _nodes.pop().getchildren():
            setattr(self, node.tag, node.text)
            
xmlPath = "F:\\weixin.xml";

def getXml(path):
    xmlContent = open(path).read()
    return TextMsg(xmlContent)

if __name__ == "__main__":
    getXml(xmlPath).desc()
    