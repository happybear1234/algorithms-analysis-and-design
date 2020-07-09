# 二分查找(递归)
def binary_search(a, x, left, right):
    if left <= right:#递归条件
        mid = (right + left) // 2
        if a[mid] < x:
            return binary_search(a, x, mid + 1, right)
        elif a[mid] > x:
            return binary_search(a, x, left, mid - 1)
        else:
            return mid
    else:
        return -1

a = [5,3,4,8,7,2,9,1]
print('排序前：', a)
a.sort()
print('排序后：', a)
x = int(input('查找：'))
print("'%d'索引为：" %x,binary_search(a, x, 0, len(a) - 1))