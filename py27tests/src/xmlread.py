'''
Created on 2013-6-9
read xml
@author: Administrator
'''
from xml.etree import ElementTree

xmlPath = "F:\\weixin.xml";

class TextMsg:
    ToUserName=''
    FromUserName=''
    CreateTime=0
    MsgType=''
    Content=''
    MsgId=0
    

def getXml(path):
    msg = TextMsg()
    xmlContent = open(path).read()
    root = ElementTree.fromstring(xmlContent)
    _nodes = root.getiterator("xml")
    help(_nodes)
    for node in _nodes:
        help(node)
    return msg
if __name__ == "__main__":
    getXml(xmlPath)
    