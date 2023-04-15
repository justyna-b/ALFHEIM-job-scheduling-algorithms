from time import perf_counter

from .johnson_asynchronous import Johnson_asynchronous
from .johnson_synchronous import Johnson_synchronous

if __name__ == "__main__":
    j_async = Johnson_asynchronous()
    j_sync = Johnson_synchronous()

    start = perf_counter()
    gantt_chart_sync = j_sync.schedule()
    end = perf_counter()
    print(f"Synchronous tasks scheduling: time = {end-start}")

    start = perf_counter()
    gantt_chart_async = j_async.schedule()
    end = perf_counter()
    print(f"Asynchronous tasks scheduling: time = {end-start}")


