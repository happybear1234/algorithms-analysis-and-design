# 判断是否能放入团中
def place(t):
    bool = 1
    for k in range(1, n): # 判断目前扩展的t顶点和前面t-1个顶点是否相连
        if x[k] and graph[t][k] == 0:
            bool = 0
            break
    return bool

def BackTrack(t):
    # 顶点遍历完，更新最优解
    global cn,bn,graph
    if t > n: # 到达叶节点
        for i in range(1, n + 1):
            bx[i] = x[i] # 记录最优值结点标记
        bn = cn # 记录最优值
        return

    # 如果能放进团中
    if place(t):
        x[t] = 1  # 标记
        cn += 1 # 子图中结点数 +1
        BackTrack(t + 1) # 深度搜索递归
        cn -= 1 # 回溯

    # 限界条件
    if cn + (n - t) > bn:
        x[t] = 0 # 不放入团，标记为 0
        BackTrack(t + 1)


def main():
    global n, m # n：顶点数 m:边数
    global cn, bn # cn:当前 完全子图中 选择了cn个节点 bn:目前找到的团中所含的最多节点
    global graph # graph[u][v]=1 表示当前 顶点 u,v 存在无向边
    global x, bx # x[i]=1:表示第i个节点已加入当前完全子图 bx[]:对应bn中记录的团所包含的点 bx[i]=1:表示有该节点
    n = int(input('请输入结点数：'))
    m = int(input('请输入边数：'))
    cn = 0
    bn = 0
    N = 100
    x = [None for i in range(N)]
    bx = [None for i in range(N)]
    graph = [[0 for i in range(N)] for i in range(N)] # 图
    print("请输入相连的顶点(空格隔开)：")
    for i in range(m): # 无向边图
        u, v = map(int, (input().split(' ')))
        graph[u][v] = 1
        graph[v][u] = 1
    BackTrack(1)
    print('最大团个数：', bn)
    print('结点有：')
    for i in range(n):
        if bx[i + 1]:
            print(i + 1, end=' ')

main()
"""
样例：
请输入结点数：5
请输入边数：8
请输入相连的顶点(空格隔开)：
1 2
1 3
1 4
1 5
2 3
3 4
3 5
4 5
"""


