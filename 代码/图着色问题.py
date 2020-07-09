# 判断当前颜色是否与相邻顶点重复
def ok(t):
    global v, graph, color
    for i in range(v):
        if graph[t][i] ==1 and color[t] == color[i]: # 如果顶点 t，i 有边，且 t 和 i 颜色相同
            return False
    return True
def back_trace(t):
    global v, c, sum, color
    if t >= v: # 到达叶节点
        sum += 1
        print(color)
    else:
        for i in range(1, c + 1): # 分别为 t 位置尝试第 i 中的颜色
            color[t] = i # 表示 t 位置上第 i 种颜色
            if ok(t):
                back_trace(t + 1) # 递归
            color[t] = None # 回溯
def main():
    global v, graph # v顶点数 graph邻接矩阵
    global c, color # c颜色数 color当前边的颜色
    global sum # 着色方法数目
    v = int(input('请输入顶点数：'))
    c = int(input('请输入颜色数：'))
    sum = 0
    color = [None for i in range(v)]
    # 邻接矩阵
    graph =[[None for i in range(v)] for i in range(v)]
    print('请输入邻接矩阵：')
    for i in range(v):
            graph[i] = list(map(int, input().split()))
    back_trace(0)
    print('着色方法有%d种' %sum)
main()

"""
样例输入：
5
4
0 1 1 1 0
1 0 1 1 1
1 1 0 1 0
1 1 1 0 1
0 1 0 1 0
"""