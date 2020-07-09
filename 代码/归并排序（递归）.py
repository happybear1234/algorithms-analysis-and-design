def merge(lis, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = lis[l + i]

    for j in range(0, n2):
        R[j] = lis[m + 1 + j]

    # 归并临时数组到 lis[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lis[k] = L[i]
            i += 1
        else:
            lis[k] = R[j]
            j += 1
        k += 1

    # 拷贝 L[] 的保留元素
    while i < n1:
        lis[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        lis[k] = R[j]
        j += 1
        k += 1

def merge_sort(lis, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merge_sort(lis, l, m)
        merge_sort(lis, m + 1, r)
        merge(lis, l, m, r)


lis = [12, 11, 13, 5, 6, 7]
n = len(lis)
print("给定的数组:")
for i in range(n):
    print("%d" % lis[i], end=' '),

merge_sort(lis, 0, n - 1)
print("\n\n排序后的数组:")
for i in range(n):
    print("%d" % lis[i], end=' ')