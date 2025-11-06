def troca_moedas_gulosa(M, moedas=[200, 100, 50, 20, 10, 5, 2, 1]):
    """
    Determina a menor quantidade de notas/moedas necessárias para formar o valor M usando abordagem gulosa.

    O que a função faz:
        - Percorre as moedas/notas do maior para o menor valor e usa o máximo possível de cada.
        - Retorna um dicionário (ou -1) e imprime para o usuário o detalhamento do troco.

    Parâmetros:
        M (int): Montante inteiro positivo a ser trocado.
        moedas (list de int): Lista de valores de notas/moedas (ordem decrescente).

    Valor de retorno:
        dict: Dicionário com quantidades usadas de cada nota/moeda.
        int: -1 se não for possível formar o valor.

    Complexidade:
        Ω(n), Θ(n), O(n) – n é a quantidade de tipos de moedas/notas.
    """
    resultado = {}
    M_original = M
    for moeda in moedas:
        if M >= moeda:
            qtd = M // moeda
            resultado[moeda] = qtd
            M -= qtd * moeda
    if M == 0:
        print(f"O troco a ser recebido é de R${M_original}:")
        for moeda in moedas:
            if resultado.get(moeda, 0) > 0:
                print(f" - {resultado[moeda]} x R${moeda}")
        return resultado
    else:
        print(f"Não é possível fornecer o troco de R${M_original} com as moedas/notas disponíveis.")
        return -1

def troca_moedas_recursiva(M, moedas=[200, 100, 50, 20, 10, 5, 2, 1]):
    """
    Retorna a menor quantidade de moedas/notas que somam M (recursiva pura, sem memoização).

    O que a função faz:
        - Calcula recursivamente o menor número de moedas/notas que somam M.
        - Testa todas as possibilidades e retorna -1 se não houver combinação.

    Parâmetros:
        M (int): Montante inteiro positivo a ser trocado.
        moedas (list de int): Lista de valores de notas/moedas.

    Valor de retorno:
        int: Menor número de moedas/notas, ou -1 se for impossível.

    Complexidade:
        Ω(M), Θ(M*n), O(n^M), crescimento exponencial na pior hipótese.

    Exemplos:
        troca_moedas_recursiva(7, [5, 2, 1])    # 2
        troca_moedas_recursiva(3, [2])          # -1
    """
    if M == 0:
        return 0
    if M < 0:
        return -1

    menor_qtd = float('inf')
    for moeda in moedas:
        resultado = troca_moedas_recursiva(M - moeda, moedas)
        if resultado != -1:
            menor_qtd = min(menor_qtd, 1 + resultado)
    return menor_qtd if menor_qtd != float('inf') else -1

def troca_moedas_memo(M, moedas=[200, 100, 50, 20, 10, 5, 2, 1], memo=None):
    """
    Retorna a menor quantidade de moedas/notas que somam M usando recursão com memoização (Top-Down).

    O que a função faz:
        - Usa recursão como a versão pura, mas armazena resultados intermediários em um dicionário (cache),
          evitando recomputar subproblemas já resolvidos.
        - Garante grande ganho de desempenho em relação à versão recursiva simples.
        - Retorna -1 se não for possível formar o valor M com as moedas disponíveis.

    Parâmetros:
        M (int): Montante inteiro positivo a ser trocado.
        moedas (list de int): Lista de valores de notas/moedas.
        memo (dict): Cache de resultados (usado internamente pela recursão).

    Valor de retorno:
        int: Menor número de moedas/notas, ou -1 se for impossível.

    Complexidade:
        - Tempo: Ω(M), Θ(M * n), O(M * n), onde n é o número de tipos de moedas.
        - Espaço: O(M) devido ao dicionário de memoização e à pilha recursiva.

    Exemplo:
        troca_moedas_memo(11, [5, 7, 1])   # 3 (7 + 1 + 1 + 1 + 1)
    """
    if memo is None:
        memo = {}
    if M == 0:
        return 0
    if M < 0:
        return -1
    if M in memo:
        return memo[M]

    menor_qtd = float('inf')
    for moeda in moedas:
        resultado = troca_moedas_memo(M - moeda, moedas, memo)
        if resultado != -1:
            menor_qtd = min(menor_qtd, 1 + resultado)

    memo[M] = menor_qtd if menor_qtd != float('inf') else -1
    return memo[M]

def troca_moedas_PD(M, moedas=[200, 100, 50, 20, 10, 5, 2, 1]):
    """
    Resolve o problema da troca de moedas com Programação Dinâmica (abordagem Bottom-Up).

    O que a função faz:
        - Cria um vetor dp[0..M], onde cada posição dp[i] armazena o menor número de moedas
          necessário para formar o valor i.
        - Constrói a solução iterativamente: dp[i] = min(dp[i - moeda] + 1) para todas as moedas <= i.
        - Retorna -1 se for impossível formar o montante M.

    Parâmetros:
        M (int): Montante inteiro positivo a ser trocado.
        moedas (list de int): Lista de valores de notas/moedas.

    Valor de retorno:
        int: Menor número de moedas/notas, ou -1 se for impossível.

    Complexidade:
        - Tempo: Ω(M), Θ(M * n), O(M * n), onde n é o número de tipos de moedas.
        - Espaço: O(M), pois mantém um vetor de tamanho M+1.

    Exemplo:
        troca_moedas_PD(11, [5, 7, 1])  # 3
    """
    dp = [float('inf')] * (M + 1)
    dp[0] = 0
    for i in range(1, M + 1):
        for moeda in moedas:
            if moeda <= i and dp[i - moeda] != float('inf'):
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    return dp[M] if dp[M] != float('inf') else -1

moedas = [200, 100, 50, 20, 10, 5, 2, 1]

print("=== Estrategia Gulosa ===")
troca_moedas_gulosa(188, moedas)

print("\n=== Estrategia Recursiva ===")
M = 18
resposta = troca_moedas_recursiva(M, moedas)
if resposta != -1:
    print(f"O menor número de moedas/notas para compor o troco de R${M} é {resposta}.")
else:
    print(f"Não é possível fornecer o troco de R${M} com as moedas/notas disponíveis.")

print("\n=== Estrategia Memoizacao ===")
M = 33
resposta = troca_moedas_memo(M, moedas)
if resposta != -1:
    print(f"O menor número de moedas/notas para compor o troco de R${M} é {resposta}.")
else:
    print(f"Não é possível fornecer o troco de R${M} com as moedas/notas disponíveis.")

print("\n=== Estrategia Programação Dinâmica (Bottom-Up) ===")
M = 57
resposta = troca_moedas_PD(M, moedas)
