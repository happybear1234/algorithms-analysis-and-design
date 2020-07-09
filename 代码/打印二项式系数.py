def main():
    n = int(input('(x+y)^n,请输入n的值: '))
    L = [[]] * (n + 1)
    for i in range(len(L)):
        L[i] = [None] * (i + 1)
        for k in range(len(L[i])): # 每一行的首位都是1，中间的数值ai为上一层a(i-1)与ai之和
            if k == 0 or k == i:
                L[i][k] = 1
            else:
                L[i][k] = L[i - 1][k] + L[i - 1][k - 1]
    # 打印
    print('\n(x+y)^%d=' %(n), end='')
    flag = 0 # 控制第一个 + 不输出
    for i in range(n + 1):
        if n == 0: # 0 幂次
            print('1')
            break
        if flag:
            print(' + ', end='')
        flag = 1 # 后面加号都输出
        # 输出系数 系数为 1 的不打印
        if L[n][i] != 1:
            print(L[n][i], end='')
        # 输出 x 的幂
        if n - i != 0:
            if n - i == 1:
                print('x', end='')
            else:
                print('x^%d' %(n - i), end='')
        # 输出 y 的幂
        if i != 0:
            if i == 1:
                print('y', end='')
            else:
                print('y^%d' %i, end='')




if __name__ == '__main__':
    main()