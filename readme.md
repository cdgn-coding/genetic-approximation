# Genetic Function Approximation

Approximates functions to polynomials using a genetic algorithm. An evaluable tree is composed by functions, constants and parameter evaluation. In a polynomial the parameter size is 1 [x], the functions available are multiplication and addition and constants are numbers in [-9, 9].

## How to run

After clone, run

```bash
bash ./scripts/setup.sh
```

It will install the requirements using pip.

Then run the project using

```bash
python genetic-program.py
```

### Toying with parameters

* genetic_program.py: with the target function and the training set.
* program_evolution.py: to work with the mutation and crossover mechanism.
* population.py: with the way the population is created (max depth of nodes, randomization, etc).
* environment.py: with the way the "best ones" are selected for combination and mutation.

### Example

For the function ```python target = lambda x: float(x**2 + 2x + 1)``` the output is:

```
Current generation: 260, size: 102
Best score found is 0
Best score found at the end: 0
addition
  addition
    1
    addition
      multiplication
        p0
        p0
      p0
  p0
```

### License

This project is under MIT licence and was created for educational purposes