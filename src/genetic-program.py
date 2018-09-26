from population import Population, PopulationProperties
from program_trees import IfWrapper, MultiplicationWrapper, AdditionWrapper, IsGreaterWrapper

target_function = lambda x: x**2 + 2*x + 1
create_training_set = lambda P: [(x, P(x)) for x in range(200)]

def compute_function_score(training_set, evaluable_tree):
    evalue_tree = lambda x: evaluable_tree.evaluate([x])
    errors = [abs(evalue_tree(x) - y) for (x, y) in training_set]
    return sum(errors)

population_size = 2
function_wrappers = [IfWrapper, MultiplicationWrapper, AdditionWrapper, IsGreaterWrapper]

polynomial_population_properties = PopulationProperties()

polynomial_population = Population(
    function_wrappers,
    population_size,
    polynomial_population_properties
)

polynomial_population.populate()

training_set = create_training_set(target_function)

print [
    compute_function_score(training_set, evaluable_tree)
    for evaluable_tree in polynomial_population.individuals
]