#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)# Print to console
    return parameter # Return to browser

@app.route('/count/<int:parameter>')
def count(parameter):
     return '\n'.join(str(i) for i in range(parameter)) + '\n'
@app.route('/math/<path:full_path>')
def math(full_path):
    try:
        parts = full_path.split('/')
        num1 = int(parts[0])
        operation = parts[1]
        num2 = int(parts[2])
    except (IndexError, ValueError):
        return "Invalid input", 400

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"
    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
