from concurrent.futures import ThreadPoolExecutor
import operator

from .johnson import Johnson

class Johnson_asynchronous(Johnson):

    def __init__(self) -> None:
        super().__init__()

    def _select_tasks_shorter_on_machines(self,
                                          tasks_on_single_machine,
                                          tasks_on_second_machine,
                                          operation):
        n = self.tasks_num
        l = []
        ops = {'<': operator.lt,'<=': operator.le}
        for task_idx in range(0, n):
            task_on_first_machine = tasks_on_single_machine[task_idx]
            task_on_second_machine = tasks_on_second_machine[task_idx]
            if ops[operation](task_on_first_machine, task_on_second_machine):
                l.append(task_on_first_machine)
        return l

    def _sort_tasks_on_machine(self,
                               tasks_on_single_machine,
                               rev_order):
        return sorted(tasks_on_single_machine, reverse=rev_order)

    def schedule(self):
        with ThreadPoolExecutor() as executor:
            shorter_on_machines = executor.map(self._select_tasks_shorter_on_machines,
                                               self.tasks,
                                               self.tasks[::-1],
                                               ["<", "<="])
            shorter_on_machines = list(shorter_on_machines)
            shorter_on_machines_sorted = executor.map(self._sort_tasks_on_machine,
                                                      shorter_on_machines,
                                                      [False, True])
            return list(shorter_on_machines_sorted)
