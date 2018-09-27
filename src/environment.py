from operator import itemgetter
from program_evolution import Evolution, EvolutionProperties
from math import log
from random import random

class EnvironmentProperties:
    def __init__(self, **options):
        self.population = options.get('population')
        self.fitness_function = options.get('fitness_function')
        self.halting_tolerance = options.get('halting_tolerance', 0.1)
        self.generation_maxima = options.get('generation_maxima', 500)
        self.meritocracy_selection_index = options.get('meritocracy_selection_index', 0.7)
        self.create_new_probability = options.get('create_new_probability', 0.05)

class Environment:
    def __init__(self, environment_properties):
        # Saves the environment injected properties
        self.population = environment_properties.population
        self.halting_tolerance = environment_properties.halting_tolerance
        self.fitness_function = environment_properties.fitness_function
        self.generation_maxima = environment_properties.generation_maxima
        self.meritocracy_selection_index = environment_properties.meritocracy_selection_index
        self.create_new_probability = environment_properties.create_new_probability

        # Sets the environment's evolution
        self.evolution = Evolution(self.evolution_properties)

        # Populates the enviroment
        self.population.populate()

    @property
    def evolution_properties(self):
        create_node = lambda: self.population.create_node()
        return EvolutionProperties(generate_random_node = create_node)

    def select_index(self):
        meritocracy_selection_index = self.meritocracy_selection_index
        free_variable = random()
        return int(log(free_variable) / log(meritocracy_selection_index))

    def build_next_generation(self, ranked_individuals):
        population_size = self.population.population_size
        create_new_probability = self.create_new_probability
        evolution = self.evolution

        next_generation = []

        for _ in range(population_size):
            if random() < create_new_probability: next_generation.append(
                evolution.mutate(evolution.crossover(
                    ranked_individuals[self.select_index()][0],
                    ranked_individuals[self.select_index()][0],
                )))
            else:
                next_generation.append(self.population.create_node())

        return next_generation

    def rank_individuals(self):
        fitness_function = self.fitness_function
        individuals = self.population.individuals
        create_tuple_of_score = lambda program: (program, fitness_function(program))
        scores = [create_tuple_of_score(program) for program in individuals]
        return sorted(scores, key=itemgetter(1))

    def evolve(self):
        halting_tolerance = self.halting_tolerance
        for generation in range(self.generation_maxima):
            print '%s%d%s%d' % ('Current generation: ', generation, ', size: ', len(self.population.individuals))
            rankings = self.rank_individuals()
            best_score = rankings[0][1]

            print '%s%d' % ('Best score found is ', best_score)

            if (best_score < halting_tolerance):
                break

            next_generation = self.build_next_generation(rankings)
            self.population.set_generation(next_generation)

        self.report_results()

    def report_results(self):
        rankings = self.rank_individuals()
        print '%s%d' % ('Best score found at the end: ', rankings[0][1])
        rankings[0][0].debug()
