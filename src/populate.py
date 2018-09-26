from random import random, choice, randint
from evaluable_trees import FunctionNode, ConstantNode, ParameterNode

# Type for managing the population properties
class PopulationProperties:
    def __init__(self, **options):
        self.parameter_count = options.get('parameter_count', 1)
        self.max_depth = options.get('max_depth', 4)
        self.function_offset = options.get('function_offset', 0.5)
        self.parameter_offset = options.get('parameter_offset', 0.6)

# Manages common population methods, should be able to create, mutate and do cross-over
class Population:
    def __init__(self, function_wrappers, population_size, population_properties):
        self.function_wrappers = function_wrappers
        self.population_size = population_size
        self.function_offset = population_properties.function_offset
        self.parameter_offset = population_properties.parameter_offset
        self.parameter_count = population_properties.parameter_count
        self.max_depth = population_properties.max_depth
        self.individuals = []

    # Creates tree individual to fill a certain number of population
    # Should receive the remaining depth as option argument
    def __create_tree_individual(self, **options):
        function_offset = self.function_offset
        parameter_offset = self.parameter_offset
        parameter_count = self.parameter_count
        function_wrappers = self.function_wrappers

        # Defaults remaining depth to the max_depth
        remaining_depth = options.get('remaining_depth', self.max_depth)

        node_definition = random()

        # From [0, function_offset) selects a function node
        if (node_definition < function_offset and remaining_depth > 0):
            function_wrapper = choice(function_wrappers)
            generate_child_program = lambda x: self.__create_tree_individual(remaining_depth = remaining_depth - 1)
            children = map(generate_child_program, range(function_wrapper.arity))
            return FunctionNode(function_wrapper, children)

        # From [function_offset, parameter_offset) selects a parameter node
        elif (node_definition < parameter_offset):
            parameter_id = choice(range(parameter_count))
            return ParameterNode(parameter_id)

        # From [parameter_offset, 1) selects a constant node
        else:
            constant_value = randint(0, 10)
            return ConstantNode(constant_value)