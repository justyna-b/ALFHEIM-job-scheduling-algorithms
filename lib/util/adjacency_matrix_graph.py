from util.graph import Graph

import numpy as np


class Adjacency_matrix_graph(Graph):

    def __init__(self, numVertices=17) -> None:
        super().__init__(numVertices)
        self.matrix = np.array([np.arange(numVertices)]*numVertices).transpose()

    def add_edge(self, v1, v2, weight=1):
        self.matrix[v1][v2] = -1

    def get_ready_tasks(self, tasks_matrix):
        ready = []
        for i in range(1,len(tasks_matrix)):
            relations = tasks_matrix[i]
            relations = list(filter(lambda node_val: node_val != 0, relations))
            if np.all(relations == relations[0]):
                ready.append((relations[i], i))
        ready = sorted(ready, reverse=True)
        return ready

    def delete_task_from_graph(self, tasks_matrix, task_key):
        task_idx = np.where(tasks_matrix.transpose()[0] == task_key)[0][0]
        tasks_matrix = np.delete(tasks_matrix, task_idx, 0)
        tasks_matrix = tasks_matrix
        tasks_matrix[:, task_key] = 0
        return tasks_matrix

    def get_root(self, tasks_graph):
        transposed = tasks_graph.transpose()
        roots = []
        for column in range(1, len(transposed)):
            if np.all(transposed[column] >= 0):
                roots.append(column)
        return sorted(roots, reverse=False)

    def get_predecessors(self, tasks_graph, node):
        nodes = tasks_graph[node]
        predecessors = []
        for node_key in range(1, len(nodes)):
            if nodes[node_key] == -1:
                predecessors.append(node_key)
        return predecessors

    def get_node_key(self, nodes):
        for val in nodes:
            if val != -1:
                return val

    def get_successors(self, matrix, predecessor):
        matrix = matrix.transpose()
        nodes = matrix[predecessor]
        successors = []
        for node_i in range(1, len(nodes)):
            if nodes[node_i] == -1:
                successors.append(node_i)
        return successors

    def assign_to_machine(self, ready, machines_num):
        num_of_ready_tasks = len(ready)
        if machines_num < num_of_ready_tasks:
            for m in range(machines_num):
                task = ready.pop(0)
                print(f"Task {task[0]} assigned to machine {m+1}")
                self.matrix = np.delete(self.matrix, task[1], 0)
                self.matrix[:, task] = 0
        else:
            for task in ready:
                print(f"Task {task[0]} assigned to machine {task[0]%1 + 1}")
                self.matrix = np.delete(self.matrix, task, 0)
                self.matrix[:, task] = 0

    def get_data(self):
        return self.matrix

    def create_example_graph(self):
        self.add_edge(10, 13)
        self.add_edge(10, 14)
        self.add_edge(12, 15)
        self.add_edge(4, 7)
        self.add_edge(4, 8)
        self.add_edge(1,9)
        self.add_edge(5, 10)
        self.add_edge(5, 11)
        self.add_edge(6, 12)
        self.add_edge(2, 4)
        self.add_edge(16, 5)
        self.add_edge(3, 6)
        self.add_edge(1, 2)
        self.add_edge(1, 16)
        self.add_edge(1, 3)
        return self.matrix

    def main(self):
        while len(self.matrix) > 1:
            ready = self.get_ready_tasks()
            self.assign_to_machine(ready, 2)


if __name__ == "__main__":
    a_m_g = Adjacency_matrix_graph(17)
    a_m_g.main()