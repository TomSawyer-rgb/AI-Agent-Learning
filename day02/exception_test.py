'''
异常处理：
    完成以下要求：
        - 输入两个数字。
        - 计算两个数字相除的结果。
        - 如果用户输入字母，提示输入错误。
        - 如果第二个数字为 0, 提示不能除以 0。
        - 无论是否发生异常，最后都输出 程序运行结束。
'''
# 1.输入两个数字
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

# 2.计算两个数字相除的结果
try:
    result = float(num1) / float(num2)
    print("计算结果为：", result)
except ValueError:
    print("输入错误，请输入有效的数字。")
except ZeroDivisionError:
    print("错误：第二个数字不能为 0。")
finally:
    print("程序运行结束。")
