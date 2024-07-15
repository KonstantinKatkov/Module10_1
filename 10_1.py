
import time
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):

    file = open(file_name, mode='w', encoding='utf8')
    for i in range(1, word_count+1):
        file_content = f'Какое-то слово № {i} \n'
        file.write(file_content)
    file.close()
    print(f'Завершилась запись в файл {file_name}')
    time.sleep(0.1)

time_start_1 = time.time()

wite_words(10,'example1.txt')
wite_words(30,'example2.txt')
wite_words(200,'example3.txt')
wite_words(100,'example4.txt')

time_end_1 = time.time()
time_res_1 = time_end_1 - time_start_1

print(f'Работа потоков завершилась, время работы: {time_res_1} сек.')

time_start_2 = time.time()

thr_first =Thread(target=wite_words, args=(10,'example5.txt'))
thr_second =Thread(target=wite_words, args=(20, 'example6.txt'))
thr_third =Thread(target=wite_words, args=(200, 'example7.txt'))
thr_forth =Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_forth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_forth.join()

time_end_2 = time.time()
time_res_2 = time_end_2 - time_start_2
print(f'Работа потоков завершилась, время работы: {time_res_2} сек.')







