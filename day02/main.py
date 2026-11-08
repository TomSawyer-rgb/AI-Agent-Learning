# # 从 calculator.py 导入四个函数。
# import calculator as cal

# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))

# result_add = cal.add(num1, num2)
# result_subtract = cal.subtract(num1, num2)
# result_multiply = cal.multiply(num1, num2)
# result_divide = cal.divide(num1, num2)

# print("加法结果为：", result_add)
# print("减法结果为：", result_subtract)
# print("乘法结果为：", result_multiply)
# print("除法结果为：", result_divide)

'''
编写交互菜单
'''
from storage import load_records, save_records
from manager import add_record, list_records, delete_record, update_record

# 读取现有记录
records = load_records()
print("原有记录：", records)

# 添加新的学习记录
while True:
    print("\n===== 学习记录管理系统 =====")
    print("1. 添加学习记录")
    print("2. 查看学习记录")
    print("3. 修改学习记录")
    print("4. 删除学习记录")
    print("5. 退出系统")
    choice = input("请选择操作：")

    if choice == "1":
        date = input("请输入学习日期：")
        content = input("请输入学习内容：")
        hours = float(input("请输入学习时长（小时）："))
        records = add_record(records, date, content, hours)
        save_records(records)
        print("学习记录已添加！")
    elif choice == "2":
        list_records(records)

    elif choice == "3":
        list_records(records)
        try:
            index = int(input("请输入要修改的记录编号：")) - 1
            date = input("请输入新的学习日期：")
            content = input("请输入新的学习内容：")
            hours = float(input("请输入新的学习时长（小时）："))

            records = update_record(records, index, date, content, hours)
            save_records(records)

        except ValueError:
            print("请输入有效的数字！")

    elif choice == "4":
        list_records(records)
        try:
            index = int(input("请输入要删除的记录编号：")) - 1

            delete_record(records, index)
            save_records(records)

        except ValueError:
            print("请输入有效的数字！")
    elif choice == "5":
        print("程序退出！")
        break
    else:
        print("无效选择，请重新输入！")


