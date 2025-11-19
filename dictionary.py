d={
    "张": 99,
    "李": 77,
    "王": 66,
    "赵": 55
} #建立字典
d["刘"]=60 #添加
d["李"]=88 #修改
del d["王"] #删除
for name, score in d.items():
    print(f"     {name}：{score}分") #遍历