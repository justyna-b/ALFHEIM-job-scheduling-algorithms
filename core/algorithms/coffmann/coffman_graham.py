import numpy as np

from lib.util.adjacency_matrix_graph import Adjacency_matrix_graph


class Coffman_graham():

    def __init__(self) -> None:
        self._tasks_provider = Adjacency_matrix_graph(17)
        self._tasks = []
        self._list_to_schedule = []
        self._num_of_processors = 2

    def prepare_data(self):
        self._tasks = self._tasks_provider.create_example_graph()

    def _count_successors(self, tasks_matrix, node):
        tasks_matrix = tasks_matrix.transpose()
        return np.count_nonzero(tasks_matrix[node] == -1)

    def _add_nodes_label(self, nodes, label=0):
        if label == 0:
            for node_key in range(len(nodes)):
                nodes[node_key] = (nodes[node_key], label)
        for node_key in range(len(nodes)):
                nodes[node_key] = (nodes[node_key], self._count_successors(self._tasks, nodes[node_key]))
        return nodes

    def _get_predecessors_for_multiple_nodes(self, tasks_matrix, nodes_list):
        predecessors = []
        for node in nodes_list:
            predecessors.append(self._tasks_provider.get_predecessors(tasks_matrix, node))
        return predecessors

    def _flatten_array(self, list_to_flatten):
        return sum(list_to_flatten, [])

    def _choose_tasks_labeled_succ(self, tasks_matrix, possible_next_nodes, tasks_provider):
        next_nodes = []
        for p_n in possible_next_nodes:
            successors = tasks_provider.get_successors(tasks_matrix, p_n)
            if (set(successors).issubset(set(self._list_to_schedule))):
                next_nodes.append(p_n)
        return next_nodes

    def _sort_by_label_and_lex(self, nodes):
        return sorted(nodes, key=lambda x: (x[1], x[0]), reverse=False)

    def _flatten_without_labels(self, nodes):
        return [i[0] for i in nodes]

    def _check_if_ready(self, task):
        ready = self._tasks_provider.get_ready_tasks(self._tasks)
        ready = self._flatten_without_labels(ready)
        return task in ready

    def _schedule_task(self, task, machine, unscheduled_tasks):
        print(f"Task {task} assigned to machine {machine}.")
        self._tasks = self._tasks_provider.delete_task_from_graph(self._tasks, task)
        print(self._tasks)

    def _schedule_tasks(self):
        unscheduled_tasks = self._list_to_schedule[::-1]
        while len(unscheduled_tasks) > 0:
            for i in range(len(unscheduled_tasks)):
                is_ready = self._check_if_ready(unscheduled_tasks[i])
                if is_ready:
                    print(f"Task {unscheduled_tasks[i]} assigned to M.")
                    self._tasks = self._tasks_provider.delete_task_from_graph(self._tasks, unscheduled_tasks[i])
                    unscheduled_tasks.remove(unscheduled_tasks[i])
                    break
    def main(self):

        self.prepare_data()

        # Find nodes with no successors.
        roots = self._tasks_provider.get_root(self._tasks)
        self._list_to_schedule = roots

        while len(self._list_to_schedule) < len(self._tasks)-1:
            # Find predecessors of labeled nodes.
            possible_next_nodes = self._get_predecessors_for_multiple_nodes(self._tasks, roots)
            possible_next_nodes = self._flatten_array(possible_next_nodes)
            possible_next_nodes = sorted(possible_next_nodes, reverse=False)

            # Choose predecessors that all successors are labeled.
            next_nodes = self._choose_tasks_labeled_succ(self._tasks, possible_next_nodes,\
                                                         self._tasks_provider)

            # Give currently released nodes labels.
            next_nodes = self._add_nodes_label(next_nodes, label=True)
            # Sort by label values and lexicographic order.
            next_nodes = self._sort_by_label_and_lex(next_nodes)
            # Omit labels.
            next_nodes = self._flatten_without_labels(next_nodes)
            self._list_to_schedule.extend(next_nodes)
            roots = next_nodes

        self._schedule_tasks()


if __name__ == "__main__":
    a_m_g = Coffman_graham()
    a_m_g.main()
