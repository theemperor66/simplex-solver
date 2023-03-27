import unittest
import simplex.ProblemParser as Parser


class LinearPrograms(unittest.TestCase):
    def test_max_first(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_1')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(600, t.matrix[-1][-1])
        sol = t.get_solution()
        self.assertEqual(20, sol['x1'])
        self.assertEqual(20, sol['x2'])

    def test_max_second(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_2')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(13, t.matrix[-1][-1])
        sol = t.get_solution()
        self.assertEqual(1, sol['x1'])
        self.assertEqual(2, sol['x2'])
        self.assertIsNone(sol.get('x3', None))

    def test_max_third(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_3')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(400, t.matrix[-1][-1])
        sol = t.get_solution()
        self.assertEqual(4, sol['x1'])
        self.assertEqual(8, sol['x2'])

    def test_max_fourth(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_4')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(5800, t.matrix[-1][-1])
        sol = t.get_solution()
        self.assertEqual(290, sol['x1'])
        self.assertIsNone(sol.get('x2', None))


if __name__ == '__main__':
    unittest.main()
