import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# === Carregar dados ===
rotas = pd.read_csv('rotas.csv', encoding='latin1', sep=None, engine='python')
combustiveis = pd.read_csv('combustiveis.csv', encoding='latin1', sep=None, engine='python')

# Criar grafo
G = nx.Graph()
for _, row in rotas.iterrows():
    G.add_edge(row['origem'], row['destino'], weight=row['distancia'])

# Exibir cidades disponíveis
print("Cidades disponíveis:", list(G.nodes))

# Entradas do usuário
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")
combustivel = input("Digite o tipo de combustível (gasolina ou alcool): ").lower()

# Validar combustível
if combustivel not in combustiveis['tipo'].values:
    print("Tipo de combustível inválido.")
    exit()

# Obter preço e rendimento do combustível
info_comb = combustiveis[combustiveis['tipo'] == combustivel].iloc[0]
preco = info_comb['preco']
rendimento = info_comb['rendimento']

# Calcular menor caminho
try:
    menor_caminho = nx.shortest_path(G, source=origem, target=destino, weight='weight')
    distancia_total = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')
except nx.NetworkXNoPath:
    print("Não há rota entre as cidades informadas.")
    exit()

# Calcular consumo e custo
litros = distancia_total / rendimento
custo_total = litros * preco

# Exibir resultados
print("\n=== Resultado ===")
print(f"Menor caminho: {' -> '.join(menor_caminho)}")
print(f"Distância total: {distancia_total:.2f} km")
print(f"Consumo estimado: {litros:.2f} litros")
print(f"Custo estimado: R$ {custo_total:.2f}")

# Visualização do grafo
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
edges_in_path = list(zip(menor_caminho, menor_caminho[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, width=3, edge_color='red')

plt.title("Mapa de Cidades - Menor Caminho")
plt.show()
