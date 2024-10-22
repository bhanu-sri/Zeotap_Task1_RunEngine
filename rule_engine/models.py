from mongoengine import Document, StringField, DictField, connect

connect('rule_engine')

class Rule(Document):
    rule_string = StringField(required=True)
    ast = DictField(required=True)  # Store AST as a JSON-like document
