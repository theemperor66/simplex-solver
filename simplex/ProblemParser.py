import re

from simplex.TableauMatrix import TableauMatrix


class LinearProblem:
    """A linear programming problem."""

    def __init__(self):
        self.name = None
        self.obj = None
        self.constraints = []
        self.variable_count = 0
        self.variables = []
        self.constraint_count = 0
        self.variable_pattern = r'x\d+'  # matches any variable x1, x2, x3, etc.
        self.operator_pattern = r'[<>]?=|[<>]'  # matches any inequality operator
        self.constant_pattern = r'[+-]?\d+'  # matches any integer constant with optional

    def extract_coefficients(self, constraint_str):
        # Extract the coefficients the term string
        coefficients = []
        constraint_str = constraint_str.replace(' ', '')
        for variable in self.variables:
            coefficient = re.search(r'([+-]?\d+)?' + variable, constraint_str)
            if coefficient is None:
                coefficients.append(0)
            else:
                coefficients.append(int(coefficient.group(1) or 1))
        return coefficients

    def parse(self, f):
        """Parse the problem from the file."""
        # TODO: do not assume that all operators are equalized
        # TODO: do not assume that all variables are x1, x2, x3, etc.
        self.constraint_count = len(f.readlines()) - 2
        f.seek(0)
        self.name = f.readline().strip()
        # read in objective function as row vector
        self.obj = []
        line = f.readline()
        variables = re.findall(self.variable_pattern, line)
        self.variables = variables
        self.variable_count = len(variables)
        # inverted coefficients to set objective function equal to zero
        coefficients = [-c for c in self.extract_coefficients(line)]
        self.obj.extend(coefficients)
        # add slack variables to objective function
        self.obj.extend([0 for _ in range(self.constraint_count)])
        # add optimization variable to objective function
        self.obj.append(1)
        # add constant to objective function
        self.obj.append(0)
        # read in constraints as row vectors
        constraint_counter = 0
        for line in f:
            cur_constraint_row = []
            # Skip blank lines and comments
            if line.strip() == '' or line.strip()[0] == '#':
                continue
            coefficients = self.extract_coefficients(line)
            constant = int(re.findall(self.constant_pattern, line)[-1])
            # first columns are the decision variable coefficients
            cur_constraint_row.extend(coefficients)
            # next columns are the slack variable coefficients
            cur_constraint_row.extend(
                [1 if i == constraint_counter else 0 for i in range(0, self.constraint_count)])
            # add column for optimization variable
            cur_constraint_row.append(0)
            # last column is the constant
            cur_constraint_row.append(constant)
            # add constraint to list of constraints
            self.constraints.append(cur_constraint_row)
            # increase constraint counter
            constraint_counter += 1


class LinearProblemParser:
    """Parse a linear programming problem from a file."""

    def __init__(self, filename):
        self.filename = filename
        self.problem = None
        self.parse()

    def parse(self):
        """Parse the problem from the file."""
        with open(self.filename, 'r') as f:
            self.problem = LinearProblem()
            self.problem.parse(f)

    def get_problem(self):
        """Return the parsed problem."""
        return self.problem

    def as_tableau(self):
        """Return the parsed problem as a tableau."""
        # instantiate tableau with variables, constraints, and objective function
        t = TableauMatrix(variables=self.problem.variables, constraints=self.problem.constraints,
                          objective=self.problem.obj)
        return t
