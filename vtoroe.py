import time
import threading
import random

def create_file_with_random_number_threaded():
    random_number = random.randint(0, 1000)
    file_name = f'{random_number}.txt'

    with open(file_name, 'w') as file:
        file.write(str(random_number))

    time.sleep(1)

start_time = time.time()

threads = []

for _ in range(1000):
    thread = threading.Thread(target=create_file_with_random_number_threaded)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
execution_time = end_time - start_time
print(f'{execution_time} seconds')
#НЕ ЗАПУСКАЙТЕ КОД БУДЕТ 1000 ФАЙЛОВ