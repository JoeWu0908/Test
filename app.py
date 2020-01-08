import pandas as pd
from flask import jsonify
import pickle
from flask import Flask, request
from flask_restful import Api, Resource

# load model
model = pickle.load(open('./model.pkl', 'rb'))

# app
app = Flask(__name__)
api = Api(app)



class Helloworld(Resource):

    def get(self):
        return 'MODEL TEST flask_RESTFUL'


class Model_test(Resource):

    def post(self):
        """ create a user"""
        # print(request.get_json())

        data = request.get_json(force=True)
        # print(data)
        # convert data into dataframe
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)

        # predictions
        result = model.predict(data_df)

        # send back to browser
        output = {'results': int(result[0])}

        return jsonify(results=output)


api.add_resource(Helloworld, '/')
api.add_resource(Model_test, '/model')


if __name__ == "__main__":
    app.run()

