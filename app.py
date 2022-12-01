from flask import Flask
from flask_restful import Api
from api import Groups, Students, Courses

app = Flask(__name__)
api = Api(app)


api.add_resource(Groups, '/api/<string:version>/groups')
api.add_resource(Students, '/api/<string:version>/students')
api.add_resource(Courses, '/api/<string:version>/courses')


if __name__ == "__main__":
    app.run(debug=True)
