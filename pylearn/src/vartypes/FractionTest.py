'''
Created on 2013-2-7
定义分数
@author: xuechong
'''
import fractions
import math

def fracTest():
    x = fractions.Fraction(1,3);
    print(x)#result is  1/3
    x = x*2
    print(x)#result is  2/3
    x = None
    x= fractions.Fraction(6/4)#会自动约分
    print(x)#所以结果为3/2
    try:
        x = fractions.Fraction(1/0)#0不能为分母
    except Exception:
        print('0不能为分母')
        
def sincos():
    x = math.sin(10)
    print(x)
    print(math.pi)#π
    return

if __name__ == "__main__":
    print(__doc__)
    fracTest()
    sincos()
    