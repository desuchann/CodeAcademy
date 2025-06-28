#### graphs ####

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def get_weight(self, edge):
    return self.edges[edge]

class Graph:
  def __init__(self, directed=False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g


#### codins ####

from random import choice
from Graph import build_tsp_graph

def print_graph(graph):
  for vertex in graph.graph_dict:
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def visited_all_nodes(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True

def travelling_salesperson(graph):
  graph_full = graph.graph_dict
  final_path = []
  visited = {vertex: 'unvisited' for vertex in graph_full}
  pick = choice(list(graph_full.keys()) )
  current_vertex = graph_full[pick]
  visited[current_vertex.value] = 'visited'
  final_path.append(current_vertex.value)
  visited_status = visited_all_nodes(visited)
  cnt = 0
  while not visited_status:
    neighbours = {}
    neighbours = {edge:current_vertex.get_weight(edge) for edge in current_vertex.get_edges() if visited[edge] == 'unvisited'}
    next_vertex_found = False
    next_vertex = ''
    while not next_vertex_found:
      if not neighbours:
        break
      min_edge = min(neighbours, key=neighbours.get)
      if visited[min_edge] == 'unvisited':        
        next_vertex = min_edge
        next_vertex_found = True
        visited[min_edge] = 'visited'
      else:
        neighbours.pop(min_edge)
      if not neighbours:
        visited_status = True
      else:
        current_vertex = graph_full[next_vertex]
        final_path.append(next_vertex)
        visited_status = visited_all_nodes(visited)
  print(f'shortest travel from {final_path[0]}: ', ' -> '.join(final_path)) 


graph = build_tsp_graph(True)
travelling_salesperson(graph)
#print_graph(graph)
