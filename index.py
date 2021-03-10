from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from routes.geocode import geocode


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.register_blueprint(geocode)


@app.route("/")
def hello():
    return "this is my flask microservice"


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)