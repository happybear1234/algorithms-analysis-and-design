# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         great = [i for i in arr[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(great)
#
# print(quicksort([10,6,5,4,8]))


def quick_sort(arr, l, r):
    if(l < r):
        i = l
        j = r
        x = arr[l]
        while i < j:
            while i < j and arr[j] >= x: # 从右向左找第一个小于 x 的数
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1

            while i < j and arr[i] < x: # 从左向右找第一个大于 x 的数
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = x
        quick_sort(arr, l, i - 1) # 递归调用
        quick_sort(arr, i + 1, r)

lis = [12, 11, 13, 5, 6, 7]
print('原始序列：', lis)
quick_sort(lis, 0, len(lis)-1)
print('\n排序后序列：',lis)