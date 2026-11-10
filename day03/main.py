# import requests
# try:
#     # url = "https://jsonplaceholder.typicode.com/posts/1"
#     url = "https://jsonplaceholder.typicode.com/posts/1"

#     # requests.get(): 发送请求、接收服务器响应
#     # response.status_code: 获取 HTTP 状态码
#     # response.raise_for_status(): 检查状态码，遇到 4xx 或 5xx 时抛出 HTTPError
#     response = requests.get(url, timeout=10)
#     print(response.status_code)
#     response.raise_for_status()
#     # print(response.json())

#     # 把 API 返回的数据保存到 data
#     data = response.json()

#     print(f"用户 ID: {data['userId']}")
#     print(f"文章 ID: {data['id']}")
#     print(f"文章标题: {data['title']}")
#     print(f"文章正文: {data['body']}")

# except requests.exceptions.ReadTimeout:
#     print("请求超时，请稍后重试！")
# # 变量e：获取报错信息
# except requests.exceptions.HTTPError as e:
#     print("HTTP 请求失败：", e)
# except requests.exceptions.ConnectionError:
#     print("请检查网络或服务器连接不稳定！")
# # 增加通用异常兜底
# except requests.exceptions.RequestException as e:
#     print("其他网络请求错误：", e)

from api_client import fetch_post
import requests
from data_handler import save_data, load_data

url = "https://jsonplaceholder.typicode.com/posts/9999"


try:

    data = fetch_post(url)

except requests.exceptions.ReadTimeout:
    print("请求超时，请稍后重试！")
except requests.exceptions.HTTPError as e:
    print("HTTP 请求错误：", e)
except requests.exceptions.ConnectionError:
    print("请检查网络或服务器连接不稳定！")
except requests.exceptions.RequestException as e:
    print("其他网络请求错误：", e)

else:
    try:
        file_path = input("请输入想要保存数据的路径：")
        save_data(data, file_path)
        saved_data = load_data(file_path)
        print(f"用户 ID: {saved_data['userId']}")
        print(f"文章 ID: {saved_data['id']}")
        print(f"文章标题: {saved_data['title']}")
        print(f"文章正文: {saved_data['body']}")
    # OSError : 文件或操作系统层面的操作错误
    # TypeError : 数据类型不符合操作要求
    except OSError as e:
            print("请输入有效路径地址！")
    except (ValueError, TypeError) as e:
        print("数据处理失败", e)
    
finally:
    print("程序运行结束！")




