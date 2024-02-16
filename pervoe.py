import threading
import time
def dela():
    time.sleep(1)
    with open('file.txt', 'w') as f:
        f.write('sozdan')
    print(f'file - {threading.current_thread().name}')

def threaded():
    time.sleep(1)
    with open('file.txt', 'w') as f:
        f.write('sozdan')
    print(f'file - {threading.current_thread().name}')

start_time = time.time()
threads = []
for _ in range(100):
    thread = threading.Thread(target=threaded, name=f'{_}')
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f'multi {end_time - start_time} seconds')
