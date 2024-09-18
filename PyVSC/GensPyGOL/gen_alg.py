from random import choices, sample, random, choice, randint
from gameframe import Bacteria

def fitness(agent: Bacteria):
    return agent.energy


def selection(population, k=5):
    s = sample(population, k)
    d = {}
    for individual in s:
        d[fitness(individual)] = individual
    max_key = max(d)
    return d[max_key]


def mutation(gen, prob: float = 0.02):
    mutant = []
    for chromos in gen:
        new_chromos = []
        for nucleotid in chromos:
            if random() < prob:
                new_chromos.append(randint(-10, 10))
            else:
                new_chromos.append(nucleotid)
        mutant.append(new_chromos)
    return mutant


def breeding(ind_1: Bacteria, ind_2:Bacteria):
    gen_1 = ind_1.gen
    gen_2 = ind_2.gen
    child_gen = []
    rang = True
    for common in zip(gen_1, gen_2):
        if rang:
            child_gen.append(common[0])
        else:
            child_gen.append(common[1])
        rang = not(rang)
    
    mut_child_gen =  mutation(child_gen)
    return Bacteria((0,0), gen=mut_child_gen)


def remake(population, size=100):
    new_population = []
    for _ in range(size):
        ind_1 = selection(population)
        ind_2 = selection(population)
        child = breeding(ind_1, ind_2)
        new_population.append(child)
    return new_population