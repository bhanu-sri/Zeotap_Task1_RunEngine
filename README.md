# Rule Engine with AST

## Overview

This project implements a 3-tier rule engine that evaluates user eligibility based on attributes like age, department, income, etc., using an Abstract Syntax Tree (AST).

## Features

- Create rules using AST.
- Combine multiple rules efficiently.
- Evaluate rules against input data.
- Store rules and their AST in MongoDB.

## Requirements

- Python 3.9+
- Flask
- MongoDB
- Docker

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/rule-engine-ast.git
    cd rule-engine-ast
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start MongoDB with Docker:

    ```bash
    docker-compose up
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

## Endpoints

### `/create_rule`

- **Method**: `POST`
- **Body**:

    ```json
    {
      "rule": "(age > 30 AND salary > 50000)"
    }
    ```

- **Response**:

    ```json
    {
      "ast": "(age > 30 AND salary > 50000)"
    }
    ```

### `/combine_rules`

- **Method**: `POST`
- **Body**:

    ```json
    {
      "rules": ["rule1_string", "rule2_string"]
    }
    ```

- **Response**:

    ```json
    {
      "combined_ast": "(age > 30 AND salary > 50000 OR age < 25 AND department = 'Marketing')"
    }
    ```

### `/evaluate_rule`

- **Method**: `POST`
- **Body**:

    ```json
    {
      "ast": "(age > 30 AND salary > 50000)",
      "data": {
        "age": 35,
        "salary": 60000
      }
    }
    ```

- **Response**:

    ```json
    {
      "result": true
    }
    ```
