# my_set1={1,1,2,3,4}
# my_set2={3,4,5,6,7}
# # my_set3=my_set1.difference(my_set2)
# # print(my_set3)

# # my_set1.difference_update(my_set2)
# # print(f"集合1{my_set1},集合2{my_set2}")

# # my_set3=my_set1.union(my_set2)
# # print(my_set3)

# # print(len(my_set1))

# for a in my_set1:
#     print(f"集合元素：{a}")

my_list=['黑马程序员','传智教育','黑马程序员','传智教育','itheima','itcast','itheima','itcast','best']
my_set=set()
for a in my_list:
    my_set.add(a)
print(f'有列表{my_list}\n存入集合后结果{my_set}')
