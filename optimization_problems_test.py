import unittest
import simplex.ProblemParser as Parser


class LinearPrograms(unittest.TestCase):
    def test_max_first(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_1')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(t.matrix[-1][-1], 600)
        sol = t.get_solution()
        self.assertEqual(sol['x1'], 20)
        self.assertEqual(sol['x2'], 20)

    def test_max_second(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_2')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(t.matrix[-1][-1], 13)
        sol = t.get_solution()
        self.assertEqual(sol['x1'], 1)
        self.assertEqual(sol['x2'], 2)
        self.assertIsNone(sol.get('x3', None))

    def test_max_third(self):
        lpp = Parser.LinearProblemParser('./problems/linear_problem_3')
        lpp.parse()
        t = lpp.as_tableau()
        t.pivot_until_optimal()
        t.print_interpret_solution()
        self.assertEqual(t.matrix[-1][-1], 400)
        sol = t.get_solution()
        self.assertEqual(sol['x1'], 4)
        self.assertEqual(sol['x2'], 8)


if __name__ == '__main__':
    unittest.main()
