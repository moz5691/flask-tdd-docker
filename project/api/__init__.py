from flask_restplus import Api
from project.api.ping import ping_namespace
from project.api.users.views import users_namespace

api = Api(version="0.1", title="Users API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(users_namespace, path="/users")
