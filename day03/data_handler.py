import json
from pathlib import Path

# # 获取当前文件所在目录
# # Path(__file__).parent: 它表示当前 Python 文件所在的文件夹。
# BASE_DIR = Path(__file__).parent

# # JSON 文件路径
# RECORDS_FILE = BASE_DIR / 'data' / 'posts.json'

# # 确保 data 文件夹存在
# # parents=True：如果上级目录不存在，也一起创建。
# # exist_ok=True：如果目录已经存在，不报错。
# RECORDS_FILE.parent.mkdir(parents=True, exist_ok=True)


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
        # json.load() 和 json.loads() 都是 Python 中用于 JSON → Python 数据 的方法
        # json.load()：一个读取文件
        # json.loads()：一个读取字符串
        return json.load(f)
    
    



