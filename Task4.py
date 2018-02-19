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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
# 遍历calls集合 ，将以140开头的的主叫电话装进集合中（可能推销电话集合）,同时将每一个集合对象的第二个元素存到一个列表中（被叫电话集合)
phone_called_set = set()
phone_likely_sell_set = set()
phone_sell_list = []
phone_text_set = set()
for item in calls:
    phone_called_set.add(item[1])
    if str(item[0]).startswith("140"):
        phone_likely_sell_set.add(item[0])

# 遍历 texts 集合，将发送，和接受的电话号码中装进另一个集合中（短信集合）
for phone_text in texts:
    phone_text_set.add(phone_text[0])
    phone_text_set.add(phone_text[1])
# 遍历可能推销集合，将那些既不在短信集合也不在被叫电话集合中的元素添加到推销集合中
for phone_likely_sell in phone_likely_sell_set:
    if not (phone_likely_sell in phone_called_set or phone_likely_sell in phone_text_set):
        phone_sell_list.append(phone_likely_sell)
# 排序，输出
print("These numbers could be telemarketers: ", phone_sell_list)
print(len(phone_sell_list))
