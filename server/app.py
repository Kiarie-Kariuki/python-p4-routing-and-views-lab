#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(map(str, range(1, parameter + 1)))
    return numbers

    
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Can't divide by 0"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Please use one of +, -, *, div, or %."

    return result


if __name__ == '__main__':
    app.run(port=5555, debug=True)
