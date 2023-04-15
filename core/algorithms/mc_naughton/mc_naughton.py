class Mc_naughton():

    def __init__(self, machines) -> None:
        self._machines_num = machines
        self._min_completion_time = None

    def _count_min_completion_type(self, tasks, machines_num):
        summary = 0
        longest_task = tasks[0]
        for task in tasks:
            summary += task
            longest_task = task if task > longest_task else longest_task
        return max(longest_task, summary/machines_num)

    def _schedule_on_machine(self, tasks):
        machine_time = 0
        machine = 1
        for task in tasks:
            pass_min_c_time = (machine_time + task) < self._min_completion_time
            if pass_min_c_time:
                print(f"Machine number: {machine} task: {task}")
                machine_time += task
            else:
                print(f"Machine number: {machine} task: {task} its part: {machine_time}")
                machine += 1

    def main(self):
        tasks = [1,2,3,4,9,18,5,21,7,1]
        self._min_completion_time = self._count_min_completion_type(tasks=tasks,machines_num=self._machines_num)
        self._schedule_on_machine(tasks=tasks)


if __name__ == "__main__":
    mc_ng = Mc_naughton(2)
    mc_ng.main()