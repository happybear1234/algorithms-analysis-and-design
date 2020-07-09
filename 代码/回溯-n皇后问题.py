import numpy as np

count = 0
def isCorrect(i, j, Q, n):
    """
判断当前位置能否放入皇后
    :param i:行
    :param j:列
    :param Q:棋盘 n*n
    :param n:皇后数量
    :return:1：放入皇后  0：不放
    """
    # 判断行
    for tmp_j in range(0, n):
        if Q[i][tmp_j] == 1 and tmp_j != j:
            return 0

    # 判断列
    for tmp_i in range(0, n):
        if Q[tmp_i][j] == 1 and tmp_i != i:
            return 0

    # 判断左上方
    tmp_i = i - 1
    tmp_j = j - 1
    while tmp_i >= 0 and tmp_j >= 0:
        if Q[tmp_i][tmp_j] == 1:
            return 0
        tmp_i -= 1
        tmp_j -= 1

    # 判断右下方
    tmp_i = i + 1
    tmp_j = j + 1
    while tmp_i < n and tmp_j < n:
        if Q[tmp_i][tmp_j] == 1:
            return 0
        tmp_i += 1
        tmp_j += 1

    # 判断左下方
    tmp_i = i + 1
    tmp_j = j - 1
    while tmp_i < n and tmp_j >= 0:
        if Q[tmp_i][tmp_j] == 1:
            return 0
        tmp_i += 1
        tmp_j -= 1

    # 判断右上方
    tmp_i = i - 1
    tmp_j = j + 1
    while tmp_i >= 0 and tmp_j < n:
        if Q[tmp_i][tmp_j] == 1:
            return 0
        tmp_i -= 1
        tmp_j += 1
    # 所有满足条件，放入皇后
    return 1

def Queen(j, Q, n):
    global count
    if j == n: # 递归条件
        print(Q) # 打印解
        print('\n')
        count += 1
        return
    for i in range(n):
        if isCorrect(i, j, Q, n): # 如果能放入皇后
            Q[i][j] = 1 # 放入皇后
            Queen(j + 1, Q, n) # 递归深度优先搜索解空间树
            Q[i][j] = 0 # 回溯到上层
def main():
    n = int(input('请输入皇后数量：'))
    Q = np.zeros((n, n))
    Queen(0, Q, n)
    print('满足条件的一共有%d种方法' % count)

main()

