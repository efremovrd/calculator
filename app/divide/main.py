from flask import Flask, request, jsonify, abort
from marshmallow import Schema, fields


class QuerySchema(Schema):
    eps = 1e-6
    a = fields.Number(required=True)
    b = fields.Number(required=True)
    
    def valid(self, args):
        if self.validate(args) or abs(float(args['b'])) < self.eps:
            return 1
        return 0


valid_args_num_error = 400
valid_args_str_error = 'Non valid arguments!\n'


app = Flask('plus')
schema = QuerySchema()


@app.route('/', methods=['GET'])
def get():
    args = request.args
    if schema.valid(args):
        abort(valid_args_num_error, valid_args_str_error)
    a = float(args['a'])
    b = float(args['b'])
    return jsonify({'result': a/b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
