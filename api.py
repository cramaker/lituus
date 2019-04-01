from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

articles = {}

class ArticleSimple(Resource):
    def get(self, article_id):
        return {article_id: articles[article_id]}

    def put(self, article_id):
        articles[article_id] = request.form['data']
        return {article_id: articles[article_id]}

api.add_resource(ArticleSimple, '/<string:article_id>')

if __name__ == '__main__':
    app.run(debug=True)
