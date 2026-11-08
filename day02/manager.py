'''
实现添加、查看、修改、删除学习记录操作
'''

"""
    1.添加学习记录
    :param records: 现有记录列表
    :param date: 学习日期
    :param content: 学习内容
    :param hours: 学习时长
    :return: 更新后的记录列表
    """
def add_record(records, date, content, hours):
    
    records.append({
        "date": date,
        "content": content,
        "hours": hours
    })
    return records

"""2.查看所有学习记录"""
def list_records(records):

    if not records:
        print("目前还没有学习记录！")
        return

    for index, record in enumerate(records, start=1):
        print(f"第 {index} 条学习记录")
        print("日期：", record["date"])
        print("内容：", record["content"])
        print("时长：", record["hours"], "小时")
        print("--------------------")

'''3.修改学习记录'''
def update_record(records, index, date, content, hours):
    if index < 0 or index >= len(records):
        print("记录编号不存在！")
        return records

    records[index] = {
        "date": date,
        "content": content,
        "hours": hours
    }

    print("学习记录修改成功！")

    return records

'''4.删除学习记录'''
def delete_record(records, index):
    if index < 0 or index >= len(records):
        print("记录编号不存在！")
        return records

    # records.pop(index)删除指定索引的记录
    deleted_record = records.pop(index)

    print("删除成功：", deleted_record["content"])

    return records