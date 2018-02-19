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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


def call_create_dict(isCalling):
    """
    电话作为键，通话时间作为值，生成字典。电话包括主叫电话和被叫电话电话。
    :param isCalling: 是主叫电话还是被叫电话
    :return:
    """
    if item[isCalling] in phone_time_dict:
        phone_time_dict[item[isCalling]] += int(item[-1])
    else:
        phone_time_dict[item[isCalling]] = int(item[-1])

#  new a dictionary with phone number ,duration time() as key and value
phone_time_dict = {}
max_time = 0
phone_list = []
for item in calls:
    call_create_dict(0)
    call_create_dict(1)
# circulate dict .so if duration time greater than max time set as zero ,new a phone number list and put phone number
# which has relationship with this duration time,then change max time into this current duration time; so if duration
# time is equal to max time and the phone number which has relationship with this duration time didn't existed in list,
# change max time into this current duration time
for phone in phone_time_dict:
    if phone_time_dict[phone] > max_time:
        phone_list = []
        phone_list.append(phone)
        max_time = phone_time_dict[phone]
    elif phone_time_dict[phone] == max_time and not (phone in phone_list):
        max_time = phone_time_dict[phone]

# at last ,circulate phone number list ,print each phone number in list and max time
for phone_item in phone_list:
    print("%s spent the longest time, %s seconds, on the phone during September 2016." % (phone_item, max_time))
