import threading
from queue import PriorityQueue
from threading import Thread, current_thread
from time import sleep
from typing import Callable


def threadify(func: Callable, args_list: list[tuple]):
    results_q = PriorityQueue(len(args_list))
    
    def do_func(priority, args):
        results_q.put((priority, func(*args)))

    for priority, args in enumerate(args_list):
        Thread(target=do_func, args=(priority, args), daemon=True).start()

    for t in threading.enumerate():
        if t != current_thread():
            t.join()
    
    return [results_q.get()[1] for _ in args_list]

print(threadify(lambda x: (x, sleep(x))[0], [(x,) for x in range(5)]))
