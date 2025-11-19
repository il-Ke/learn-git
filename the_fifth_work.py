list1=[1,2,3,4,5,3,2] #列表1
list2=[4,5,6,7,8,5] #列表2
set1=set(list1) #转化为集合
set2=set(list2)
inter_set=set1.intersection(set2) #交集
print(inter_set)
union_set=set1.union(set2) #并集
print(union_set)