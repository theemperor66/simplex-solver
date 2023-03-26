import unittest
import simplex.TableauMatrix as tableau


class LinearPrograms(unittest.TestCase):
    def test_max_first(self):
        t = tableau.TableauMatrix(3, 3, [-5, -4, -3, 0, 0, 0, 1, 0])
        t.add_constraint([2, 3, 1, 1, 0, 0, 0, 5])
        t.add_constraint([4, 1, 2, 0, 1, 0, 0, 11])
        t.add_constraint([3, 4, 2, 0, 0, 1, 0, 8])
        t.pivot_until_optimal()
        t.interpret_solution()
        self.assertEqual(t.matrix[-1][-1], 13)

    def test_max_second(self):
        t = tableau.TableauMatrix(2, 2, [-20, -10, 0, 0, 1, 0])
        t.add_constraint([1, 1, 1, 0, 0, 40])
        t.add_constraint([4, 1, 0, 1, 0, 100])
        t.pivot_until_optimal()
        t.interpret_solution()
        self.assertEqual(t.matrix[-1][-1], 600)


if __name__ == '__main__':
    unittest.main()
