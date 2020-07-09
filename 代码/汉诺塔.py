import turtle


# 声明栈方法类
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1] # 查看当前栈元素
    def size(self):
        return len(self.items)


# 1) 画出三个柱子
def draw_column3():
    # 初始化 turtle
    t = turtle.Turtle()
    t.hideturtle() # 隐藏画笔形状
    # 从左至右开始
    def draw_column1(k):
        t.up() # 笔画抬起时移动,不划线
        t.pensize(10) # 画笔宽度
        t.speed(100)# 画笔移动速度
        t.goto(400 * (k - 1), 100) # 画笔移动到坐标(x,y)
        t.down() # 画笔落下时移动,划线
        t.goto(400 * (k - 1), -100)
        t.goto(400 * (k - 1) - 40, -100)
        t.goto(400 * (k - 1) + 40, -100)
    draw_column1(0)
    draw_column1(1)
    draw_column1(2)


# 2)在第一根柱子画出 n 个盘子
def draw_plates(n):
    plates = [turtle.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].hideturtle()
        plates[i].up()
        plates[i].shape('square')
        plates[i].shapesize(1,10 - i)
        plates[i].goto(-400,-90 + 20 * i)
        plates[i].showturtle()
    return plates


# 3)实现
# 创建栈
def column_stack():
    columns = [Stack() for i in range(3)]
    return columns
# 移动
def move_plates(plates, columns, fromColumn, toColumn):
    index = columns[fromColumn].peek()
    plates[index].goto((fromColumn - 1) * 400, 150)
    plates[index].goto((toColumn - 1) * 400, 150)
    l = columns[toColumn].size()
    plates[index].goto((toColumn - 1) * 400, -90 + 20 * l)
# 递归实现
def hanoi(plates, columns, height, fromColumn, withColumn, toColumn):
    if height == 1:
        move_plates(plates, columns, fromColumn, toColumn)
        columns[toColumn].push(columns[fromColumn].pop())
        return

    hanoi(plates, columns, height - 1, fromColumn, toColumn, withColumn) # 借助第三根，将第一根前 n-1 层移到第二根
    move_plates(plates, columns, fromColumn, toColumn)
    columns[toColumn].push(columns[fromColumn].pop())
    hanoi(plates, columns, height - 1, withColumn, fromColumn, toColumn) # 借助第一根，从第二根移动到第三根


n = int(input('请输入汉诺塔层数:\n'))
draw_column3()
plates = draw_plates(n)
columns = column_stack()
for i in range(n):
    columns[0].push(i)
hanoi(plates, columns, n, 0, 1, 2)
turtle.done()