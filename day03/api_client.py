import requests

def fetch_post(url):
    # 获取url地址数据
    response = requests.get(url, timeout=10)

    # 不需要打印HTTP状态码, 注释掉：实际项目中，负责请求的模块最好只负责请求，不负责展示结果。
    # print(response.status_code)

    # 检查状态码，遇到 4xx 或 5xx 时抛出 HTTPError
    response.raise_for_status()
    # response.json(): 将JSON数据转换成Python字典
    data_dict = response.json()
    return data_dict
    

