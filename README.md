# Interview-questions
  
1.我做过的面试题  
2.面试难度总共为5星  
3.基本为python、web方面
---
1.寒武纪科技  
面试难度：2星
***
面试题：
* 另类乘法,123*45=1*4+1*5+2*4+2*5+3*4+3*5=54  
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
