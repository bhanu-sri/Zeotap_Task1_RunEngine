class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value (for conditions)

    def __repr__(self):
        if self.node_type == "operand":
            return f"({self.value})"
        return f"({self.left} {self.node_type} {self.right})"


import json

class RuleEngine:

    def create_rule(self, rule_string):
        # Parse rule_string and convert it into an AST (Abstract Syntax Tree)
        # For simplicity, this is a manual parser for a rule string
        # In a real-world application, this would involve a proper parsing library
        tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
        return self._parse_expression(tokens)

    def _parse_expression(self, tokens):
        token = tokens.pop(0)
        if token == '(':
            left = self._parse_expression(tokens)
            operator = tokens.pop(0)
            right = self._parse_expression(tokens)
            tokens.pop(0)  # Remove closing ')'
            return Node("operator", left, right, operator)
        else:
            # This is an operand, e.g., "age > 30"
            return Node("operand", value=token)

    def combine_rules(self, rules):
        combined_node = None
        for rule in rules:
            rule_node = self.create_rule(rule)
            if combined_node is None:
                combined_node = rule_node
            else:
                combined_node = Node("operator", combined_node, rule_node, "OR")
        return combined_node

    def evaluate_rule(self, node, data):
        # Recursively evaluate AST against input data
        if node.node_type == "operand":
            # Operand case: evaluate the condition (e.g., "age > 30")
            return self._evaluate_condition(node.value, data)
        elif node.node_type == "operator":
            if node.value == "AND":
                return self.evaluate_rule(node.left, data) and self.evaluate_rule(node.right, data)
            elif node.value == "OR":
                return self.evaluate_rule(node.left, data) or self.evaluate_rule(node.right, data)

    def _evaluate_condition(self, condition, data):
        # This is a simple condition evaluator
        attr, operator, value = condition.split()
        attr_value = data.get(attr)

        if operator == ">":
            return attr_value > int(value)
        elif operator == "<":
            return attr_value < int(value)
        elif operator == "=":
            return attr_value == value.strip("'")
        else:
            raise ValueError("Invalid operator")


