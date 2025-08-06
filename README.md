# 🛣️ Otimizador de Roteiro de Viagem com Custo de Combustível

## 📌 Sobre o Projeto
Este projeto calcula a **menor rota entre duas cidades** e estima o **custo da viagem** com base no tipo de combustível (gasolina ou álcool), utilizando **algoritmo de Dijkstra**.

## 🤖 Tecnologias usadas
- Python 3.x
- [pandas](https://pandas.pydata.org/) - para leitura dos arquivos CSV
- [networkx](https://networkx.org/) - para criação e manipulação do grafo
- [matplotlib](https://matplotlib.org/) - para visualização do grafo

## 🔍 Como funciona
1. O usuário informa:
   - Cidade de origem
   - Cidade de destino
   - Tipo de combustível (**gasolina** ou **alcool**)
2. O programa calcula:
   - Menor rota usando **Dijkstra**
   - Distância total
   - Consumo estimado em litros
   - Custo total da viagem
3. Exibe um grafo com a rota destacada.

## 📂 Estrutura de Arquivos
```
📁 roteiro-viagem-grafo
│── main.py
│── rotas.csv
│── combustiveis.csv
│── README.md
```

## ▶️ Como executar
1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pandas networkx matplotlib
   ```
3. Execute o script:
   ```bash
   python main.py
   ```
4. Siga as instruções no terminal.

## ✅ Exemplo de Uso
```
Digite a cidade de origem: São Paulo
Digite a cidade de destino: Salvador
Digite o tipo de combustível (gasolina ou alcool): gasolina

=== Resultado ===
Menor caminho: São Paulo -> Rio de Janeiro -> Vitória -> Salvador
Distância total: 2150.00 km
Consumo estimado: 165.38 litros
Custo estimado: R$ 976.72
```

## 🎯 Próximos Passos
-  Implementar escolha entre viagem urbana (cidade) ou rodoviária (estrada) para ajustar rendimento
-  Adicionar opção de preço dinâmico via API
-  Evoluir para roteiros com múltiplas paradas
