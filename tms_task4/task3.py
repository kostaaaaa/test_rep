from datetime import datetime
import time
def show_time():
    now = datetime.now()
    time.sleep(1)
    return now.strftime("%H:%M:%S")

time_gen = [show_time() for i in range(1, 10)]
print(time_gen)