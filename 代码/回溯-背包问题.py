best_v = 0  # 最优价值
now_w = 0  # 当前容量
now_v = 0  # 当前价值
best_x = None  # 最优背包选择序列

def backtrack(i):
	global best_v, now_w, now_v, x, best_x
	if i >= n: # 是否到达叶节点
		if best_v < now_v:
			best_v = now_v # 记录回溯最优价值
			best_x = x[:] # 记录回溯情况
	else:
		if now_w + w[i] <= c: # 约束条件，是否放入
			x[i] = 1
			now_w += w[i]
			now_v += v[i]
			backtrack(i + 1) # 进行下一个节点的分析
			now_w -= w[i] # 在到达叶节点后进行回溯
			now_v -= v[i]
		# 若放入 i 后不满足约束条件则进行到此处,选择不放入
		x[i] = 0
		backtrack(i + 1)


if __name__ == '__main__':
	n = 5  # 物品数量
	c = 10  # 背包容量
	print('物品数量：%d   背包容量：%d' %(n, c))
	w = [2,1,6,6,2] # 物品容量
	v = [3,2,8,9,4] # 物品价值
	print('物品容量列表：{}\n物品价值列表：{}'.format(w,v) )
	x = [False for i in range(n)]
	backtrack(0)
	print('\n最优价值：', best_v)
	print('背包物品选择序列：', best_x)