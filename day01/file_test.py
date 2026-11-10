'''
学习 Python 模块与文件操作:
    1. 模块(module)：
        - 模块是一个包含 Python 定义和语句的文件。
        - 可以使用 import 语句导入模块来重复使用其已存在的函数。
    2. 文件操作(file)：
        - Python 提供了内置函数 open() 来打开文件。
        - 文件操作模式：
            - 'r'：只读模式（默认）。
            - 'w'：写入模式（会覆盖原有内容）。
            - 'a'：追加模式（在原有内容后追加）。


            - 语法：
                with open('文件名', '模式') as 文件对象:
                    # 在这里进行文件操作
                    pass
                
'''
with open('day01/students.txt', 'w', encoding='utf-8') as file:
    file.write("姓名：赵六, 年龄：23, 专业：软件工程\n")
    file.write("姓名：李四, 年龄：23, 专业：人工智能\n")
    file.write("姓名：王五, 年龄：21, 专业：数据科学\n")


with open('day01/students.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("\n======== 读取文件内容 ========")
    print(content)


with open('day01/students.txt', 'a', encoding='utf-8') as file:
    file.write("姓名：赵六, 年龄：23, 专业：软件工程\n")

with open('day01/students.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("\n======== 读取追加后的文件内容 ========")
    print(content)