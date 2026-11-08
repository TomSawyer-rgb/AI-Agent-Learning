# import json

'''
实践：Python 字典转换为 JSON
'''
# student = {
#     "name": "Tom",
#     "age": 20,
#     "major": "Big Data Science",
#     "skills": ["Python", "SQL", "Git", "C语言"],
#     "is_student": True
# }

# # Python 字典转换成 JSON字符串
# json_data = json.dumps(
#     student,  # 要转换的 Python 字典
#     ensure_ascii=False,  # 保留中文字符，显示中文
#     indent=4  # 让 JSON 数据缩进 4 个空格，方便阅读。
# )
# # 打印 JSON字符串
# print(json_data)

# print(type(student))  # <class 'dict'>
# print(type(json_data))  # <class 'str'>

'''
实践：JSON字符串转换为 Python 字典
'''
# # JSON字符串转换为 Python 字典
# python_dict = json.loads(json_data)
# # 打印 Python 字典
# print(python_dict)

# print(python_dict["name"])  # Tom
# print(python_dict["age"])  # 20
# print(python_dict["skills"])  # ['Python', 'SQL', 'Git', 'C语言']


'''
保存JSON数据到文件：
    - 使用 json.dump() 方法将 JSON 数据保存到文件中。
'''
# with open("day02/student.json", "w", encoding="utf-8") as f:
#     json.dump(
#         student,
#         f,
#         ensure_ascii=False,
#         indent=4
#     )

# with open("day02/student.json", "r", encoding="utf-8") as f:
#     # 从文件中读取JSON文件
#     data = json.load(f)

# print(data)

# # 修改数据并重新保存
# data["age"] = 18
# with open("day02/student.json", "w", encoding="utf-8") as f:
#    json.dump(
#       data,
#       f,
#       ensure_ascii=False,
#       indent=4
#    )

'''
独立练习:
    要求：
        1. 创建一个学生字典。
        2. 包含姓名、年龄、专业、技能列表。
        3. 将字典保存到 student.json。
        4. 从 student.json 读取数据。
        5. 输出姓名、专业和全部技能。
        6. 将年龄修改为 21。
        7. 把修改后的数据重新保存。
        8. 再次读取文件，确认年龄已经变成 21。
'''
import json

student = {
    "name": "Alice",
    "age": 18,
    "major": "Computer Science",
    "skills": ["Python", "Java", "C++"]
}
# 将字典保存到 student.json
with open("day02/student.json", "w", encoding="utf-8") as f:
    json.dump(
        student, 
        f, 
        ensure_ascii=False, 
        indent=4
    )
with open("day02/student.json", "r", encoding="utf-8") as f:
    # 从 student.json 读取数据
    data = json.load(f)
print(data)

data["age"] = 21
print(data)
# 将修改后的数据重新保存
with open("day02/student.json", "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4,
    )

with open("day02/student.json", "r", encoding="utf-8") as f:
    # 再次读取文件，确认年龄已经变成 21
    updated_data = json.load(f)
print(updated_data)
print("数据修改并保存成功！")

