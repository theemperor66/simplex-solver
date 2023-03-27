import simplex.ProblemParser as parser
import random

from simplex.TableauMatrix import TableauMatrix


# generate a random problem with d variables and c constraints
# and solve it
def solve_random_problem(dimension_count, constraints_count):
    variables = []
    constraints = []
    objective = []
    for i in range(1, dimension_count + 1):
        variables.append("x" + str(i))
        objective.append(random.randint(0, 100))
    objective = [-c for c in objective]
    # add slack variables to objective function
    objective.extend([0 for _ in range(constraints_count)])
    # add optimization variable to objective function
    objective.append(1)
    # add constant to objective function
    objective.append(0)
    constraint_counter = 0
    for i in range(constraints_count):
        constraint = []
        for j in range(dimension_count):
            constraint.append(random.randint(0, 100))
        constraint.extend(
            [1 if i == constraint_counter else 0 for i in range(0, constraints_count)])
        # add column for optimization variable
        constraint.append(0)
        # last column is the constant (random)
        constraint.append(random.randint(0, 1000))
        constraints.append(constraint)
        # increment constraint counter
        constraint_counter += 1
    print(objective)
    print("*" * 100)
    print(constraints)
    print("*" * 100)
    problem = TableauMatrix(variables, constraints, objective)
    problem.print()
    problem.pivot_until_optimal()
    problem.print_interpret_solution()


solve_random_problem(1000, 1000)
