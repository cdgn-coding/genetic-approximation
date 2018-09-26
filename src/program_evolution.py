from random import random
from copy import deepcopy
from evaluable_trees import FunctionNode

class EvolutionProperties:
    def __init__(self, **options):
        self.mutation_probability = options.get('mutation_probability', 0.1)
        self.generate_random_node = options.get('generate_random_node')

class Evolution:
    def __init__(self, evolution_properties):
        self.evolution_properties = evolution_properties

    # Mutates a given program
    def mutate(self, evaluable_tree):
        mutation_probability = self.evolution_properties.mutation_probability
        generate_random_node = self.evolution_properties.generate_random_node

        free_variable = random()

        # Given the probability, it mutates to a random node or tree
        if (free_variable < mutation_probability):
            return generate_random_node()

        cloned_tree = deepcopy(evaluable_tree)

        # Mutates, recursively, the children, if the node has children
        if isinstance(cloned_tree, FunctionNode):
            cloned_tree.children = map(
                lambda child: self.mutate(child),
                cloned_tree.children
            )

        return cloned_tree