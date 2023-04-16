from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import itertools

class Inefficient_asynchronous():

    def __init__(self, tasks=[2,4,1,3,2,2,1,4,5]) -> None:
        self._tasks = tasks

    def _create_combinations_of_tasks(self, tasks):
        tasks_combinations = []
        n = len(tasks)
        for task_idx in range(n + 1):
            for subset in itertools.combinations(tasks, task_idx):
                tasks_combinations.append(subset)
        return tasks_combinations

    def _count_possible_min_c_time(self, combination, tasks):
        correct_combinations = []
        if sorted(combination[0] + combination[1]) == sorted(tasks):
            min_c_time = self._count_completion_time(combination)
            correct_combinations.append((min_c_time, combination))
        return correct_combinations

    def _count_completion_time(self, combination):
        c_time_first_machine = sum(combination[0])
        c_time_second_machine = sum(combination[1])
        min_c_time = max(c_time_first_machine, c_time_second_machine)
        return min_c_time

    def _get_shortest_schedule(self, c_times):
        return sorted(c_times, key=lambda x: x[0])[0]

    def schedule(self):
        all_combinations = self._create_combinations_of_tasks(self._tasks)
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._count_possible_min_c_time, combination, self._tasks)
                       for combination in itertools.combinations(all_combinations, 2)]
            res = []
            for future in as_completed(futures):
                if len(list(future.result())) > 0:
                    res.append(future.result())
        shortest_schedule = self._get_shortest_schedule(res)
        return shortest_schedule[0][0], shortest_schedule[0][1]

if __name__ == "__main__":
    i_a = Inefficient_asynchronous()
    print("OK")
    i_a.schedule()
