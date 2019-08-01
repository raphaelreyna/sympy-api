from flask import Flask, request, jsonify
from flask_cors import CORS
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, series, Poly

application = Flask(__name__)
x = symbols('x')
CORS(application)

def expand(f, n, x0):
    f_expanded = series(f, x, n=n, x0=x0).removeO()
    f_expanded = Poly(f_expanded,x)
    coeffs = f_expanded.all_coeffs()
    coeffs = reversed(coeffs)
    coeffs_dict = {}
    i = 0
    for c in coeffs:
        coeffs_dict[str(i)] = float(c)
        i += 1
    return coeffs_dict

@application.route('/')
def taylor_series():
    fxn = request.args.get('fxn')
    deg = request.args.get('deg')

    deg = int(deg) + 1
    f = parse_expr(fxn)
    response = expand(f, deg, 0)

    return jsonify(response)

if __name__ == '__main__':
    application.run()
