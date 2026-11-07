'''
列表(list)和字典(dict):  开发 AI Agent 时，聊天记录、工具列表、用户信息都会使用它们。
    1. 列表(list)：
        - 用于存储一组有序的数据。(可用于存储多个数据的容器)
    2. 字典(dict)：
        - 用于存储一组键值对的数据。
    3.实际开发中，我们经常把字典放进列表中，形成一个列表套字典的结构。
'''

'''
三、编写一个学生管理系统：
    要求实现：
        1. 创建一个列表 students。   创建一个名为 students 的列表。
        2. 添加三个学生，每个学生使用字典保存。
        3. 每个学生包含姓名、年龄、专业。
        4. 输出所有学生的信息。
        5. 添加一个新学生。
        6. 修改其中一个学生的年龄。
        7. 删除其中一个学生。
            {"name": "张三", "age": 20, "major": "计算机科学"},
    {"name": "李四", "age": 22, "major": "人工智能"},
    {"name": "王五", "age": 21, "major": "数据科学"},
'''

# 1. 创建一个列表 students
students = []
# 2. 添加三个学生，每个学生使用字典保存
students.append({"name": "张三", "age": 20, "major": "计算机科学"})
students.append({"name": "李四", "age": 22, "major": "人工智能"})
students.append({"name": "王五", "age": 21, "major": "数据科学"})
# 3. 输出所有学生的信息
print("\n======== 学生信息列表 ========")
# print(students)
# 使用for循环优化输出
for student in students:
    # student['name']：通过字典的键获取对应的值。
    print(f"姓名：{student['name']}, 年龄：{student['age']}, 专业：{student['major']}")
# 4. 添加一个新学生
new_student = {"name": "赵六", "age": 23, "major": "软件工程"}
students.append(new_student)
# 5. 修改其中一个学生的年龄
students[1]["age"] = 23  # 修改李四的年龄为23
# 6. 删除其中一个学生
del students[0]  # 删除张三
# 7. 输出修改后的学生信息
print("\n======== 修改后的学生信息列表 ========")
# print(students)
# 使用for循环优化输出
for student in students:
    # student['name']：通过字典的键获取对应的值。
    print(f"姓名：{student['name']}, 年龄：{student['age']}, 专业：{student['major']}")


