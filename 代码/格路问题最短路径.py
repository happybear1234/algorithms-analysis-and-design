import matplotlib.pyplot as plt
import random


# 动态规划:自底向上
def min_path(pots_dic, m, n):
    d = 0 # 初始化 当前最短路径距离
    from_path = [] # 1:来源左 2:来源下
    i, j=0, 0 # 初始位置
    while i != m and j != n:
        dR = pots_dic[i +1, j]  # 向右的距离
        dU = pots_dic[i, j +1]  # 向上的距离
        if(dR < dU):
            d += dR
            i += 1
            from_path.append(1)
        else:
            d += dU
            j += 1
            from_path.append(2)

    if i==m: # 已经到最右端
        while j != n:
            dU = pots_dic[i, j + 1]  # 向上的距离
            d += dU
            j += 1
            from_path.append(2)
    else:
        while i != m:
            dR = pots_dic[i + 1, j]  # 向右的距离
            d += dR
            i += 1
            from_path.append(1)
    return d, from_path
# 绘制路径
def show_path(pots_dic,from_path, m, n):
    # 初始化图
    plt.figure(figsize=(10, 10))
    plt.grid(linestyle='--')
    plt.xticks(range(m + 1))
    plt.yticks(range(n + 1))
    # 标上权值
    for a, b in pots_dic:
        plt.text(a, b, pots_dic[a, b], ha='center', va='bottom', fontsize=10, color='b')

    # 绘制路径
    point = []
    x, y = 0, 0
    point.append([x, y])
    for i in from_path:
        if i == 1:
            x += 1
            point.append([x, y])
        else:
            y += 1
            point.append([x, y])
    for i in range(len(point) - 1):
        plt.plot([point[i][0], point[i + 1][0]], [point[i][1] , point[i + 1][1]], color='r')
    plt.show()

def main():
    # 格子方阵大小 m*n
    m = int(input('输入格图的行:'))
    n = int(input('输入格图的列:'))
    pots_key = [] # 坐标集
    pots_value = [] # 权值集
    # 生成格子,每个点附上权值
    for i in range(0, m + 1):
        for j in range(n + 1):
            temp_key = (i,j)
            pots_key.append(temp_key)
            temp_value = random.randint(1, 99)
            pots_value.append(temp_value)
    pots_dic = dict(zip(pots_key, pots_value))
    pots_dic[0,0] = 0
    print(pots_dic)
    min_d , from_path = min_path(pots_dic, m, n)
    path = []
    for i in from_path:
        if i == 1:
            path.append('r')
        else:
            path.append('u')
    print('\n')
    print('path=',list(path))
    print('d=',min_d)
    show_path(pots_dic, from_path, m , n)
main()