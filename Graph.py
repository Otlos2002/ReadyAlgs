from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List
from linkedlist import *


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, value: Any, index: int) -> None:
        self.data = value
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: 'Vertex', destination: 'Vertex', weight=None) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)








