import simplex.ProblemParser as parser

LP = parser.LinearProblemParser('./cur_proplem')
LP.parse()
LP = LP.as_tableau()
LP.print()
LP.pivot_until_optimal()
LP.print_interpret_solution()
