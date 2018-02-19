"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""


def extract_phone(calls_texts_list):
    """
        put phones  which call in and out  into a list
    :return: list.phone list which call in and out
    """
    call_list = []
    for call in calls_texts_list:
        call_list.append(call[0])
        call_list.append(call[1])
    return call_list


# put phones  which call in and out belong to calls into a list
calls_phone_list = extract_phone(calls)
# put phones  which call in and out belong to texts into a list
texts_phone_list = extract_phone(texts)
# combine these two lists and transform it into a set
all_phone_set = set(calls_phone_list.__add__(texts_phone_list))
# caculate the set'size and print
print('there are %d different telephone numbers in the records.' % len(all_phone_set))
