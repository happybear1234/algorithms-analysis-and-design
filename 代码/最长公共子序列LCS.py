import numpy

def find_lcseque(str1, str2):
    # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
    m = [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    # d用来记录转移方向
    d = [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:  # 对应字符相等的时候，用↖标记，则该位置的值为左上方的值加1
                m[i + 1][j + 1] = m[i][j] + 1
                d[i + 1][j + 1] = '↖'
            elif m[i + 1][j] > m[i][j + 1]:  # 左值 > 上值 的时候，用←标记
                m[i + 1][j + 1] = m[i + 1][j]
                d[i + 1][j + 1] = '←'
            else:  # 上值 >= 左值 用↑标记
                m[i + 1][j + 1] = m[i][j + 1]
                d[i + 1][j + 1] = '↑'
    (i, j) = (len(str1), len(str2))
    print(numpy.array(d))
    s = []
    while m[i][j]:  # 不为0时
        c = d[i][j]
        if c == '↖':  # 匹配成功，插入该字符，并向左上角找下一个
            s.append(str1[i - 1])
            i -= 1
            j -= 1
        if c == '←':  # 根据标记，向左找下一个
            j -= 1
        if c == '↑ ':  # 根据标记，向上找下一个
            i -= 1
    s.reverse()
    return ''.join(s)

if __name__ == '__main__':
    str1=input('请输入str1：')
    str2=input('请输入str2：')
    print('最长公共子序列是：',find_lcseque(str1,str2))



