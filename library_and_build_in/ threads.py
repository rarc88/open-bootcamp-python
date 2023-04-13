import _thread
import time


def currentTime(name, sleepTime):
    time.sleep(sleepTime)
    print(f'Thread: {name}, time: {time.ctime(time.time())}')


_thread.start_new_thread(currentTime, ('t1', 1))
_thread.start_new_thread(currentTime, ('t2', 2))

print('Body End')
time.sleep(30)
