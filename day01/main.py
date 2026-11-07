'''2026-11-07'''
# # 1. 获取用户信息
# name = input("请输入你的名字：")
# goal = input("请输入你的学习目标：")

# # 2. 定义一个函数
# def instroduce(name, goal):
#     print("\n======== 个人学习档案 ========")
#     print(f"姓名：{name}")
#     print(f"学习目标：{goal}")
#     print("当前学习方向：AI Agent 开发")
#     print("================================")

# # 3. 调用函数
# instroduce(name,goal)

# # 独立练习1
# name = input("请输入你的名字：")
# age = int(input("请输入你的年龄："))
# daily_study_hours = float(input("请输入你每天学习的小时数："))

# def calculate_weekly_hours(hours):
#     weekly_hours = hours * 7
#     return weekly_hours

# result = calculate_weekly_hours(daily_study_hours)

# print("\n======== 学习计划 ========")
# print(f"姓名：{name}")
# print(f"年龄：{age}")
# print(f"每天学习小时数：{daily_study_hours} 小时")
# print(f"每周学习小时数：{result} 小时")

'''
小结：
    理解 print 和 return 的区别：
        print 把信息显示在终端上，而 return 是将结果返回给调用者。
'''


'''
二、编写一个简单的计算器：
    实现三个功能：
        1. 两个数字相加。
        2. 两个数字相减。
        3. 两个数字相乘。
'''
# # 用户输入两个数字
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))

# # 定义三个函数来实现加、减、乘的功能
# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# # 调用函数并定义变量保存结果
# result_add = add(num1, num2)
# result_subtract = subtract(num1, num2)
# result_multiply = multiply(num1, num2)

# # 输出计算结果
# print("\n======== 计算结果 ========")
# print(f"两数之和 = {result_add}")
# print(f"两数之差 = {result_subtract}")
# print(f"两数之积 = {result_multiply}")


