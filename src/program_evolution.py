from random import random, choice
from copy import deepcopy
from evaluable_trees import FunctionNode

class EvolutionProperties:
    def __init__(self, **options):
        self.mutation_probability = options.get('mutation_probability', 0.7)
        self.generate_random_node = options.get('generate_random_node')
        self.swap_probability = options.get('swap_probability', 0.7)

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

    # Combines two trees
    def crossover(self, tree_a, tree_b, is_root = True):
        swap_probability = self.evolution_properties.swap_probability
        free_variable = random()

        if (free_variable < swap_probability and not is_root):
            return deepcopy(tree_b)

        next_gen = deepcopy(tree_a)

        if (isinstance(tree_a, FunctionNode) and isinstance(tree_b, FunctionNode)):
            get_gen_choice = lambda: choice(tree_b.children)
            next_gen.children = [self.crossover(x, get_gen_choice(), False) for x in tree_a.children]

        return next_gen