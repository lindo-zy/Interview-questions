# Interview-questions  


 
***  
1.我做过的笔试题和一些面试经历  
2.面试难度总共为5星，笔试难度总共为5星  
3.基本为python、web方面  

***  
1.寒武纪科技  
面试岗位：python web开发实习生  
面试难度：2星  
笔试难度：2星  

*** 

笔试题：
* 另类乘法,123x45=1x4+1x5+2x4+2x5+3x4+3x5=54  
```python
a = '123'
b = '45'
s = 0
for i in a:
    for j in b:
        s += int(i) * int(j)
print(s)
```
* 给一个长度为奇数的数组,n=[1,3,5,7,1,3,5,7,9],求出里面无重复的元素
```python
方法1:
n = [1, 3, 5, 7, 1, 3, 5, 7, 9]
res = set(n)
for i in list(res):
    if n.count(i) == 1:
        print(i)
 
 方法2:
n = [1, 3, 5, 7, 1, 3, 5, 7, 9]
s=set(n)
for i in s:
    if n.count(i)==1:
        print(i)
```
***
评价：面试的很全面，简历上写的东西全问，还涉及一些算法相关的问题。不过整体难度不大，并且数据结构相关没有涉及。  
***  

2.奇游科技  
面试岗位：python web开发实习生  
面试难度：未进面试  
笔试难度： 4星    

*** 

笔试题：
* 给定列表，统计重复元素个数
```python
n = [1, 2, 3, 1, 2, 2, 4]
a = {}
for i in n:
    if n.count(i) > 1:
        a[i] = n.count(i)
print(len(a))

```
* python实现快排
```python
def partiton(li, a, b):
    x = li[b]
    i = a
    for j in range(a,b): 
        if li[j] < x:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[i], li[b] = li[b], li[i]
    return i

def quickSort(li, a, b):
    if a >= b:
        return
    i = partiton(li, a, b)
    quickSort(li, a, i - 1)
    quickSort(li, i + 1, b)

li = [5, 4, 6, 3, 2, 1]
quickSort(li, 0, len(li) - 1)
print (li)


```
*** 

评价：笔试过去很久，题目搞忘很多。当时是给45分钟，做大概15道题，除了4道编程题其他都是问答题，笔试时感觉难度很大。不过公司在阿里巴巴大楼里面，而且环境很好。有机会再去试一试吧。  

***  

3.悟空找房  
面试岗位：爬虫工程师(实习)  
面试难度：5星  
笔试难度：无笔试  

***

面试内容：  
http协议  
网络报文  
css选择器  
spring mvc中的ioc，aop  
正则表达式  
爬虫业务  
爬虫的反爬  
数据库的操作和优化  
数据库运行原理  
java中接口和抽象类的区别  
设计模式  

*** 

评价：一共有两轮面试，都是技术面试。问的比较深入，比如http协议，数据库运行原理。总体难度和正式找工作差不多。  

***

4.上海数策软件  
面试岗位：爬虫工程师(实习)  
一面难度：2星  
二面难度：4星  
笔试难度：3星  

***  

面试内容：  
range和xrange区别  
logging模块的使用  
常见的Exception  
写出三条git命令  
如何查看函数运行时间  
copy和deecopy的区别  
正则表达式match和search的区别  
如何写单元测试  
一千万条url去重  
三台服务器进行千万级爬虫并发，如何执行  
什么是pep8  
http协议  
   
笔试：  
列表的交集、差集、并集、对称差集
```python
listA = [1, 2, 3, 4, 5]
listB = [3, 4, 5, 6, 7]
#交集的方法
intersectionA=[i for i in listA if i in listB]
print(intersectionA)
intersectionB=list(set(listA).intersection(set(listB)))
print(intersectionB)
intersectionC=list(set(listA)&set(listB))
print(intersectionC)

#并集的方法
unionA=list(set(listA)|set(listB))
print(unionA)
unionB=list(set(listA).union(listB))
print(unionB)

#差集的方法
differenceA=[i for i in  listB if i not in listA]
print(differenceA)
differenceB=list(set(listB)-set(listA))
print(differenceB)
differenceC=list(set(listB).difference(listA))
print(differenceC)

#对称差集的方法
diffA=list(set(listA)^set(listB))
print(diffA)
diffB=list(set(listA).symmetric_difference(listB))
print(diffB)

```
---  

评价：前前后后三轮面试，最后一轮面试有点牵强，需要有千万级分布式爬虫经验。公司还是不错，不过面试水平一般。

---
***
5.成都善读数据



----------
面试内容：
pep8  
赋值,浅拷贝,深拷贝  
线程和进程  
类方法  
装饰器  
liunx  
git命令  
2.7和3.6  
logging,线程安全?  
with,实现  
Pythonic语法  
爬虫的反爬  
硬连接,软连接  
tcp/ip/http  
ip池  
计算密集/iO密集  
range和xrange  


----------
笔试：
```
def foo(a, b=[]):
    for i in range(a):
        b.append(i ** 2)
    print(b)


if __name__ == '__main__':
    foo(3)
    foo(2, [1, 2, 3])
    foo(3)
```
    


----------
6.成都微银合创


----------
面试内容：
无技术面试


----------
笔试：
1.输入一个字母字符串，统计出字符串每个字母的个数，按照字母的ASCII码从大到小排序。以字典形式输出。
```
s = input()
d = {}
for i in s:
    d[i] = s.count(i)
sorted(d)
print(d)
```
2.输入一个数字字符串，每个数字*2后输出，如果*2后大于9，则十位变成#。写出编码函数，和解码函数。
```
def encode_num(s):
    encode_result = ''
    for i in s:
        temp = int(i) * 2
        if temp > 9:
            temp = str(temp).replace('1', '#')
        encode_result += str(temp)
    # print(encode_result)
    return encode_result


def decode_num(encode_result):
    decode_result = ''
    for i in range(len(encode_result)):
        if encode_result[i] == '#':
            decode_result += str((int(encode_result[i + 1]) + 10) // 2)
        if encode_result[i].isalnum() and encode_result[i - 1] != '#':
            decode_result += str(int(encode_result[i]) // 2)
    #print(decode_result)
    return decode_result


if __name__ == '__main__':
    s = input()
    r1 = encode_num(s)
    r2 = decode_num(r1)
    print(r1)
    print(r2)


```

