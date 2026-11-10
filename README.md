# AI-Agent-Learning

> 从 Python 基础到 AI Agent 应用开发，通过持续学习、项目实践和工程化训练，逐步具备独立开发 AI Agent 应用的能力。

## 一、项目介绍

**AI-Agent-Learning** 是我的个人 AI Agent 学习项目，记录从 Python 基础、API 调用、LLM 应用开发，到 Agent、RAG 和工程化部署的完整学习过程。

本项目采用「理论学习 + 代码实践 + 独立项目」的方式推进，目标不是只会调用大模型 API，而是理解 AI Agent 的基本原理，并能够独立设计、开发、测试和部署实际应用。

### 学习目标

- 掌握 Python 项目开发基础。
- 理解 HTTP、REST API 和大模型 API 调用。
- 掌握 Prompt Engineering、Function Calling 和 Tool Calling。
- 理解 Agent 的工作流程、工具调用和状态管理。
- 掌握 RAG 知识库问答系统的基本开发方法。
- 学会使用 FastAPI 构建 AI 应用接口。
- 完成具有实际应用价值的 AI Agent 项目。
- 提升 Git、项目文档、调试和技术表达能力。

## 二、技术路线

```text
Python 基础
    ↓
Python 项目开发
    ↓
HTTP / REST API
    ↓
LLM API / Prompt Engineering
    ↓
Function Calling / Tool Calling
    ↓
AI Agent 核心原理
    ↓
RAG 知识库
    ↓
LangGraph / FastAPI
    ↓
数据库 / 测试 / Docker
    ↓
完整 AI Agent 项目
```

## 三、技术栈

| 技术 | 学习方向 |
|---|---|
| Python 3.11 | 核心开发语言 |
| VS Code | 开发环境 |
| Git / GitHub | 版本控制与项目管理 |
| Requests | HTTP 请求 |
| JSON | 数据交换与存储 |
| LLM API | 大语言模型接入 |
| Prompt Engineering | 提示词设计 |
| Function Calling | 模型工具调用 |
| LangGraph | Agent 工作流 |
| FastAPI | 后端 API 开发 |
| SQLite | 关系型数据存储 |
| Chroma | 向量数据库 |
| Pandas | 数据分析 |
| Matplotlib | 数据可视化 |
| Docker | 项目部署 |

## 四、学习进度

### 第一阶段：Python 项目开发基础

目标：具备独立编写 Python 小型项目的能力。

| 日期 | 学习内容 | 状态 |
|---|---|---|
| Day 1 | Python 基础、函数、列表、字典、文件操作、Git | ✅ 已完成 |
| Day 2 | 异常处理、模块、JSON、CRUD 操作 | ✅ 已完成 |
| Day 3 | HTTP 请求、Requests、API 数据处理 | ✅ 已完成 |
| Day 4 | 面向对象编程（OOP） | ⏳ 计划中 |
| Day 5 | Python 项目结构与综合练习 | ⏳ 计划中 |
| Day 6 | HTTP/API 综合实践 | ⏳ 计划中 |
| Day 7 | 阶段复习与项目整理 | ⏳ 计划中 |

### 第二阶段：LLM 应用开发

目标：能够使用大模型 API 开发具有实际功能的应用。

计划学习：

- 大语言模型 API 接入
- Prompt Engineering
- Messages 与上下文管理
- Token 与上下文窗口
- JSON 结构化输出
- Function Calling
- Tool Calling
- API 异常处理与调用限制

阶段项目：多工具 AI 助手。

### 第三阶段：AI Agent 核心原理

目标：理解 Agent 如何接收任务、选择工具、执行操作和返回结果。

计划学习：

- Agent 基本概念
- Agent Loop
- 工具注册与调用
- 任务拆解与规划
- 对话状态管理
- 工具执行结果验证
- 错误处理与执行限制
- 人工确认机制

阶段项目：个人任务管理 Agent。

### 第四阶段：RAG 知识库

目标：构建能够检索外部知识并基于资料回答问题的 AI 应用。

计划学习：

- PDF / Word 文档解析
- 文本清洗与分块
- Embedding 向量嵌入
- 向量数据库
- 相似度检索
- Top-K 检索
- RAG 工作流程
- 回答来源引用
- 无相关资料时拒绝编造答案

阶段项目：个人知识库问答 Agent。

### 第五阶段：工程化开发

目标：将 AI Agent 从简单脚本升级为可运行、可测试的应用服务。

计划学习：

- LangGraph 工作流
- FastAPI
- Pydantic
- SQLite
- 日志系统
- pytest 自动化测试
- Docker 部署
- API 接口设计
- 错误处理与项目文档

### 第六阶段：综合项目实战

目标：独立完成一个具有实际应用价值的 AI Agent 项目。

**主项目：智能数据分析 Agent**

计划实现：

1. 支持 CSV / Excel 文件上传。
2. 自动分析数据结构。
3. 检查缺失值和异常数据。
4. 计算基础统计指标。
5. 根据用户需求进行分组分析。
6. 自动生成数据图表。
7. 使用大模型理解用户分析需求。
8. Agent 自动选择合适的工具。
9. 输出分析结果和报告。

计划设计的工具：

```text
get_data_info       # 获取数据基本信息
check_missing      # 检查缺失值
calculate_statistics # 计算统计指标
group_by_analysis  # 分组分析
generate_chart     # 生成图表
export_report      # 导出分析报告
```

## 五、项目目录结构

随着学习推进，项目预计采用以下结构：

```text
AI-Agent-Learning/
│
├── README.md
│
├── day01/
│   └── README.md
│
├── day02/
│   ├── main.py
│   ├── calculator.py
│   ├── exception_test.py
│   ├── json_test.py
│   ├── manager.py
│   ├── storage.py
│   ├── data/
│   │   └── records.json
│   └── README.md
│
├── day03/
│   ├── main.py
│   ├── api_client.py
│   ├── data_handler.py
│   ├── data/
│   │   └── posts.json
│   └── README.md
│
├── day04/
│   └── README.md
│
├── projects/
│   ├── multi-tool-assistant/
│   ├── rag-knowledge-agent/
│   └── data-analysis-agent/
│
├── requirements.txt
│
└── .gitignore
```

说明：以上是计划中的整体目录结构，实际目录会根据学习进度逐步建立。

## 六、开发环境

当前主要开发环境：

- 操作系统：Windows
- Python：3.11.4
- IDE：Visual Studio Code
- 虚拟环境：`.venv`
- 版本管理：Git
- 代码托管：GitHub

创建虚拟环境：

```powershell
python -m venv .venv
```

激活虚拟环境：

```powershell
.venv\Scripts\Activate.ps1
```

安装依赖：

```powershell
pip install requests
```

查看已安装依赖：

```powershell
pip list
```

## 七、项目开发规范

1. 每个学习阶段建立独立目录。
2. 每个阶段编写对应的 README.md。
3. 尽量独立完成代码，不直接复制完整答案。
4. 遇到问题先定位原因，再修改代码。
5. 完成一个阶段后进行功能测试。
6. 使用 Git 记录重要开发进度。
7. 不将 API Key、密码等敏感信息提交到 GitHub。
8. 对重要函数和模块编写必要的注释。
9. 每个综合