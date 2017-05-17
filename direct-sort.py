#-*- coding:utf8 -*-
def direct_sort():
    a=[60,71,49,11,82,49,3,66]
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        #print("i:%d, key is: %d" % (i,key))
        while j>0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
            #print(a)
        a[j+1]=key
        #print(a)
    print(a)

"""
算法思路：
从第二个元素开始，与第一个元素组合，进行排序
从第三个元素开始，与第一个、第二个元素组合，进行排序
以此类推
第k个元素，与之前的k-1个元素（已经排序好了的序列）组合进行排序。
"""
def direct_sort_my():
    a=[60,71,49,11,82,49,3,66]
    n=len(a)
    for i in range(1,n):
        for j in range(i):
            if a[j]>a[i]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
    print(a)

direct_sort()
direct_sort_my()