import simplex.ProblemParser as parser

LP = parser.LinearProblemParser('./problems/linear_problem_2')
LP.parse()
LP = LP.as_tableau()
LP.print()
LP.pivot_until_optimal()
LP.print_interpret_solution()
