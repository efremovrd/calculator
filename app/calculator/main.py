from flask import Flask, request, abort
from marshmallow import Schema, fields
from abc import abstractmethod
import requests


class QuerySchema(Schema):
    a = fields.Number(required=True)
    b = fields.Number(required=True)
    operation = fields.Str(required=True)


ok_req_status_code = 200


class Command:
    @abstractmethod
    def execute(self, a: float, b: float):
        raise NotImplementedError


class PlusCommand(Command):
    def execute(self, a: float, b: float):
        req = requests.post(url=f'http://plus:5001', data={'a': a, 'b': b})
        if req.status_code == ok_req_status_code:
            return req.json()
        else:
            abort(valid_args_num_error, valid_args_str_error)


class MultiplyCommand(Command):
    def execute(self, a: float, b: float):
        req = requests.post(url=f'http://multiply:5002', data={'a': a, 'b': b})
        if req.status_code == ok_req_status_code:
            return req.json()
        else:
            abort(valid_args_num_error, valid_args_str_error)


class MinusCommand(Command):
    def execute(self, a: float, b: float):
        req = requests.post(url=f'http://minus:5003', data={'a': a, 'b': b})
        if req.status_code == ok_req_status_code:
            return req.json()
        else:
            abort(valid_args_num_error, valid_args_str_error)


class DivideCommand(Command):
    def execute(self, a: float, b: float):
        req = requests.post(url=f'http://divide:5004', data={'a': a, 'b': b})
        if req.status_code == ok_req_status_code:
            return req.json()
        else:
            abort(valid_args_num_error, valid_args_str_error)


class ModCommand(Command):
    def execute(self, a: float, b: float):
        req = requests.post(url=f'http://mod:5006', data={'a': a, 'b': b})
        if req.status_code == ok_req_status_code:
            return req.json()
        else:
            abort(valid_args_num_error, valid_args_str_error)


valid_args_num_error = 400
valid_args_str_error = 'Non valid arguments!\n'

operations = {'+': PlusCommand(), '*': MultiplyCommand(),
              '-': MinusCommand(), '/': DivideCommand(),
              '%': ModCommand()}

app = Flask('calculator')
schema = QuerySchema()


@app.route('/', methods=['POST'])
def post():
    form = request.form
    if schema.validate(form):
        abort(valid_args_num_error, valid_args_str_error)
    a = float(form['a'])
    b = float(form['b'])
    try:
        operation = operations[form['operation']]
        return operation.execute(a, b)
    except KeyError:
        abort(valid_args_num_error, valid_args_str_error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
