def multi(stra, strb):
    a = stra[::-1] # 将字符串倒序排列
    b = strb[::-1]
    length_a = len(stra)
    length_b = len(strb)
    result = [0 for i in range(length_a + length_b)]
    # 结果储存在 result 中,result[i + j] = a[i] * b[j]
    for i in range(length_a):
        for j in range(length_b):
            result[i + j] += int(a[i]) * int(b[j])
    # 从低位到高位进行进位
    for i in range(len(result)):
        while result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10
    # 将前导0全部剔掉，比如我们结果是236，在result中是这样存储的63200……
    result = result[::-1] # 倒序
    for i in range(len(result)): # 删除前导0
        if result[0] == 0:
            del result[0]
        else:
            break
    print('%d*%d=' % (int(stra), int(strb)), end='')
    for i in range(len(result)):
        print(result[i], end='')

if __name__ == '__main__':
    print('请输入两个参数')
    str1 = input()
    str2 = input()
    if str1.isdigit() and str2.isdigit():
        multi(str1, str2)