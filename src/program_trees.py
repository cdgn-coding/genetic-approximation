from evaluable_trees import FunctionWrapper

AdditionWrapper = FunctionWrapper(lambda params: params[0] + params[1], 2, 'addition')
MultiplicationWrapper = FunctionWrapper(lambda params: params[0] * params[1], 2, 'multiplication')

def ternary_if_function(parameters):
    condition = parameters[0]
    when_true_value = parameters[1]
    when_false_value = parameters[2]
    if (condition): return when_true_value
    return when_false_value

IfWrapper = FunctionWrapper(lambda params: ternary_if_function(params), 3, 'ternary_if')

def is_greater(parameters):
    a = parameters[0]
    b = parameters[1]
    if (a > b): return 1
    return 0

IsGreaterWrapper = FunctionWrapper(lambda params: is_greater(params), 2, 'is_greater')