> 一.创建虚拟环境
1.创建虚拟环境
python -m venv .venv
2.激活虚拟环境
.\.venv\Scripts\Activate.ps1
3.检查python版本
python --version
4.删除虚拟文件夹
Remove-Item -Recurse -Force .venv

# Day 1：Python 基础学习

## 一、项目简介

这是 AI Agent 学习计划的第一个阶段项目，主要用于练习 Python 基础语法和文件操作，为后续开发 AI Agent 应用打下基础。

## 二、学习内容

本阶段主要学习了以下知识：

- Python 变量与数据类型
- `input()` 输入和 `print()` 输出
- 函数的定义与调用
- `return` 返回值
- `int()` 和 `float()` 类型转换
- Python 列表（List）
- Python 字典（Dictionary）
- 文件读写操作
- Git 基础操作

## 三、实践项目

### 1. 个人信息介绍程序

文件：`main.py`

实现功能：
- 输入个人姓名和学习目标
- 输入年龄和每日学习时间
- 使用函数计算每周学习时间

### 2. 简易计算器

实现功能：
- 加法
- 减法
- 乘法
- 使用函数封装计算逻辑

### 3. 学生信息管理

文件：`student_manager.py`

实现功能：
- 使用列表保存多个学生信息
- 使用字典保存学生姓名、年龄等信息
- 添加学生
- 修改学生信息
- 删除学生信息
- 遍历学生列表

### 4. 文件读写练习

文件：`file_test.py`

实现功能：
- 创建文本文件
- 写入学生信息
- 读取文件内容
- 向文件追加数据

## 四、项目结构

```text
AI-Agent-Learning/
│
├── .gitignore
├── students.txt
│
└── day01/
    ├── README.md
    ├── main.py
    ├── student_manager.py
    └── file_test.py
```

## 五、运行环境

- 操作系统：Windows
- Python：3.11.4
- 开发工具：Visual Studio Code
- 版本管理：Git

## 六、运行方式

在项目根目录打开终端，执行：

```bash
python day01/main.py
```

运行学生信息管理程序：

```bash
python day01/student_manager.py
```

运行文件读写程序：

```bash
python day01/file_test.py
```

## 七、学习总结

通过 Day 1 的学习，我初步掌握了 Python 基础语法，能够使用函数组织代码，使用列表和字典管理数据，并通过文件操作实现数据的保存和读取。

同时，完成了 Git 仓库初始化、`.gitignore` 配置和第一次版本提交的准备工作。

## 八、下一步计划

- 学习 Python 模块与包
- 学习异常处理
- 学习面向对象编程
- 学习 JSON 数据处理
- 学习 HTTP 请求
- 继续完善 Python 项目开发能力
