from flask import Flask, request, jsonify
from ast_engine import RuleEngine

app = Flask(__name__)
engine = RuleEngine()

# Endpoint to create a rule and return its AST
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')
    try:
        ast = engine.create_rule(rule_string)
        return jsonify({"ast": repr(ast)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to combine multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json.get('rules')
    try:
        combined_ast = engine.combine_rules(rules)
        return jsonify({"combined_ast": repr(combined_ast)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to evaluate a rule with input data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast_json = request.json.get('ast')
    data = request.json.get('data')
    try:
        result = engine.evaluate_rule(json.loads(ast_json), data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
