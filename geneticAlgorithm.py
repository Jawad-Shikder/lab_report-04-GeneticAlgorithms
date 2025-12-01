import random

def fitness(chromosome):
    n = len(chromosome)
    non_attacking = 0
    total_pairs = n * (n - 1) // 2

    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1

    return non_attacking, total_pairs

def random_chromosome(n):
    return [random.randint(1, n) for _ in range(n)]

def selection(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1 if fitness(parent1)[0] > fitness(parent2)[0] else parent2

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(chromosome, mutation_rate=0.1):
    if random.random() < mutation_rate:
        n = len(chromosome)
        idx = random.randint(0, n-1)
        chromosome[idx] = random.randint(1, n)
    return chromosome

def genetic_algorithm(n, population_size=50, max_gen=500):
    population = [random_chromosome(n) for _ in range(population_size)]

    for generation in range(max_gen):
        population = sorted(population, key=lambda x: fitness(x)[0], reverse=True)

        # Check best solution
        best_fit, max_fit = fitness(population[0])
        if best_fit == max_fit:
            print("Solution Found!")
            return population[0], generation

        new_pop = population[:10]  

while len(new_pop) < population_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    return population[0], max_gen

solution, generations = genetic_algorithm(8)

print("Final Solution:", solution)
print("Generations:", generations)
fit, max_fit = fitness(solution)
print("Fitness:", fit, "/", max_fit)
