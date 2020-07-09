# 二分查找（迭代）
def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (right + left) // 2
        if a[mid] < x:
            left = mid +1
        elif a[mid] > x:
            right = mid - 1
        else:
            return mid
    return 0
a = [5,3,4,8,7,2,9,1]
print('排序前：', a)
a.sort()
print('排序后：', a)
x = int(input('查找：'))
print("'%d'索引为：" %x,binary_search(a, x))

