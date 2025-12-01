## N-Queens Problem Using Genetic Algorithm
## 1. Objective

The objective of this project is to apply the Genetic Algorithm (GA) technique to solve the N-Queens Problem. The aim is to arrange N queens on an NxN chessboard such that no two queens attack each other. This project also focuses on understanding GA operations such as selection, crossover, mutation, and fitness evaluation.

## 2. Procedure

**Chromosome Representation**

- Each chromosome is represented as a list of size N.
- Index = column number
- Value = row number of the queen in that column.

```Example:
[4, 2, 7, 3, 6, 8, 5, 1]
```

**Fitness Function**

- Counts how many pairs of queens are non-attacking.
- Maximum possible fitness = N * (N - 1) / 2.

**Initial Population**

Randomly generated chromosomes.

**Selection**

Tournament selection: randomly pick two chromosomes and keep the one with better fitness.

**Crossover**

Single-point crossover between two parents.

**Mutation**

Randomly replace the row position of one queen with a new value.

**Termination Condition**

The algorithm stops when:

- A chromosome reaches maximum fitness, or
- Maximum generations are reached.

## Output

```Final Solution: [4, 2, 5, 8, 1, 4, 6, 3]
Generations: 500
Fitness: 27 / 28
```

A chromosome reaches maximum fitness, or

Maximum generations are reached.
