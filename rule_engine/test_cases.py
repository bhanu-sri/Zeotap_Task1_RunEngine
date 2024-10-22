import unittest
from ast_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):

    def setUp(self):
        self.engine = RuleEngine()

    def test_create_rule(self):
        rule_string = "(age > 30 AND salary > 50000)"
        ast = self.engine.create_rule(rule_string)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.node_type, "operator")

    def test_combine_rules(self):
        rule1 = "(age > 30 AND salary > 50000)"
        rule2 = "(age < 25 AND department = 'Marketing')"
        combined_ast = self.engine.combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_ast)
        self.assertEqual(combined_ast.node_type, "operator")

    def test_evaluate_rule(self):
        rule_string = "(age > 30 AND salary > 50000)"
        ast = self.engine.create_rule(rule_string)
        data = {"age": 35, "salary": 60000}
        result = self.engine.evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
