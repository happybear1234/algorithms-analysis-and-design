import math

nodes = ('A', 'B', 'C', 'D', 'E')  # 节点
# dis矩阵初始化
dis = [[0, 3, 4, math.inf, 1],
       [3, 0, math.inf, 5, 1],
       [4, math.inf, 0, 2, 2],
       [math.inf, 5, 2, 0, math.inf],
       [1, 1, 2, math.inf, 0]]
print('初始路径：')
for i in range(len(dis)):
    print(dis[i])
node_num = len(nodes)  # 节点个数
for k in range(node_num):
    for i in range(node_num):
        for j in range(node_num):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])  # 若比原来距离小，则更新
print('\n各个点的最短路径为:')
for i in range(len(dis)):
    print(dis[i])
