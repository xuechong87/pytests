'''
Created on 2013-6-9
read xml
@author: Administrator
'''
from xml.etree import ElementTree

xmlPath = "F:\\weixin.xml";

class TextMsg:
    def __init__(self,nodeXML):
        for node in nodeXML.getchildren():
            setattr(self, node.tag, node.text)
            
    ToUserName=''
    FromUserName=''
    CreateTime=0
    MsgType=''
    Content=''
    MsgId=0

def getXml(path):
    xmlContent = open(path).read()
    root = ElementTree.fromstring(xmlContent)
    _nodes = root.getiterator("xml")
    return TextMsg(_nodes.pop())


if __name__ == "__main__":
    getXml(xmlPath).desc()
    