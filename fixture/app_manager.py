from fixture.route_helper import Route
from fixture.environment import Environment
from fixture.rest_helper import Rest
from fixture.string_generator_helper import StringGeneratoHelper
from fixture.data_helper import DataHelper


global baseurls


class AppManager:

    def __init__(self, env, token):
        global baseurls

        self.env = Environment(env, token)
        self.route = Route()
        self.rest = Rest()
        self.string = StringGeneratoHelper()
        self.data_help = DataHelper()
