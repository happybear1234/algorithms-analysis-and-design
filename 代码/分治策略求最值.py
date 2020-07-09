def max_min(l, low, high):
    """
    :param l: 序列
    :param low: left 索引
    :param high: right 索引
    :return: 返回的是一个列表[max,min]，第一个最大值，第二个最小值
    """
    #   判断列表分到最后只剩下两个数时就比较
    if high - low <= 1:
        if l[low] < l[high]:
            return [l[high], l[low]]
        else:
            return [l[low], l[high]]
    # 选取分治的中点
    mid = (low + high) // 2
    # 调用递归 分为s1，s2
    left_list = max_min(l, low, mid)
    right_list = max_min(l, mid + 1, high)
    # 将左边的最大值和右边的最大值比较
    if left_list[0] > right_list[0]:
        # 将左边的最小值和右边最小值比较
        if left_list[1] > right_list[1]:
            # 返回列表[max,min]
            return [left_list[0], right_list[1]]
        else:
            return [left_list[0], left_list[1]]
    else:
        if left_list[1] > right_list[1]:
            return [right_list[0], right_list[1]]
        else:
            return [right_list[0], left_list[1]]
test_list = [1,3,5,7,9,8,6,4,2,0]
print('序列：', test_list)
num = max_min(test_list, 0, len(test_list) - 1)
print("最大值：%d,最小值%d" % (num[0], num[1]))