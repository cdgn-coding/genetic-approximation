from random import random, choice, randint
from evaluable_trees import FunctionNode, ConstantNode, ParameterNode
from program_trees import MultiplicationWrapper, AdditionWrapper, IfWrapper, IsGreaterWrapper

def make_random_program_tree(
    function_wrappers,
    parameter_count = 1,
    max_depth = 4,
    function_offset = 0.5,
    parameter_offset = 0.6):
    node_definition = random()
    if (node_definition < function_offset and max_depth > 0):
        function_wrapper = choice(function_wrappers)
        generate_child_program = lambda x: make_random_program_tree(
            function_wrappers,
            parameter_count,
            max_depth - 1,
            function_offset,
            parameter_offset,
        )
        children = map(generate_child_program, range(function_wrapper.arity))
        return FunctionNode(function_wrapper, children)
    elif (node_definition < parameter_offset):
        parameter_id = choice(range(parameter_count))
        return ParameterNode(parameter_id)
    else:
        constant_value = randint(0, 10)
        return ConstantNode(constant_value)

function_wrappers = [MultiplicationWrapper, AdditionWrapper, IfWrapper, IsGreaterWrapper]
random_program = make_random_program_tree(function_wrappers)
random_program.debug()

print '%s%d' % ('Executing program: ', random_program.evaluate([1]))