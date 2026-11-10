'''
封装 JSON 读取和保存
'''
import json
from pathlib import Path

# 获取当前文件所在目录
# Path(__file__).parent: 它表示当前 Python 文件所在的文件夹。
BASE_DIR = Path(__file__).parent

# JSON 文件路径
RECORDS_FILE = BASE_DIR / 'data' / 'records.json'

# 确保 data 文件夹存在
RECORDS_FILE.parent.mkdir(parents=True, exist_ok=True)

# 读取学习记录
def load_records():
    if not RECORDS_FILE.exists():
        return []
    with open(RECORDS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
# 保存学习记录
def save_records(records):
    with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            records,    
            f,
            ensure_ascii=False,
            indent=4
        )
    

