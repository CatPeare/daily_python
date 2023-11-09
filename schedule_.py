# pip install schedule
import time
import schedule



# print(current_time_in_human_readable_format)

def current_time():
    current_time_in_human_readable_format = time.strftime("saat %H:%M:%S ve ben pisimi bu saatte de çok seviyorum", time.localtime())
    print(current_time_in_human_readable_format)

schedule.every(0.01).minutes.do(current_time)

while True:
    schedule.run_pending()
    time.sleep(1)
