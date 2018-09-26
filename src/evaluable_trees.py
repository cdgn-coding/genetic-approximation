class FunctionWrapper:
    def __init__(self, function, arity, name):
        self.function = function
        self.arity = arity
        self.name = name

base_indent = '  '

class FunctionNode:
    def __init__(self, function_wrapper, children):
        self.function = function_wrapper.function
        self.name = function_wrapper.name
        self.children = children
    def evaluate(self, program_parameters):
        evaluated_children = [child.evaluate(program_parameters) for child in self.children]
        return self.function(evaluated_children)
    def debug(self, indent = 0):
        print (base_indent * indent) + self.name
        for child in self.children:
            child.debug(indent + 1)

class ParameterNode:
    def __init__(self, parameter_id):
        self.parameter_id = parameter_id
    def evaluate(self, program_parameters):
        return program_parameters[self.parameter_id]
    def debug(self, indent = 0):
        print '%sp%d' % (base_indent * indent, self.parameter_id)

class ConstantNode:
    def __init__(self, constant_value):
        self.constant_value = constant_value
    def evaluate(self, program_parameters):
        return self.constant_value
    def debug(self, indent = 0):
        print '%s%d' % (base_indent * indent, self.constant_value)