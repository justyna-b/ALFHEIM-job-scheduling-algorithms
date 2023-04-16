from time import perf_counter

from .inefficient_asynchronous import Inefficient_asynchronous
from .inefficient_synchronous import Inefficient_synchronous

if __name__ == "__main__":
    i_s = Inefficient_synchronous()
    start = perf_counter()
    c_time, gantt_chart = i_s.schedule()
    end = perf_counter()
    print(gantt_chart)
    print(f"(Inefficient) Synchronous tasks scheduling: time = {end-start}")

    i_a = Inefficient_asynchronous()
    start = perf_counter()
    c_time, gantt_chart = i_a.schedule()
    end = perf_counter()
    print(gantt_chart)
    print(f"(Inefficient) Asynchronous tasks scheduling: time = {end-start}")
