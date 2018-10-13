list1 = dir(list)
list2 = dir(tuple)
print('关于列表：')
for i in list1:
    if(i in list2):
        print(i,"为列表与元组通用")
    else:
        print(i,"为列表特有")
print('关于元组')
for i in list2:
    if(i not in list1):
        print(i,"为元组特有的函数")
