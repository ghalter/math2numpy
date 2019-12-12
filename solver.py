"""


"""

import numpy as np

expressions = {
    "min" : "np.amin",
    "max" : "np.amax",
    "sin" : "np.sin",
    "cos" : "np.cos",
    "tan" : "np.tan",
    "arcsin" : "np.arcsin",
    "arccos" : "np.arccos",
    "arctan" : "np.arctan",
    "^": "**"
}

checker = [
    "os", "sys", "shutil", "print", "eval", "exec", "def", "import", "="
]

def eval_expression(exp, variables):
    # "Security" ;-)
    for t in checker:
        if t in exp:
            raise ValueError("Dangerous!")

    for k, v in expressions.items():
        exp = exp.replace(k, v)

    for i, v in enumerate(variables):
        exp = exp.replace(v['name'], "Xs[" + str(i) + "]")

    string = "def func(Xs):  return " + exp
    exec(string)
    return eval("func")


if __name__ == '__main__':

    # Example usage

    var = [
        dict(name="x", info="Length", param_range=(0,100)),
        dict(name="t", info="time", param_range=(0, 1.0))
    ]

    exp = "sin(x) * 12 * cos(t)"
    f = eval_expression(exp, var)
    print(f([10,20]))