'''
Created on 2013-6-17
@author: Administrator
'''
import httplib

def searchMoeGirl(keyWord):
    conn = httplib.HTTPConnection('zh.moegirl.org')
    requestUrl = str.format("/?action=opensearch&search=%s&format=xml&limit=10&namespace=0"%keyWord.encode("utf-8"))
    conn.request("POST", requestUrl)
    print requestUrl
    result = conn.getresponse().read()
    return result


if __name__ == "__main__":
#    conn = httplib.HTTPConnection('open.t.qq.com')
#    conn.request("GET","/api/statuses/user_timeline?format=xml&pageflag=0&pagetime=0&reqnum=20&lastid=0&name=xuechong87&fopenid=&type=0&contenttype=0&oauth_consumer_key=xx&access_token=xx&clientip=xx&oauth_version=2.a&scope=all")
#    res = conn.getresponse()
#    print res.read()
    print searchMoeGirl(open("F:\\search.txt").read())