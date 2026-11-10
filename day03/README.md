# Day 3：Python HTTP 请求与 API 数据处理

## 一、今日学习目标

今天主要学习 Python 如何通过 HTTP 请求获取网络 API 数据，并将获取的数据保存到本地 JSON 文件，实现 API 数据的获取、处理、保存和读取。

主要学习内容：

1. HTTP 和 API 基础知识
2. Requests 库的使用
3. GET 请求与 HTTP 状态码
4. JSON 数据解析
5. Python 异常处理
6. pathlib库 文件路径管理
7. JSON 文件读写
8. Python 模块化编程

## 二、项目介绍

本项目使用 Python 的 Requests 库访问 JSONPlaceholder 测试 API，获取文章数据，并将数据保存到本地 JSON 文件。

项目实现了以下功能：

- 通过 HTTP GET 请求获取文章数据。
- 解析服务器返回的 JSON 数据。
- 提取文章 ID、用户 ID、标题和正文。
- 将 API 数据保存到本地 JSON 文件。
- 从本地 JSON 文件重新读取数据。
- 自动创建不存在的文件夹。
- 对网络请求异常进行处理。
- 对文件操作和数据处理异常进行处理。

## 三、项目结构

```text
day03/
├── main.py              # 主程序，负责调度各个模块
├── api_client.py        # API 请求模块
├── data_handler.py      # JSON 数据保存与读取模块
├── test_handler.py      # 数据保存与读取测试
└── data/
    ├── posts.json       # API 获取的文章数据
    ├── test.json        # 测试数据
    └── test/
        └── new_posts.json
```

## 四、核心知识点

### 1. HTTP 请求

使用 Requests 库发送 HTTP GET 请求：

```python
response = requests.get(url, timeout=10)
```

常用属性和方法：

| 方法或属性 | 作用 |
|---|---|
| `requests.get()` | 发送 GET 请求 |
| `response.status_code` | 获取 HTTP 状态码 |
| `response.raise_for_status()` | 检查 HTTP 请求状态 |
| `response.json()` | 将 JSON 响应解析为 Python 对象 |
| `response.text` | 获取响应文本 |

### 2. HTTP 状态码

| 状态码 | 含义 |
|---|---|
| 200 | 请求成功 |
| 201 | 资源创建成功 |
| 400 | 客户端请求错误 |
| 401 | 未授权 |
| 403 | 禁止访问 |
| 404 | 请求资源不存在 |
| 500 | 服务器内部错误 |

### 3. JSON 数据处理

JSON 和 Python 数据类型的转换：

| 方法 | 作用 |
|---|---|
| `json.dump()` | Python 对象转换为 JSON 并写入文件 |
| `json.dumps()` | Python 对象转换为 JSON 字符串 |
| `json.load()` | 从文件读取 JSON 并转换为 Python 对象 |
| `json.loads()` | 将 JSON 字符串转换为 Python 对象 |

特别注意：

`response.json()` 已经完成 JSON 解析，返回的是 Python 字典或列表，不需要再次使用 `json.loads()`。

### 4. 文件路径管理

使用 pathlib 管理文件路径：

```python
from pathlib import Path

file_path = Path("data/posts.json")

file_path.parent.mkdir(parents=True, exist_ok=True)
```

- `Path()`：创建路径对象。
- `parent`：获取父目录。
- `mkdir()`：创建目录。
- `parents=True`：允许创建多级目录。
- `exist_ok=True`：目录已存在时不报错。
- `exists()`：判断路径是否存在。

### 5. 异常处理

使用 try、except、else、finally 处理程序运行过程中可能发生的异常。

| 语句 | 作用 |
|---|---|
| `try` | 执行可能发生异常的代码 |
| `except` | 捕获并处理异常 |
| `else` | 没有异常时执行 |
| `finally` | 无论是否发生异常都会执行 |

本项目处理的异常包括：

- `ReadTimeout`：请求读取超时。
- `HTTPError`：HTTP 请求错误。
- `ConnectionError`：网络连接错误。
- `RequestException`：其他 Requests 请求异常。
- `OSError`：文件操作异常。
- `ValueError`：数据值或 JSON 格式异常。
- `TypeError`：数据类型错误。

## 五、核心代码

### 1. api_client.py

负责向 API 发送请求并获取数据。

```python
import requests

def fetch_post(url):
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data_dict = response.json()

    return data_dict
```

### 2. data_handler.py

负责 JSON 数据的保存和读取。

```python
import json
from pathlib import Path


def save_data(data, file_path):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def load_data(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
```

### 3. main.py

负责组织整个程序的执行流程。

主要流程：

1. 调用 `fetch_post()` 获取 API 数据。
2. 输入文件保存路径。
3. 调用 `save_data()` 保存数据。
4. 调用 `load_data()` 重新读取数据。
5. 输出文章相关信息。
6. 使用异常处理机制保证程序稳定运行。

## 六、API 测试

使用 JSONPlaceholder 提供的测试接口：

成功请求：

```text
https://jsonplaceholder.typicode.com/posts/1
```

不存在的文章：

```text
https://jsonplaceholder.typicode.com/posts/9999
```

### 测试一：API 请求成功

预期结果：

```text
用户 ID: 1
文章 ID: 1
文章标题: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
文章正文: quia et suscipit
...
程序运行结束！
```

### 测试二：多级文件夹自动创建

输入保存路径：

```text
day03/data/test/new_posts.json
```

程序自动创建不存在的目录，并成功保存文章数据。

### 测试三：HTTP 404 异常

预期结果：

```text
HTTP 请求错误： 404 Client Error: Not Found
程序运行结束！
```

说明程序能够正确捕获 HTTP 错误，并执行 finally 中的代码。

## 七、今日学习总结

今天完成了一个完整的 Python API 数据获取与本地存储小项目。

通过实践掌握了：

- 使用 Requests 进行 HTTP 网络请求。
- 使用 `response.json()` 解析 API 返回数据。
- 使用 `raise_for_status()` 检查 HTTP 请求状态。
- 使用 try-except-else-finally 处理异常。
- 使用 pathlib 管理文件路径。
- 使用 json.dump 和 json.load 实现 JSON 文件读写。
- 将程序拆分为多个模块，提高代码的可维护性。

### 今日最重要的收获

1. 理解了 HTTP 请求与 API 的基本工作流程。
2. 理解了 JSON 字符串、Python 字典和列表之间的转换关系。
3. 掌握了网络请求与文件操作中的基本异常处理。
4. 初步理解了 Python 项目中的模块化设计思想。

## 八、下一步学习计划

Day 4：Python 面向对象编程（OOP）

计划学习：

1. 类（Class）与对象（Object）
2. `__init__()` 构造方法
3. `self` 的作用
4. 实例属性与实例方法
5. 类与模块的组织方式
6. 使用类重构 API 数据获取项目

**阶段目标：从编写单个函数，逐步过渡到设计和组织完整的 Python 项目。**