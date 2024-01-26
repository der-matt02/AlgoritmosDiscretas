# Importación de librerías
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Funcion del algoritmo de kruskal
def algoritmo_kruskal(matriz_adyacencia):
    aristas = []
    for i in range(len(matriz_adyacencia)):
        for j in range(i + 1, len(matriz_adyacencia[i])):
            if matriz_adyacencia[i, j] != 0:
                aristas.append((i, j, matriz_adyacencia[i, j]))

    aristas.sort(key=lambda x: x[2])

    # Inicializar conjuntos disjuntos
    conjuntos = [{i} for i in range(len(matriz_adyacencia))]

    arbol_tsp = set()
    peso_total = 0
    for arista in aristas:
        u, v, peso = arista
        u_conjunto = next((s for s in conjuntos if u in s), None)
        v_conjunto = next((s for s in conjuntos if v in s), None)

        if u_conjunto != v_conjunto:
            arbol_tsp.add(arista)
            peso_total += peso
            conjuntos.remove(u_conjunto)
            conjuntos.remove(v_conjunto)
            conjuntos.append(u_conjunto.union(v_conjunto))

    return arbol_tsp, peso_total

def visualizar_circular_con_longitud_de_arista_personalizada(grafo, camino, peso_total, etiquetas_nodos):
    posiciones = nx.circular_layout(grafo)
    etiquetas_aristas = nx.get_edge_attributes(grafo, 'weight')

    # tamaño de la figura para dar más espacio al título
    plt.figure(figsize=(8, 8))

    nx.draw(grafo, posiciones, with_labels=True, labels=etiquetas_nodos, font_weight='bold', node_size=800, node_color="skyblue", font_size=8,
            width=1.5, node_edge_color="black", node_edge_width=0.5)  # Especifica el color del borde de los nodos

    nx.draw_networkx_edges(grafo, posiciones, edgelist=camino, edge_color='r', width=2)
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas_aristas, font_size=8)

    plt.suptitle(f"Suma de todos los pesos: {peso_total}", y=1)  # Ajusta el valor de y según tus preferencias
    plt.show()

# Matriz adyaciencia
matriz_adyacencia = np.array([
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

# Inicio de ejecucion
arbol_tsp_kruskal, peso_total_kruskal = algoritmo_kruskal(matriz_adyacencia)

# Creacion grafo
G = nx.Graph()
for arista in arbol_tsp_kruskal:
    u, v, peso = arista
    G.add_edge(u, v, weight=peso)

# Etiquetas de los nodos
etiquetas_nodos = {0: 'Tulcán', 1: 'Ibarra', 2: 'Quito', 3: 'Latacunga', 4: 'Ambato', 5: 'Guaranda',
                   6: 'Riobamba', 7: 'Azogues', 8: 'Cuenca', 9: 'Esmeraldas', 10: 'Portoviejo',
                   11: 'Manta', 12: 'S. Domingo', 13: 'Guayaquil', 14: 'Salinas', 15: 'Machala'}

# Visualizar kruskal
visualizar_circular_con_longitud_de_arista_personalizada(G, arbol_tsp_kruskal, peso_total_kruskal, etiquetas_nodos)
