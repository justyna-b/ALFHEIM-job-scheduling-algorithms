import abc


class Graph(abc.ABC):

    def __init__(self, numVertices) -> None:
        self.num_vertices = numVertices

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass
