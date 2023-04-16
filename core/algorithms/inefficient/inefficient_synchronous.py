import itertools

class Inefficient_synchronous():

    def __init__(self, tasks=[2,4,1,3,2,2,1,4,5]) -> None:
        self._tasks = tasks

    def _create_combinations_of_tasks(self, tasks):
        tasks_combinations = []
        n = len(tasks)
        for task_idx in range(n + 1):
            for subset in itertools.combinations(tasks, task_idx):
                tasks_combinations.append(subset)
        return tasks_combinations

    def _select_correct_subsets(self, combinations, tasks):
        correct_combinations = []
        for combination in itertools.combinations(combinations, 2):
            if sorted(combination[0] + combination[1]) == sorted(tasks):
                correct_combinations.append(combination)
        return correct_combinations

    def _count_completion_times(self, correct_combinations):
        c_times = []
        for correct_combination in correct_combinations:
            c_time_first_machine = sum(correct_combination[0])
            c_time_second_machine = sum(correct_combination[1])
            c_times.append((max(c_time_first_machine, c_time_second_machine),
                            correct_combination))
        return c_times

    def _get_shortest_c_time(self, c_times):
        return sorted(c_times)[0]

    def schedule(self):
        all_combinations = self._create_combinations_of_tasks(self._tasks)
        correct_combinations = self._select_correct_subsets(all_combinations, self._tasks)
        c_times = self._count_completion_times(correct_combinations)
        shortest_c_time = self._get_shortest_c_time(c_times)
        return shortest_c_time[0], shortest_c_time[1]
