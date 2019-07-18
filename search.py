"""
二分查找方法训练
"""
# list_为有序数列，key为是要查找的关键值，返回key在数列中索引

def search(list_,key):
    low ,high = 0, len(list_) -1
    while low <=high:
        mid =(low+high)//2
        if list_[mid]<key:
            low = mid +1
        elif list_[mid]>key:
            high =mid - 1
        else:
            return mid




l=[1,2,3,4,5,6,7,8,9,10]
print("key index：",search(l,10))

"""
search.py 二分查找方法训练
"""

# list_为有序数列，key为要查找的关键值,返回key在数列中的索引号
# def search(list_,key):
#     # 第一个数index 最后一个数index
#     low,high = 0,len(list_) - 1
#
#     #　循环每次去除一半内容
#     while low <= high:
#         mid = (low + high) // 2
#         #　取后半部分
#         if list_[mid] < key:
#             low = mid + 1
#         # 取前半部分
#         elif list_[mid] > key:
#             high = mid - 1
#         else:
#             return mid
#
#
# l = [1,2,3,4,5,6,7,8,9,10]
# print("Key index:",search(l,10))
