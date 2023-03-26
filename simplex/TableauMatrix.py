class TableauMatrix:
    # constructor
    def __init__(self, variables, constraints, objective):
        self.rows = constraints + 1
        self.cols = variables * 2 + 2
        self.variable_count = variables
        self.constraint_count = constraints
        self.matrix = [objective]

    def add_variable(self):
        self.cols += 1
        self.variable_count += 1
        for i in range(self.rows):
            self.matrix[i].append(0)

    def add_constraint(self, constraint):
        self.matrix.insert(0, constraint)
        # self.rows += 1
        # self.constraint_count += 1

    def pick_pivot(self):
        # find pivot column
        pivot_col = 0
        for i in range(1, self.variable_count):
            if self.matrix[-1][i] < self.matrix[-1][pivot_col]:
                pivot_col = i

        # find pivot row
        pivot_row = 0
        for i in range(self.rows - 1):
            if self.matrix[i][pivot_col] > 0:
                pivot_row = i
                break

        for i in range(pivot_row + 1, self.rows - 1):
            if self.matrix[i][pivot_col] > 0:
                if self.matrix[i][-1] / self.matrix[i][pivot_col] < self.matrix[pivot_row][-1] / self.matrix[pivot_row][
                    pivot_col]:
                    pivot_row = i

        return pivot_row, pivot_col

    def pivot(self, pivot_row, pivot_col):
        # divide pivot row by pivot element
        pivot_element = self.matrix[pivot_row][pivot_col]
        for i in range(self.cols):
            self.matrix[pivot_row][i] /= pivot_element

        # subtract pivot row from other rows
        for i in range(self.rows):
            if i != pivot_row:
                factor = self.matrix[i][pivot_col]
                for j in range(self.cols):
                    self.matrix[i][j] -= factor * self.matrix[pivot_row][j]

    def pivot_until_optimal(self):
        while True:
            pivot_row, pivot_col = self.pick_pivot()
            if self.matrix[-1][pivot_col] >= 0:
                break
            self.pivot(pivot_row, pivot_col)

    def get_solution(self):
        # find active variables (columns with only one 1)
        active_variables = []
        for i in range(self.cols - 1):
            count = 0
            for j in range(self.rows):
                if self.matrix[j][i] == 1:
                    count += 1
            if count == 1:
                active_variables.append(i)
        # look up values for active variables
        resulting_values = [self.matrix[j][-1] for j in range(self.rows - 1) if j in active_variables]
        # pack them up with the variable names as keys into dictionary
        solution = {}
        for i in range(len(resulting_values)):
            # x1, x2, x3, ..., s1, s2, s3, ... could all be active variables
            key = "x" + str(i + 1) if i < self.variable_count else "s" + str(i - self.variable_count + 1)
            solution[key] = resulting_values[i]
        return solution

    def get_objective_value(self):
        return self.matrix[-1][-1]

    def print_interpret_solution(self):
        print("Optimal solution: ", self.get_objective_value())
        print("Solution: ", self.get_solution())

    def print(self):
        for i in range(self.rows):
            print(self.matrix[i])
