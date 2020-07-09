def merge2(array, left, mid, right):
    temp = array[left:right + 1]
    # 新数组temp的左中右标记,充当常量
    n = right - left + 1
    l = 0
    r = right - left
    m = mid - left
    # 左数组标记i,右数组标记j,赋值外部循环标记k
    i = 0
    j = m + 1
    # 遍历【0，n)即整个数组长度，每次确定一个下标应该赋值的元素并完成赋值操作
    k = 0
    while k < n:
        # 2、定义判断条件，防越界；循环的次数是由n确定的，不存在i,j同时越界的情况
        if i > m:
            array[k + left] = temp[j]
            j += 1
        elif j > r:
            array[k + left] = temp[i]
            i += 1
        # 1、判断两个子数组当前位置的值，并赋值给原数组array的对应位置，此处可能涉及到越界问题,所以循环主体开始之前要判断一下
        elif temp[i] < temp[j]:
            array[k + left] = temp[i]
            i += 1
        else:
            array[k + left] = temp[j]
            j += 1

        k += 1
    return array

def merge_sort_BU(array):
    result = []
    n = len(array)
    # 初始最小区间长度为1
    sz = 1
    while sz < n + 1:

        i = 0
        while i < n:
            l1 = i
            r1 = i + 2 * sz - 1
            if r1 > n - 1:
                r1 = n - 1
            m1 = l1 + sz - 1
            result = merge2(array, l1, m1, r1)
            i += 2 * sz

        sz *= 2
    print('\n排序后数组：', result)

array = [12, 11, 13, 5, 6, 7]
print('给定数组：', array)
merge_sort_BU(array)
