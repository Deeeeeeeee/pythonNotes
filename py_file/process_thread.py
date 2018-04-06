"""
多进程/多线程
author: tankeryang
date: 2018-04-06
"""
import logging
import os
import time
import random
from multiprocessing import Process, Pool
logging.basicConfig(level=logging.INFO)


def run_task(process_name):
    logging.info('run child process [name: %s | pid: %s]' % (process_name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    logging.info('child process [name: %s | pid: %s] runs %.2f seconds' % (process_name, os.getpid(), end - start))


def create_child_process(process_name):
    logging.info('current parent process [name: parent | pid: %s]' % os.getpid())
    p = Process(target=run_task, args=(process_name, ))
    logging.info('child process [name: %s] will start.' % (process_name))
    p.start()
    p.join()
    logging.info('child process [name: %s] end' % (process_name))


def create_process_pool(n_process):
    logging.info('current parent process [name: parent | pid: %s]' % os.getpid())
    pool = Pool(n_process)
    for i in range(n_process):
        pool.apply_async(run_task, args=(i, ))
    logging.info('watting for all child process done...')
    pool.close()
    pool.join()
    logging.info('all child process done.')


if __name__ == '__main__':
    # create_child_process('child')
    create_process_pool(4)
