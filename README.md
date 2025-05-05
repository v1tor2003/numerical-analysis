## Projeto: Métodos Numéricos — Resolução de Equações e Sistemas Lineares

### Descrição

Este projeto reúne a implementação de diversos métodos numéricos clássicos para resolução de equações não lineares e sistemas lineares. Os algoritmos foram desenvolvidos em Python com foco em modularidade, reutilização de componentes e geração automática de relatórios com registro das iterações.

Cada método é executado a partir de arquivos de entrada (`input.txt`) e gera relatórios detalhados em arquivos de saída (`result.txt`). O projeto é organizado por módulos, com reutilização de funções auxiliares como leitura de dados, formatação e escrita em disco.

---

### Métodos Implementados

#### Equações Não Lineares (uma variável)

* **Bisseção**
* **Posição Falsa (Regula Falsi)**
* **Newton-Raphson**
* **Secante**

#### Sistemas Lineares

**Métodos Diretos:**

* **Eliminação de Gauss**
* **Fatoração LU (Doolittle)**
* **Gauss-Jordan**

**Métodos Iterativos:**

* **Jacobi**
* **Gauss-Seidel**

---

### Estrutura do Projeto

```
/methods
│
├── utils/
│   └── file_utils.py        # Funções de leitura e escrita reutilizáveis
│
├── bisection/
│   ├── input.txt
│   ├── result.txt
│   └── bisection.py
│
├── gauss-elimination/
├── jacobi/
├── gauss-jordan/
├── ... (demais métodos)
```

---

### Formato dos Arquivos de Entrada

#### Para métodos de equações (ex: Bisseção, Newton-Raphson):

```
# input.txt
1 - (1 + x + x**2 / 2) * math.exp(-x) - 0.1     # Função f(x)
(x**2 / 2) * math.exp(-x)                       # Derivada f'(x) (se necessário)
0.1 1.0                                         # Intervalo [a, b]
0.0001                                          # Tolerância
```

#### Para sistemas lineares (ex: Gauss, LU, Jacobi):

```
# input.txt
0.0001
10 -1 2 6
-1 11 -1 25
2 -1 10 -11
```

Representa o sistema $Ax = b$, com a última coluna sendo o vetor $b$.

---

### Saída dos Relatórios

Cada método grava no `result.txt`:

* Iterações com detalhes (valores intermediários)
* Formato tabular para métodos iterativos
* Solução final do sistema ou raiz aproximada
* Mensagens de erro, se houver

---

### Requisitos

* Python 3.10+
* Nenhuma biblioteca externa necessária
* Estrutura orientada a texto (sem interface gráfica)

---

### Autor

Projeto desenvolvido por **Vitor Pires** como parte da disciplina de **DEX000086 - ANÁLISE NUMÉRICA**.


