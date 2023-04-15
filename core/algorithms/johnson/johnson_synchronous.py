from .johnson import Johnson

class Johnson_synchronous(Johnson):

    def __init__(self) -> None:
        super().__init__()

    def _select_tasks_shorter_on_machines(self, n, tasks):
        shorter_on_first, shorter_on_second = [], []
        for task_idx in range(0, n):
            task_first_machine = tasks[0][task_idx]
            task_second_machine = tasks[1][task_idx]
            shorter_on_first.append(task_first_machine) if (task_first_machine <
                                                            task_second_machine) else None
            shorter_on_second.append(task_second_machine) if (task_first_machine >=
                                                              task_second_machine) else None
        return [shorter_on_first, shorter_on_second]

    def _sort_tasks_on_machine(self, tasks_first_machine, tasks_second_machine):
        return [sorted(tasks_first_machine, reverse=False),
                sorted(tasks_second_machine)[::-1]]

    def schedule(self):
        shorter_on_machines = self._select_tasks_shorter_on_machines(self.tasks_num,
                                                                     self.tasks)
        shorter_on_machines_sorted = self._sort_tasks_on_machine(shorter_on_machines[0],
                                                                 shorter_on_machines[1])
        return shorter_on_machines_sorted

