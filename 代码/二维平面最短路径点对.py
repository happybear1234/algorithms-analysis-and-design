import matplotlib.pyplot as plt
import math
import random


# 1)暴力求解
def closestpair_simple(X, n):
    dist = [[distance(X[i], X[j]), i, j] for i in range(len(X)) for j in range(i+1,len(X))]
    return min(dist)[0], [X[min(dist)[1]], X[min(dist)[2]]]
# 距离公式
def distance(a, b):
    return math.sqrt(math.pow((a[0]-b[0]), 2)+math.pow((a[1]-b[1]), 2))

# 2) 分治策略
# 归并预排序 复杂度 o(nlogn)
def sort(points, l, r):
    n = len(points)
    X = list(points)
    Y = list(points)
    merge_sort_X(X, l, r)
    merge_sort_Y(Y, l, r)
    return closest_pair(X, Y, n)
# 按 x 坐标排序
def merge_sort_X(points, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merge_sort_X(points, l, m)
        merge_sort_X(points, m + 1, r)
        merge_X(points, l, m, r)
def merge_X(points, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = points[l + i]
    for j in range(0, n2):
        R[j] = points[m + 1 + j]
    # 归并临时数组到 points[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    while i < n1 and j < n2:
        if L[i][0] <= R[j][0]:
            points[k] = L[i]
            i += 1
        else:
            points[k] = R[j]
            j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        points[k] = L[i]
        i += 1
        k += 1
    # 拷贝 R[] 的保留元素
    while j < n2:
        points[k] = R[j]
        j += 1
        k += 1
# 按 y 坐标排序
def merge_sort_Y(points, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merge_sort_Y(points, l, m)
        merge_sort_Y(points, m + 1, r)
        merge_Y(points, l, m, r)
def merge_Y(points, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = points[l + i]
    for j in range(0, n2):
        R[j] = points[m + 1 + j]
    # 归并临时数组到 points[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    while i < n1 and j < n2:
        if L[i][1] <= R[j][1]:
            points[k] = L[i]
            i += 1
        else:
            points[k] = R[j]
            j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        points[k] = L[i]
        i += 1
        k += 1
    # 拷贝 R[] 的保留元素
    while j < n2:
        points[k] = R[j]
        j += 1
        k += 1

# 求最短距离对 复杂度o(nlogn)
def closest_pair(X, Y, n):
    # 不足 4 个时暴力求解
    if n <= 3:
        return closestpair_simple(X, n)
    mid = n // 2
    Y_left = []
    Y_right = []
    for p in Y:
        if p in X[:mid]:
            Y_left.append(p)
        else:
            Y_right.append(p)
    # 分别对左,右进行递归
    dis_left, point_left = closest_pair(X[:mid], Y_left, mid)
    dis_right, point_right = closest_pair(X[mid:], Y_right, n - mid)
    if dis_left <= dis_right:
        min_dis = dis_left
        min_point = point_left
    else:
        min_dis = dis_right
        min_point = point_right
    wait_set = []
    # 关于坐标 Y 里取小于当前最短距离的为候补点矩形区域
    for (x, y) in Y:
        if abs(x - X[mid][0]) < min_dis:
            wait_set.append((x, y))
    wait_dis, wait_point = wait_set_closest(wait_set, min_dis, min_point)
    if wait_dis <= min_dis:
        min_dis = wait_dis
        min_point = wait_point
    return min_dis, min_point
# 候补区域最短距离
def wait_set_closest(wait_set, d, min_point):
    min_d = d
    length = 0
    # 比较候补区域最近的 6 个点
    for i in range(len(wait_set)):
        if len(wait_set) > 6:
            length = 6
        else:
            length = len(wait_set)
        for j in range(i + 1, length):
            temp_dis = distance(wait_set[i], wait_set[j])
            if temp_dis < min_d:
                min_d = temp_dis
                min_point = [wait_set[i], wait_set[j]]
    return min_d, min_point

# 绘图
def show_closest_pair(points, min_point, n):
    plt.xlim(0, 3 * n)
    plt.ylim(0, 3 * n)
    plt.title("Point Pair")
    for i in range(len(points)):
        plt.plot(points[i][0], points[i][1], 'bo-')
    plt.plot([min_point[0][0],min_point[1][0]], [min_point[0][1],min_point[1][1]], 'ro-')
    plt.show()
def main():
    n = int(input('请输入要生成的坐标数:\n'))
    points = [(random.randint(0, 3 * n), random.randint(0, 3 * n)) for i in range(0, n)]
    print(points)
    l = 0
    r = len(points) - 1
    min_dist, min_point = sort(points, l, r)
    print ('分治:', (min_dist, min_point))
    print('暴力求解', closestpair_simple(points, len(points)))
    show_closest_pair(points, min_point, n)

main()