# CP05-Dynamic-Programming 

## 👥 Nossa equipe

* Estevam Melo RM555124 
* Eduardo Lima RM554804 
* Guilherme Ulacco RM558418 
* Matheus Hostim RM556517

---

## 💰 O Desafio das Moedas  

Neste CP, o nosso objetivo foi implementar e compreender diferentes abordagens pra estar resolvendo o provblema de troca das moedas. A proposta é desenvolver um conjunto de quatro funções em Python capazes de determinar a menor quantidade de moedas necessárias para formar um determinado valor M, usando diferentes estratégias para a nossa resolução.
Nós implementamos e comparamos as quatro estratégias requisitas, sendo elas a gulosa, recursiva pura, recursiva com memoização (Top-Down) e programação dinâmica (Bottom-Up). A ideia foi testar na prática como cada uma delas funciona e ver onde cada abordagem se sairia melhor.
Durante a implementação, também deu pra perceber diferenças de desempenho entre as abordagens, dependendo do tamanho do montante e do conjunto de moedas.
O desafio basicamente consiste em determinar o menor número de moedas em que a soma seja igual a um montante M, a partir de um conjunto de valores disponíveis. A quantidade de cada moeda é ilimitada, e o objetivo é minimizar o número total de unidades usadas. Esse problema é um exemplo de problema de otimização, pois envolve encontrar a solução com o menor número de moedas e contém subproblemas que se repetem, o que faz da programação dinâmica uma técnica ideal para lidar com ele.

---

## 🔍 Análise das Funções

* **Estratégia Gulosa (Iterativa)**

A versão gulosa tenta resolver o problema pegando sempre a maior moeda possível até chegar no valor desejado. É uma ideia simples e eficiente pra alguns casos, mas não funciona sempre. Em sistemas de moedas “não padronizados”, o resultado pode sair errado. Um exemplo é usar as moedas `[4, 3, 1]` pra formar 6. O algoritmo guloso pegaria `4 + 1 + 1 = 3` moedas, mas a solução ótima seria `3 + 3 = 2` moedas. Essa abordagem não vai garantir a solução ótima pra todos os conjuntos de moedas.

**Complexidade:** `O(n)`, onde n é o número de moedas disponíveis, já que ele percorre as moedas de forma linear para encontrar o melhor encaixe.



* **Função Recursiva Pura (Ingênua)**  

A abordagem recursiva pura testa todas as combinações possíveis de moedas para formar o montante `M`. Para cada moeda disponível, a função chama a si mesma para calcular o número mínimo de moedas necessárias para o valor restante (`M - moeda`). O grande problema dessa estratégia é o **reprocessamento repetido** dos mesmos subproblemas. Por exemplo, para `M = 6` e moedas `[1, 3, 4]`, o cálculo de “quantas moedas para formar 3” aparece várias vezes em diferentes ramos da árvore recursiva. Isso faz com que o número de chamadas cresça exponencialmente com o valor de `M`, tornando o algoritmo uma escolha ruim para valores maiores.

**Complexidade de tempo:** O(n^M) ou O(2^M) dependendo da interpretação, exponencial.



* **Função Recursiva com Memoização (Top-Down)**

A versão recursiva com memoização é uma otimização direta da função antes dessa. Aqui, um dicionário ou cache é usado para armazenar os resultados de subproblemas qjá resolvidos. Assim, sempre que o algoritmo precisar denovo de um resultado já calculado, ele simplesmente o recupera do cache em vez de recalcular. Essa técnica é chamada de Top-Down porque o algoritmo começa resolvendo o problema completo e o divide recursivamente em partes menores, armazenando os resultados à medida que avança. Com isso, a complexidade cai de exponencial para quase linear em relação ao valor do montante multiplicado pela quantidade de moedas.

**Complexidade:** O(M * n), onde *M* é o montante e *n* é o número de moedas.



* **Programação Dinâmica (Bottom-Up)**

Na abordagem de Programação Dinâmica (Bottom-Up), a ideia é começar do menor subproblema possível (por exemplo, montar o valor 1) e construir uma tabela (ou vetor `dp`) que armazena o número mínimo de moedas necessário para cada valor até chegar ao montante `M`. 
Cada posição da tabela representa o melhor resultado para aquele valor específico, considerando todas as combinações de moedas possíveis. Assim, quando o algoritmo chega ao valor final `M`, ele já tem todas as soluções intermediárias prontas, evitando recursão e redundância. Essa é a forma mais eficiente e estável entre as quatro, sendo amplamente usada em problemas de otimização que envolvem sobreposição de subproblemas.

**Complexidade:** O(M * n), semelhante à versão com memoização, mas geralmente com uma leve vantagem de desempenho por evitar a sobrecarga das chamadas recursivas.



---

## 🏁 Conclusão  

Após implementar e testar as quatro funções, deu pra perceber na prática como cada uma se comporta.  
A estratégia gulosa é rápida, mas vai estar falhando em diversos casos; a recursiva pura é bem simples, mas é bem ruim pra grandes valores; já as versões com memoização e programação dinâmica conseguem reduzir drasticamente o tempo de execução, mostrando a força da reutilização de resultados intermediários.  

### 📊 Comparativo de Complexidade  

| Abordagem | Estratégia | Complexidade | Observação |
|------------|-------------|---------------|-------------|
| Gulosa | Iterativa | O(n) | Nem sempre retorna a solução ótima |
| Recursiva Pura | Top-Down sem cache | O(2^M) | Muito lenta para grandes valores |
| Recursiva com Memoização | Top-Down com cache | O(M * n) | Muito mais eficiente |
| Programação Dinâmica | Bottom-Up | O(M * n) | A mais estável e escalável |

No fim, a **Programação Dinâmica (Bottom-Up)** apresentou ser a abordagem mais eficiente e robusta.  
Ela é a melhor escolha para resolver o problema da troca de moedas, pois ela evita cálculos desnecessários, reaproveita resultados e garante sempre a solução ótima.  

---
