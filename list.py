one_list=[10,'www',True] #建立列表
print("索引为0的元素：", one_list[0]) #查询第一个元素
one_list[0]=1 #修改第一个元素
one_list.insert(1,2) #在索引1的位置插入2
deleted_val=one_list.pop(0) #删除索引1的元素
one_list.append(10) #添加元素10
print(one_list)
