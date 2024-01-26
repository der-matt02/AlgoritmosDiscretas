import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def kruskal_algorithm(adjacency_matrix):
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix[i])):
            if adjacency_matrix[i, j] != 0:
                edges.append((i, j, adjacency_matrix[i, j]))

    edges.sort(key=lambda x: x[2])

    # Inicializar conjuntos disjuntos
    sets = [{i} for i in range(len(adjacency_matrix))]

    mst = set()
    total_weight = 0
    for edge in edges:
        u, v, weight = edge
        u_set = next((s for s in sets if u in s), None)
        v_set = next((s for s in sets if v in s), None)

        if u_set != v_set:
            mst.add(edge)
            total_weight += weight
            sets.remove(u_set)
            sets.remove(v_set)
            sets.append(u_set.union(v_set))

    return mst, total_weight

def visualize_custom_edge_length_circular(graph, path, total_weight, node_labels):
    pos = nx.circular_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')

    # Ajustar el tamaño de la figura para dar más espacio al título
    plt.figure(figsize=(8, 8))

    nx.draw(graph, pos, with_labels=True, labels=node_labels, font_weight='bold', node_size=800, node_color="skyblue", font_size=8,
            width=1.5)

    nx.draw_networkx_edges(graph, pos, edgelist=path, edge_color='r', width=2)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8)

    plt.suptitle(f"Suma de todos los pesos: {total_weight}", y=1)  # Ajusta el valor de y según tus preferencias
    plt.show()

# Matriz de adyacencia (debes proporcionarla)
adjacency_matrix = np.array([
    [0, 25.216, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [25.216, 0, 17.287, 0, 0, 0, 0, 0, 0, 107, 0, 0, 0, 0, 0, 0],
    [0, 17.287, 0, 16.637, 0, 0, 0, 0, 0, 46.66, 0, 0, 59.3, 0, 0, 0],
    [0, 0, 16.637, 0, 8.437, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8.437, 0, 20.816, 10.9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 20.816, 0, 14.15, 0, 0, 0, 0, 0, 0, 65.93, 0, 0],
    [0, 0, 0, 0, 10.9, 14.15, 0, 44.516, 0, 0, 0, 0, 0, 103.33, 0, 0],
    [0, 0, 0, 0, 0, 0, 44.516, 0, 7.075, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7.075, 0, 0, 0, 0, 0, 73.66, 0, 85.3],
    [0, 107, 46.66, 0, 0, 0, 0, 0, 0, 0, 0, 63.783, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.875, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 63.783, 7.875, 0, 44.883, 27.887, 43.687, 0],
    [0, 0, 59.3, 0, 0, 0, 0, 0, 0, 0, 0, 44.883, 0, 38.412, 0, 0],
    [0, 0, 0, 0, 0, 65.93, 103.33, 0, 73.66, 0, 0, 27.887, 38.412, 0, 51.466, 25.85],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43.687, 0, 51.466, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 85.3, 0, 0, 0, 0, 25.85, 0, 0]
])

# Ejecutar Kruskal
mst_kruskal, total_weight_kruskal = kruskal_algorithm(adjacency_matrix)

# Crear el grafo completo
G = nx.Graph()
for edge in mst_kruskal:
    u, v, weight = edge
    G.add_edge(u, v, weight=weight)

# Etiquetas de los nodos
node_labels = {0: 'Tulcán', 1: 'Ibarra', 2: 'Quito', 3: 'Latacunga', 4: 'Ambato', 5: 'Guaranda',
               6: 'Riobamba', 7: 'Azogues', 8: 'Cuenca', 9: 'Esmeraldas', 10: 'Portoviejo',
               11: 'Manta', 12: 'S. Domingo', 13: 'Guayaquil', 14: 'Salinas', 15: 'Machala'}

# Visualizar el camino más corto encontrado por Kruskal con disposición circular
visualize_custom_edge_length_circular(G, mst_kruskal, total_weight_kruskal, node_labels)
