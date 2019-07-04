# encoding=UTF-8
list1 = ['A', 'B', 'C']
list2 = list1;
list3 = list1[:]  # 複製裡面的內容
list4 = list(list1)  # 複製裡面的內容
print list1, list2, list3, list4
print hex(id(list1)), hex(id(list2)), hex(id(list3)), hex(id(list4))  # 12指向相同的值 34指向!不同的值
list1[0] = 'a'
list2[0] = 'b'
print list1, list2, list3, list4
