def fibonacci(n):
    # 创建一个列表用于存储斐波那契数列
    fib_list = []

    # 前两个数字为 0 和 1
    fib_list.append(0)
    fib_list.append(1)

    # 生成剩余的数字
    for i in range(2, n):
        # 计算当前数字为前两个数字的和
        fib_num = fib_list[i - 1] + fib_list[i - 2]
        # 将数字添加到列表中
        fib_list.append(fib_num)

    return fib_list

# 输入要生成的斐波那契数列长度
n = int(input("请输入要生成的斐波那契数列长度："))

# 调用函数生成斐波那契数列
fib_sequence = fibonacci(n)

# 打印生成的斐波那契数列
print("生成的斐波那契数列为：")
print(fib_sequence)
