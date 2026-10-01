from datetime import datetime
import time

running = True

while(running):
    current_time = datetime.now().time()
    print(current_time)
    time.sleep(1)