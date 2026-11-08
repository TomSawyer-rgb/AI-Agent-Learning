# Day 2：Python 个人学习记录管理系统

## 1. 项目简介

这是一个基于 Python 开发的命令行个人学习记录管理系统。

项目使用 JSON 文件进行数据持久化，实现学习记录的添加、查看、修改和删除（CRUD）功能。

通过本项目，练习 Python 函数、模块化编程、异常处理、JSON 数据读写以及文件操作，为后续学习 AI Agent 开发打下基础。

## 2. 项目功能

目前实现以下功能：

| 功能 | 说明 |
|---|---|
| 添加学习记录 | 输入日期、学习内容和学习时长 |
| 查看学习记录 | 显示所有已保存的学习记录 |
| 修改学习记录 | 根据记录编号修改指定记录 |
| 删除学习记录 | 根据记录编号删除指定记录 |
| 数据持久化 | 使用 JSON 文件保存学习记录 |
| 异常处理 | 捕获错误输入，避免程序异常退出 |

## 3. 项目结构

```text
day02/
│
├── main.py                 # 程序入口，负责菜单和用户交互
├── manager.py              # 业务逻辑，负责增删改查
├── storage.py              # JSON 文件读取和保存
│
├── exception_test.py      # 异常处理练习
├── calculator.py          # Python 模块导入练习
├── json_test.py            # JSON 数据读写练习
├── student.json           # 学生信息记录数据
│
├── data/
│   └── records.json        # 学习记录数据
│
└── README.md               # 项目说明文档
```

## 4. 技术知识

### Python 基础

- 函数定义与调用
- 列表（List）
- 字典（Dictionary）
- 条件判断（if/elif/else）
- 循环结构（while/for）
- 函数返回值（return）

### 异常处理

- try
- except
- finally
- ValueError
- ZeroDivisionError

### 模块化编程

- import
- 模块拆分
- 函数调用
- 模块之间的数据传递

### JSON 数据处理

- json.dumps()
- json.loads()
- json.dump()
- json.load()
- ensure_ascii=False
- indent=4

### 文件操作

- open()
- 文件读取（r）
- 文件写入（w）
- 文件追加（a）
- with open()

### 数据管理

- append()
- pop()
- enumerate()
- len()
- CRUD 操作

## 5. 程序运行

### 环境要求

- Python 3.11+
- Windows
- VS Code（推荐）

### 运行方式

在项目根目录执行：

```bash
python day02/main.py
```

### 操作菜单

```text
===== 学习记录管理系统 =====
1. 添加学习记录
2. 查看学习记录
3. 修改学习记录
4. 删除学习记录
5. 退出系统
```

## 6. 数据存储格式

学习记录保存在 `data/records.json` 中。

数据格式示例：

```json
[
    {
        "date": "2026-11-08",
        "content": "study English words",
        "hours": 2.0
    }
]
```

程序启动时读取 JSON 文件，执行修改后重新保存，实现数据持久化。

## 7. 项目架构设计

采用简单的模块化设计：

```text
             main.py
                |
       用户交互与菜单控制
                |
          manager.py
                |
           业务逻辑
                |
           storage.py
                |
          JSON 文件读写
                |
          records.json
```

各模块职责：

- main.py：负责接收用户输入、显示菜单和调用功能。
- manager.py：负责学习记录的添加、查看、修改和删除。
- storage.py：负责 JSON 文件的数据读取与保存。
- records.json：保存实际的学习记录。

## 8. Day 2 学习总结

通过本项目，我完成了从独立 Python 语法练习到小型完整应用开发的过渡。

主要收获：

1. 理解了 Python 列表和字典的组合使用。
2. 掌握了函数之间的数据传递。
3. 学会了将程序拆分为多个模块。
4. 掌握了 JSON 文件的读取、写入和持久化。
5. 学会使用 try/except 处理异常输入。
6. 理解了 CRUD 四种基本数据操作。
7. 初步建立了业务逻辑与数据存储分离的编程思想。

## 9. 后续学习计划

Day 3 计划学习：

- HTTP 协议基础
- GET 和 POST 请求
- Python requests 库
- API 接口调用
- JSON API 数据解析

目标：使用 Python 调用真实 API，为后续接入大语言模型 API 和开发 AI Agent 做准备。

---

**Project:** AI-Agent-Learning  
**Day:** 02  
**Language:** Python 3.11  
**Status:** Completed