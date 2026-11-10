# AI Agent 应用开发实习 · 路线图

> 最后校准：2026-11-09（Day03）
> 目标：**12/15 开始投递，12 月底前面试**
> 节奏：每周 30h+，每天约 6 小时

---

## 一、当前坐标

| 项 | 状态 |
|---|---|
| Day01（11/07） | 变量、列表、文件读写、基础函数 ✅ |
| Day02（11/08） | 字典、函数、异常、JSON、模块化（main/manager/storage 分层）✅ |
| Day03（11/09） | requests GET + JSON 解析 🚧 进行中 |
| 累计投入 | 2 天 |
| 距投递 | **36 天** |

### 已经具备（超出同龄人平均水平的部分）

- 能把一个需求拆成**入口 / 业务逻辑 / 数据持久化**三个文件，这是很多工作一年的人都做不到的
- README 写得结构化、有表格有目录树，这个习惯会直接变成面试时的沟通加分
- 文件读写、JSON 序列化、异常捕获都动手写过，不是只看过

### 还缺的（按对后面 RAG/Agent 的阻塞程度排序）

| 缺口 | 卡在哪 | 补的时机 |
|---|---|---|
| **类与对象** | RAG 里要封装 Retriever、Agent 里要封装 Tool，全是类 | Day04 必须补 |
| **类型标注 + pydantic** | 结构化输出、工具参数校验的地基 | Day05 |
| **HTTP 细节**（timeout / 状态码 / 异常 / headers） | 调任何大模型 API 都会遇到 | Day03 今天 |
| **虚拟环境与依赖管理**（requirements.txt / .env） | 别人跑不起来你的项目 = 项目等于没做 | Day05 |
| **logging** | 排查"模型为什么这么回答"必须靠日志 | Day05 |
| **推导式 / 生成器** | 数据清洗、批量处理会反复用到 | 随用随补 |

---

## 二、五个冲刺段

> 原计划的第一周（11/10 起）已经作废，换成下面这版——因为你需要先把「类 + 工程规范」补上，否则 RAG 阶段会写成一堆函数互相传参。

### 冲刺 A · 11/09 – 11/15（Day03–Day09）
**Python 收尾 + 打通大模型 API**

目标：能自己写出一个带流式输出的 CLI 多轮对话工具。

| 日 | 日期 | 任务 | 产出 |
|---|---|---|---|
| Day03 | 11/09 | requests 打透：GET 加 params、POST 发 JSON、headers、timeout、状态码、异常；**收尾用 requests 直接调一次大模型 API** → 明细见 [day03/TASKS.md](./day03/TASKS.md) | `day03/llm_call.py` 打印出模型回复 |
| Day04 | 11/10 | 类与对象：`__init__`、实例属性、方法、继承；把 Day02 的记录系统重构成 `class RecordManager` | `day04/` 重构版，功能不变 |
| Day05 | 11/11 | 工程规范：`requirements.txt`、`.env` + `python-dotenv`、`logging`、`pydantic` 校验返回数据 | 项目能"克隆即运行" |
| Day06 | 11/12 | LLM 第一课：token、消息角色、temperature、上下文窗口、流式输出原理 | `day06/chat_cli.py` 多轮 + 流式 |
| Day07 | 11/13 | Prompt 工程：五段式结构、JSON Schema 约束输出、失败重试 | JD 结构化解析器 |
| Day08 | 11/14 | 机动补课 + 把 A 阶段代码整理成统一仓库结构 | — |
| Day09 | 11/15 | 复盘 + 写本周 README + 八股第一页（Attention 直觉） | 阶段小结 |

**硬截止：11/15 之后不再系统学 Python 语法。** 后面所有缺口都靠项目里现学。

---

### 冲刺 B · 11/16 – 11/22（Day10–Day16）
**RAG 全链路 + 上线 → 作品集项目 ①**

| 日 | 任务 | 产出 |
|---|---|---|
| Day10 | Embedding 原理、余弦相似度、调 embedding 接口 | 相似度 demo |
| Day11 | 三种切分策略对比；numpy 手写暴力检索 → 换 FAISS/Chroma | 检索对比表 |
| Day12 | RAG v1 打通：解析 → 切分 → 入库 → 召回 → 生成 | 能回答你的课程资料 |
| Day13 | 优化：混合检索、rerank、查询改写、引用溯源 | v2 + 前后对比数字 |
| Day14 | 40 条评测集 + 命中率/忠实度/拒答率 | 评测报告 |
| Day15 | FastAPI + Streamlit + Docker + 公网部署 | **一个能点开的链接** |
| Day16 | 复盘 + 写 3 条量化简历句 | README |

**验收：面试官问"你 78% 的命中率怎么算的、剩下 22% 错在哪"，你能立刻答出来。**

---

### 冲刺 C · 11/23 – 11/29（Day17–Day23）
**Agent 核心 + MCP → 作品集项目 ②**

| 日 | 任务 | 产出 |
|---|---|---|
| Day17 | Function Calling 手写（不用框架）：schema → tool_calls → 回填 | 单工具 demo |
| Day18 | 手写 ReAct 循环（Thought/Action/Observation）+ 最大步数/超时/死循环保护 | ~80 行 react_agent |
| Day19 | LangGraph：State/Node/Edge/条件边/Checkpointer | 同一任务两版实现 |
| Day20 | 多工具（搜索/SQL/文件）+ 短期长期记忆 + 人工确认 | agent_v2 |
| Day21 | MCP 协议 + 写一个自己的 MCP server | 被外部客户端调用成功 |
| Day22 | 多智能体编排 + 失败重规划 + 流式 | multi_agent |
| Day23 | 录 2 分钟 demo + 架构图 | README 顶部 GIF |

---

### 冲刺 D · 11/30 – 12/06（Day24–Day30）
**工程化 + 评测 → 作品集项目 ③**

| 日 | 任务 | 产出 |
|---|---|---|
| Day24 | FastAPI 服务化：异步、SSE、错误码、鉴权 | API 文档 |
| Day25 | Docker compose + 部署上线 | 一条命令跑起来 |
| Day26 | 可观测：tracing 记录每步 prompt/token/耗时 + 成本核算 | trace 截图 |
| Day27 | 评测流水线：任务集 → rubric → 3 个 grader | 一键评测 |
| Day28 | badcase 归因 20 个，修 3 个并复测 | 分析报告 |
| Day29 | 三个项目 README 统一 + GitHub 首页索引 | 3 分钟看懂你 |
| Day30 | 机动 | — |

---

### 冲刺 E · 12/07 – 12/14（Day31–Day38）
**简历 + 面试 + 开投**

| 日 | 任务 |
|---|---|
| Day31 | 简历 v1（一页，项目占 60% 篇幅） |
| Day32 | 简历 v2：对齐 JD 关键词 + 两版自我介绍 |
| Day33 | 八股第一轮：原理 |
| Day34 | 八股第二轮：项目深挖 20 问 |
| Day35 | 模拟面试 2 场 + 录音回听 |
| Day36 | 投递清单（郑州 8–10 家 + 外省 5–6 家） |
| Day37 | 投递追踪表 + 定制话术 |
| **12/15** | **首日投 20 家** |

---

## 三、今日（Day03）具体做什么

你现在的 `main.py` 已经能拿到一条 post 了。接下来按顺序加，每加一步都跑一次：

**1. 先改个笔误**：`respones` → `response`。变量名拼错不影响运行，但面试官看代码时会觉得不够严谨。

**2. 加参数，从"取一条"变成"取一组"**

```python
params = {"userId": 1, "_limit": 3}
response = requests.get("https://httpbin.org/get", params=params, timeout=10)
data = response.json()
print(response.url)      # https://httpbin.org/get?userId=1&_limit=3
print(data["args"])      # {'userId': '1', '_limit': '3'} —— 注意值都变成了字符串
```

> 用 httpbin 而不是原计划的 jsonplaceholder，是因为后者在你这条线路上不可达（实测 8 秒超时）。httpbin 会把参数原样回显，反而更适合验证 `params`。

**3. 加超时和异常**——这是今天最重要的一个习惯

```python
import requests

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()      # 4xx/5xx 主动抛异常
    data = response.json()
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as e:
    print("状态码异常：", e)
except requests.exceptions.RequestException as e:
    print("网络异常：", e)
```

**4. 学 POST**（大模型 API 全是 POST）

```python
response = requests.post(
    "https://httpbin.org/post",
    json={"title": "foo", "body": "bar", "userId": 1},
    timeout=10,
)
data = response.json()
print(data["json"])          # 服务端收到的 body 被原样解析回来
print(data["headers"]["Content-Type"])   # application/json
```

> 注意 `headers` 会自动出现 `Content-Type: application/json` —— 这是 `json=` 参数帮你加的，不用手写。

**5. 关键一步：用 requests 直接调大模型**

调 LLM 和调上面这个接口**没有任何区别**，只是 body 长得不一样、headers 里多一个 key：

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "用一句话解释什么是 RAG"}
        ],
    },
    timeout=60,
)
print(response.json()["choices"][0]["message"]["content"])
```

做到这里，你就是"能用原生 HTTP 调通大模型"的人了——这比装个 SDK 就 `client.chat()` 调一句的人懂得多。

**6. 写 `day03/README.md`**（现在是空的），至少记四件事：requests 的四个关键参数、状态码含义、为什么要设 timeout、以及"调 LLM = 调一个 POST 接口"这个认知。

> **API Key 注意**：`.gitignore` 已经包含 `.env`，很好。但**不要把 key 写进 .py 文件**，一旦提交上 GitHub，机器人几分钟内就会扫到并盗刷。注册 DeepSeek 或阿里云百炼拿一个 key，先充 10 块钱够用很久。

---

## 四、几条硬规则

1. **40 分钟规则**：任何单点卡住超过 40 分钟，立刻换路（换库、换方案、先用 mock 顶过去），周五统一收拾。基础弱的人最大的时间黑洞是环境问题。
2. **每天必须有一个能跑的 commit**，允许丑，不允许"明天一起写"。
3. **commit message 格式统一**：`feat(day03): 用 requests 调通 DeepSeek API`。你现在的 `Complete Day 1 Python basics` 已经不错，加上范围前缀会更专业。
4. **每个 day 目录必须有 README**，写清"今天学了什么、卡在哪、怎么解决的"。第 5 周写简历时，这些 README 就是素材库。
5. **不要为了完美回头改旧代码**。Day02 的代码现在看着粗糙是正常的，等 Day05 学完类和 pydantic，再回头一次性重构。

---

## 五、视频资源（B站，2026-11-09 实测在架）

> **使用原则**：视频只当"卡住时的解释器"，不当主教材。只在两种情况打开它——① 某个概念看文档看不懂；② 报错搜不到原因。看完那几集就关掉，回去写代码。
> **绝对不要通刷**：下面任何一套的完整时长都在 17 小时以上，通刷一遍你这 5 周就废了。

| 用途 | 课程 | UP 主 | 数据 | 什么时候看 |
|---|---|---|---|---|
| 类与对象、异常、文件（补 Day04） | 黑马程序员 Python 600 集（`BV1ex411x7Em`） | 黑马程序员 | 2086 万播放 | **按章节跳看**，只挑「面向对象」「异常处理」那几节 |
| Python 概念看不懂时 | 《零基础入门学习Python》最新版（`BV1c4411e77t`） | 鱼C-小甲鱼 | 1386 万播放，17.5h | 随查随看，别从头跟 |
| **Agent/LangChain 主线** | 黑马 2026 LangChain+LangGraph 实战（`BV178w1z7EHQ`） | 黑马程序员 | 206 万播放，87P/22.5h | 11/16 起，**按 5.0 的分P清单挑着看** |
| **补丁：中间件/记忆/Pydantic** | 尚硅谷 2026 LangChain 教程（`BV1rv7A6oEeP`） | 尚硅谷 | 272 万播放，120P/21.4h | 卡在哪补哪，别当主线 |
| 想要更深的框架理解 | 楼兰 LangChain 系统教程（`BV1cCd6YwE4n`） | 楼兰架构师 | 4.8 万播放，6.9h | 有余力再看，讲得比上面两套细但节奏慢 |

**如果只能记住一句话**：Day04 缺的那点「类」，去黑马那 600 集里挑 3–4 节看完就够，剩下的时间继续写代码。

### 5.0 两套主力课的分工（`BV178w1z7EHQ` vs `BV1rv7A6oEeP`，2026-11-09 核实）

两套都是真课，投币都过万，**不是二选一，是分工**。

| 维度 | 黑马 `BV178w1z7EHQ`（87P / 22.5h / 206万播放） | 尚硅谷 `BV1rv7A6oEeP`（120P / 21.4h / 272万播放） |
|---|---|---|
| 发布 | 2026-03 | 2026-06（更新） |
| 节奏 | 均 16 min/P，讲得慢、铺垫足 | 均 11 min/P，速度快、点密集 |
| **RAG** | **✅ 强（P44–P70，27P≈6.5h）**：Milvus 稀疏+稠密向量、**混合检索、RRF 融合、Reranker**、2Step / AgenticRAG | ⚠️ 基础（P102–P120，19P）：加载→切分→向量化→入 Milvus→检索，**没有混合检索和 Reranker** |
| **LangGraph** | **✅ 独立一章（P71–P86，16P≈3.5h）**：Node / State+Reducer / 条件边 / Command 路由 / 子图嵌套 | ❌ 无独立章节（1.x 的 `create_agent` 底层即 LangGraph） |
| **中间件** | 4 节（P32–P37，HITL / 自定义 / 条件跳转） | **✅ 19 节（P64–P85）**：Summarization / PII / TodoList / Token 限流 / Fallback / ToolRetry / wrap_model_call / hook 执行顺序 |
| **记忆** | 3 节（P21–P23） | **✅ 16 节（P86–P101）**：PostgreSQL 持久化、消息裁剪/删除/摘要治理、长期记忆 Store |
| **Pydantic** | 未单独讲 | **✅ 10 节（P41–P50）**：可选字段 / 枚举 / 嵌套 / 限制条件 / 四种类型校验对比 |
| **MCP** | **✅ 3 节（P39–P41，≈51min）** | ❌ 完全没有 |
| **多智能体** | ✅ 2 节（P42–P43，婚礼策划案例） | ❌ 无 |
| AI 通识 | ✅ P2–P13（神经网络原理 / LLM / API 规范） | ❌ 无（直接进 LangChain） |
| 收尾项目 | AI私厨、婚礼策划（小案例） | Assistant 客服知识库（Milvus 端到端） |

**结论：主线用黑马，补丁用尚硅谷。** 理由是你那 11 份 JD 里出现频率最高的是 RAG 全链路、LangGraph、MCP——这三项黑马都更强；而尚硅谷赢在中间件和记忆系统，那是"能讲出工程深度"的部分，但不是投简历的门槛。

**黑马按这个顺序看（合计约 12h，不是 22.5h）**

| 分P | 内容 | 时长 | 必看理由 |
|---|---|---|---|
| P1–P13 | AI 通识 + API 规范 | ~2.6h | 面试八股直接能用（Transformer / 会话记忆 / 接口规范） |
| P14–P28 | LangChain 入门 + AI私厨实战 | ~5h | 打底，跟你的 `api_client.py` 正好接上 |
| P39–P41 | **MCP** | 51min | JD 加分项，别跳 |
| P44–P56 | RAG 基础 + 加载器 + 切分 + 向量化 | ~3h | 你第 2 周手写 RAG 的理论对照 |
| P57–P60 | **RAG Agent（2Step / AgenticRAG）** | 1.2h | 面试高频："你的 RAG 和普通 RAG 有什么区别" |
| P61–P69 | **Milvus 混合检索 / RRF / Reranker** | 2.3h | **最值钱的 2 小时**，把你的作品①从"玩具"拉到"工业级" |
| P71–P86 | LangGraph | 3.5h | 第 3 周 Agent 项目的骨架 |

**跳过**：P29–P38（Runtime/Middleware，尚硅谷讲得更透）、P42–P43（MultiAgent，等你做完单 Agent 再看）、P70（1 分钟过渡）。

**尚硅谷只抽这三段（合计约 7h，其余全不看）**

| 分P | 内容 | 时长 | 什么时候看 |
|---|---|---|---|
| P41–P50 | Pydantic + 结构化输出（4 种策略） | ~1.7h | **11/10–11/12 就用得上**，正好补 Day04 的类和类型标注 |
| P64–P85 | 中间件（挑 HITL / Summarization / ToolRetry / wrap_model_call） | ~2h | 11/24 之后，做 Agent 项目的容错和人工审核时 |
| P86–P101 | 记忆系统（PostgreSQL / 消息治理 / 长期记忆） | ~2.5h | 12/01 之后，做多轮对话和部署时 |

**三个必须知道的坑**

1. **黑马标题夸大**：「到 LangSmith 的监控、调试、**评估**一套搞定」——实际 LangSmith 只有 P26 一节 20 分钟，**全课没有 rubric、LLM-as-Judge、Benchmark 内容**。评估这块你得自己补（我在第 4 周计划里单独留了时间），而这恰恰是曼孚科技 250–450/天那个岗位的核心要求。
2. **两套课都用 LangChain 1.x 新 API**（`create_agent` + middleware）。你在网上搜到的绝大多数博客还是 0.3 版（`AgentExecutor` / `create_react_agent`），**代码对不上不是你写错，是版本不同**。以课程和官方文档为准。
3. **两套都没有完整部署上线**（Docker + FastAPI + 公网）。尚硅谷有腾讯云和 PostgreSQL 的部署片段，但不成体系。Docker 这块你第 4 周要自己啃，别指望课程。

### 5.1 遇到营销号课程怎么 30 秒判断（2026-11-09 实例复盘）

> 案例：`BV16aDpB4Er6`《【全748集】目前B站最全最细《AI大模型应用开发》教程…7天就能从小白到大神！少走99%的弯路！》
> UP 主"吴恩达langchain"（mid 3493259842160936）**不是吴恩达本人，也不是 DeepLearning.AI 官方**，是蹭名字的搬运号。

五个信号，命中两个以上直接跳过：

| # | 信号 | 本例实测 |
|---|---|---|
| 1 | 标题含"全XXX集 / B站最全 / 7天从小白到大神 / 少走99%弯路 / 存下吧很难找全" | 全中 |
| 2 | 宣称集数 ≠ 实际分P | 标题 748 集，实际 **102 个分P** |
| 3 | **弹幕数 < 播放量的 0.5%**（说明几乎没人真看下去） | 14.3 万播放 / **260 条弹幕**（0.18%） |
| 4 | 赞播比 < 2%，且收藏远高于点赞（收藏是"mark 一下以后看"，不是"看完了"） | 点赞 1522（1.06%），收藏 6870 |
| 5 | 描述/置顶写"三连 + 置顶自取资料 / 加群" | 中：引流私域 |
| 6 | 热评在问"有看完的吗"却没人回答 | 中：3 赞热评，零回复 |

对照一下同主题的真课：黑马 600 集 2086 万播放，尚硅谷 LangChain 272 万播放——差两个数量级。

**另外，这个号的内容框架停留在 2024 年**：讲 OpenAI Swarm（2025-03 已被 Agents SDK 取代）、Agent Tuning（微调 Agent，实习岗完全用不上）、CrewAI（JD 里要的是 LangGraph / LangChain）。49.5 小时通刷一遍，换不来一个能写进简历的项目。

---

## 六、投递时的目标清单（提前存着）

| 档位 | 公司 | 岗位 |
|---|---|---|
| 保底 | 浩鲸云（郑州经开区） | 人工智能实习生 120–200/天 |
| 主攻 | 新开普（郑州高新区） | AI应用开发/智能体开发实习生 150–180/天，6 个月 |
| 主攻 | 河南特立达（郑东新区） | AI Agent 开发工程师（实习）200–400/天 |
| 主攻 | 杭州先进编译郑州分公司 | 大模型应用开发（大三优先）可签三方 |
| 主攻 | 曼孚科技（郑州金水） | 大模型评测实习生 250–450/天，3 个月 |
| 冲刺 | 360 武汉 | AI应用开发实习生 220–240/天 |
| 冲刺 | 智矩 杭州 | AI Agent 开发实习生（Python/LangGraph） |
| 彩票 | 字节跳动 北京 | AI Agent 全栈工程师实习生 500–550/天 |

---

## 七、里程碑自查

- [ ] 11/15 —— 能用原生 requests 调 LLM，写出带流式的 CLI 多轮对话
- [ ] 11/22 —— RAG 项目上线，有公网链接，有 40 条评测数字
- [ ] 11/29 —— Agent 项目能被外部 MCP 客户端调用
- [ ] 12/06 —— 三个项目有统一 README + 可观测截图 + badcase 报告
- [ ] 12/14 —— 简历定稿，八股两轮过完，模拟面 2 场
- [ ] 12/15 —— 首日投出 20 份
