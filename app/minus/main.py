from flask import Flask, request, jsonify, abort
from marshmallow import Schema, fields


class QuerySchema(Schema):
    a = fields.Number(required=True)
    b = fields.Number(required=True)


valid_args_num_error = 400
valid_args_str_error = 'Non valid arguments!\n'


app = Flask('minus')
schema = QuerySchema()


@app.route('/', methods=['POST'])
def post():
    form = request.args
    if schema.validate(form):
        abort(valid_args_num_error, valid_args_str_error)
    a = float(form['a'])
    b = float(form['b'])
    return jsonify({'result': a-b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
